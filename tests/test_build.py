"""Integration tests for build.py — stdlib only, no pytest dependency."""

import re
import sys
import unittest
import zipfile
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).parent.parent))
import build

# ---------------------------------------------------------------------------
# Test fixtures
# ---------------------------------------------------------------------------

MINIMAL_SKILL = """\
---
name: test-skill
description: Lyhyt kuvaus. Toinen lause.
---

# Body

Content here. ks. references/patterns.md
"""

SKILL_NO_DESCRIPTION = """\
---
name: test-skill
---

# Body

Content here.
"""

SKILL_ONE_DASH = """\
---
name: test-skill
description: Kuvaus.
"""

SKILL_LONG_DESCRIPTION = """\
---
name: test-skill
description: Tämä ensimmäinen lause on kirjoitettu tarkoituksella hyvin pitkäksi jotta se yksinäänkin lähestyy merkkimäärän rajaa ja vie tilaa. Tämä toinen lause on yhtä lailla pitkä ja sisältää runsaasti tekstiä varmistaakseen että yhteispituus ylittää selvästi kaksisataa merkkiä. Kolmas lause.
---

# Body

Content here. ks. references/patterns.md
"""

MINIMAL_PATTERNS = """\
# Finnish Humanizer: Täysi patternilista

Kuvaus.

## Sisällysluettelo

- [Suomenkieliset](#suomenkieliset)

---

## Suomenkieliset

Patternit tässä.
"""

PATTERNS_NO_TOC = """\
# Finnish Humanizer: Täysi patternilista

Kuvaus.

## Suomenkieliset

Patternit tässä.
"""


# ---------------------------------------------------------------------------
# Base class
# ---------------------------------------------------------------------------

class TempDirTestCase(unittest.TestCase):
    def setUp(self):
        self._tmpdir = TemporaryDirectory()
        self.tmpdir = Path(self._tmpdir.name)

    def tearDown(self):
        self._tmpdir.cleanup()


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestTruncateDesc(unittest.TestCase):

    def test_single_sentence_with_period(self):
        """Single sentence ending with period must not produce double period."""
        result = build._truncate_desc("Lyhyt kuvaus.")
        self.assertFalse(result.endswith(".."), f"Kaksoispistet: {result!r}")
        self.assertEqual(result, "Lyhyt kuvaus.")

    def test_two_sentences_with_period(self):
        """Two-sentence input must not produce double period."""
        result = build._truncate_desc("Lause yksi. Lause kaksi.")
        self.assertFalse(result.endswith(".."), f"Kaksoispistet: {result!r}")
        self.assertEqual(result, "Lause yksi. Lause kaksi.")

    def test_three_sentences_truncates_to_two(self):
        """Three sentences: only first two are kept."""
        result = build._truncate_desc("Yksi. Kaksi. Kolme.")
        self.assertEqual(result, "Yksi. Kaksi.")

    def test_truncation_over_limit(self):
        """Content over limit gets '...' suffix."""
        long = "A" * 150 + ". " + "B" * 100 + "."
        result = build._truncate_desc(long, limit=200)
        self.assertLessEqual(len(result), 200)
        self.assertTrue(result.endswith("..."))


class TestParseSkill(TempDirTestCase):

    def _skill_path(self, content: str) -> Path:
        p = self.tmpdir / "SKILL.md"
        p.write_text(content, encoding="utf-8")
        return p

    def test_parse_skill_valid(self):
        p = self._skill_path(MINIMAL_SKILL)
        with patch.object(build, "SKILL_MD", p):
            body, desc_short = build.parse_skill()
        self.assertIn("Content here.", body)
        self.assertIn("Lyhyt kuvaus.", desc_short)

    def test_parse_skill_missing_delimiter(self):
        """Single --- raises ValueError (len(parts) < 3)."""
        p = self._skill_path(SKILL_ONE_DASH)
        with patch.object(build, "SKILL_MD", p):
            with self.assertRaises(ValueError):
                build.parse_skill()

    def test_parse_skill_missing_description(self):
        """Missing description field raises ValueError."""
        p = self._skill_path(SKILL_NO_DESCRIPTION)
        with patch.object(build, "SKILL_MD", p):
            with self.assertRaises(ValueError):
                build.parse_skill()


class TestBuildPlatforms(unittest.TestCase):

    def test_build_all_platforms(self):
        """All platform files created; LOCAL_REF replaced with GitHub URL."""
        with TemporaryDirectory() as tmpdir:
            dist = Path(tmpdir)
            with patch.object(build, "DIST", dist):
                results = build.build_platforms(
                    "# Body\nContent. ks. references/patterns.md\n",
                    "Kuvaus. Toinen.",
                )
            self.assertEqual(len(results), len(build.PLATFORMS))
            for _name, path, _chars, _warn in results:
                out = dist / path
                self.assertTrue(out.exists(), f"{path} ei löydy")
                content = out.read_text(encoding="utf-8")
                self.assertNotIn(
                    "ks. references/patterns.md",
                    content,
                    f"{path} sisältää LOCAL_REF",
                )
                self.assertIn(
                    build.GITHUB_PATTERNS_URL,
                    content,
                    f"{path} ei sisällä GITHUB_PATTERNS_URL",
                )

    def test_windsurf_char_limit_ok(self):
        """Content under windsurf limit produces no warning."""
        body = "x" * 100 + ". ks. references/patterns.md"
        with TemporaryDirectory() as tmpdir:
            dist = Path(tmpdir)
            with patch.object(build, "DIST", dist):
                results = build.build_platforms(body, "Kuvaus.")
        windsurf = next(r for r in results if r[0] == "windsurf")
        self.assertEqual(windsurf[3], "", f"Odottamaton varoitus: {windsurf[3]!r}")

    def test_windsurf_char_limit_exceeded(self):
        """Content over windsurf limit produces RAJA YLITETTY warning."""
        body = "x" * 12_001 + ". ks. references/patterns.md"
        with TemporaryDirectory() as tmpdir:
            dist = Path(tmpdir)
            with patch.object(build, "DIST", dist):
                results = build.build_platforms(body, "Kuvaus.")
        windsurf = next(r for r in results if r[0] == "windsurf")
        self.assertIn("RAJA YLITETTY", windsurf[3])

    def test_frontmatter_platforms_have_yaml_header(self):
        """Platforms with frontmatter lambda emit --- blocks."""
        frontmatter_platforms = {"cursor", "copilot", "continue"}
        no_frontmatter_platforms = {"windsurf", "cline", "jetbrains", "generic", "agents"}
        with TemporaryDirectory() as tmpdir:
            dist = Path(tmpdir)
            with patch.object(build, "DIST", dist):
                results = build.build_platforms(
                    "# Body\nContent. ks. references/patterns.md\n",
                    "Kuvaus.",
                )
            for name, path, _chars, _warn in results:
                content = (dist / path).read_text(encoding="utf-8")
                if name in frontmatter_platforms:
                    self.assertTrue(
                        content.startswith("---\n"),
                        f"{name}: odotettu frontmatter, ei löydy",
                    )
                elif name in no_frontmatter_platforms:
                    self.assertFalse(
                        content.startswith("---"),
                        f"{name}: ei pitäisi olla frontmatteria",
                    )


class TestBuildSkill(TempDirTestCase):

    def test_build_skill_zip_contents(self):
        """Zip contains exactly the right files; description ≤ 200 chars."""
        skill_md = self.tmpdir / "SKILL.md"
        skill_md.write_text(MINIMAL_SKILL, encoding="utf-8")
        patterns_md = self.tmpdir / "patterns.md"
        patterns_md.write_text("# Patternit\n", encoding="utf-8")
        dist = self.tmpdir / "dist"
        dist.mkdir()
        with (
            patch.object(build, "SKILL_MD", skill_md),
            patch.object(build, "PATTERNS_MD", patterns_md),
            patch.object(build, "DIST", dist),
        ):
            skill_path = build.build_skill()

        with zipfile.ZipFile(skill_path) as zf:
            names = set(zf.namelist())
            content = zf.read("finnish-humanizer/SKILL.md").decode("utf-8")

        self.assertIn("finnish-humanizer/SKILL.md", names)
        self.assertIn("finnish-humanizer/references/patterns.md", names)

        m = re.search(r"^description:\s*(.+)$", content, re.MULTILINE)
        self.assertIsNotNone(m, "description ei löydy zip-tiedostosta")
        self.assertLessEqual(len(m.group(1).strip()), 200)

    def test_build_skill_long_description_truncated(self):
        """Description over 200 chars is truncated to ≤200 and ends with '...'."""
        skill_md = self.tmpdir / "SKILL.md"
        skill_md.write_text(SKILL_LONG_DESCRIPTION, encoding="utf-8")
        patterns_md = self.tmpdir / "patterns.md"
        patterns_md.write_text("# Patternit\n", encoding="utf-8")
        dist = self.tmpdir / "dist"
        dist.mkdir()
        with (
            patch.object(build, "SKILL_MD", skill_md),
            patch.object(build, "PATTERNS_MD", patterns_md),
            patch.object(build, "DIST", dist),
        ):
            skill_path = build.build_skill()

        with zipfile.ZipFile(skill_path) as zf:
            content = zf.read("finnish-humanizer/SKILL.md").decode("utf-8")
        m = re.search(r"^description:\s*(.+)$", content, re.MULTILINE)
        self.assertIsNotNone(m)
        desc = m.group(1).strip()
        self.assertLessEqual(len(desc), 200)
        self.assertTrue(desc.endswith("..."), f"Ei pääty '...': {desc!r}")

    def test_build_skill_missing_delimiter(self):
        """Single --- raises ValueError."""
        skill_md = self.tmpdir / "SKILL.md"
        skill_md.write_text(SKILL_ONE_DASH, encoding="utf-8")
        patterns_md = self.tmpdir / "patterns.md"
        patterns_md.write_text("# Patternit\n", encoding="utf-8")
        dist = self.tmpdir / "dist"
        dist.mkdir()
        with (
            patch.object(build, "SKILL_MD", skill_md),
            patch.object(build, "PATTERNS_MD", patterns_md),
            patch.object(build, "DIST", dist),
        ):
            with self.assertRaises(ValueError):
                build.build_skill()


class TestDescShort(TempDirTestCase):

    def test_desc_short_single_sentence_with_period(self):
        """Single-sentence description ending with period must not produce double period."""
        skill_md = self.tmpdir / "SKILL.md"
        skill_md.write_text(
            "---\nname: x\ndescription: Lyhyt kuvaus.\n---\n\n# Body\n",
            encoding="utf-8",
        )
        with patch.object(build, "SKILL_MD", skill_md):
            _, desc_short = build.parse_skill()
        self.assertFalse(desc_short.endswith(".."), f"Kaksoispistet: {desc_short!r}")
        self.assertEqual(desc_short, "Lyhyt kuvaus.")

    def test_desc_short_two_sentences_with_period(self):
        """Two-sentence description must not produce double period."""
        skill_md = self.tmpdir / "SKILL.md"
        skill_md.write_text(
            "---\nname: x\ndescription: Lyhyt kuvaus. Toinen lause.\n---\n\n# Body\n",
            encoding="utf-8",
        )
        with patch.object(build, "SKILL_MD", skill_md):
            _, desc_short = build.parse_skill()
        self.assertFalse(desc_short.endswith(".."), f"Kaksoispistet: {desc_short!r}")
        self.assertEqual(desc_short, "Lyhyt kuvaus. Toinen lause.")


class TestChatGPTPatterns(TempDirTestCase):

    def test_chatgpt_patterns_no_toc(self):
        """Output has no TOC and uses the fixed CHATGPT_INTRO."""
        patterns_md = self.tmpdir / "patterns.md"
        patterns_md.write_text(MINIMAL_PATTERNS, encoding="utf-8")
        dist = self.tmpdir / "dist"
        dist.mkdir()
        with (
            patch.object(build, "PATTERNS_MD", patterns_md),
            patch.object(build, "DIST", dist),
        ):
            build.build_chatgpt_patterns()

        out = dist / "chatgpt" / "patterns.md"
        content = out.read_text(encoding="utf-8")

        self.assertNotIn("Sisällysluettelo", content)
        self.assertIn("instructions.md sisältää kanonisia esimerkkejä", content)
        self.assertTrue(
            content.startswith("# Finnish Humanizer: Täysi patternilista"),
            "Intro-otsikko puuttuu",
        )

    def test_chatgpt_patterns_missing_toc_raises(self):
        """patterns.md without TOC section raises ValueError."""
        patterns_md = self.tmpdir / "patterns.md"
        patterns_md.write_text(PATTERNS_NO_TOC, encoding="utf-8")
        dist = self.tmpdir / "dist"
        dist.mkdir()
        with (
            patch.object(build, "PATTERNS_MD", patterns_md),
            patch.object(build, "DIST", dist),
        ):
            with self.assertRaises(ValueError) as ctx:
                build.build_chatgpt_patterns()
        self.assertIn("TOC", str(ctx.exception))


if __name__ == "__main__":
    unittest.main()
