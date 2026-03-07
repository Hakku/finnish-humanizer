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

MINIMAL_PATTERNS = """\
# Finnish Humanizer: Täysi patternilista

Kuvaus.

## Sisällysluettelo

- [Suomenkieliset](#suomenkieliset)

---

## Suomenkieliset

Patternit tässä.
"""


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestParseSkill(unittest.TestCase):

    def setUp(self):
        self._tmpdir = TemporaryDirectory()
        self.tmpdir = Path(self._tmpdir.name)

    def tearDown(self):
        self._tmpdir.cleanup()

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
        """All 8 platform files created; LOCAL_REF replaced with GitHub URL."""
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


class TestBuildSkill(unittest.TestCase):

    def setUp(self):
        self._tmpdir = TemporaryDirectory()
        self.tmpdir = Path(self._tmpdir.name)

    def tearDown(self):
        self._tmpdir.cleanup()

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


class TestDescShort(unittest.TestCase):

    def setUp(self):
        self._tmpdir = TemporaryDirectory()
        self.tmpdir = Path(self._tmpdir.name)

    def tearDown(self):
        self._tmpdir.cleanup()

    def test_desc_short_single_sentence(self):
        """Single-sentence description must not produce double period."""
        skill_md = self.tmpdir / "SKILL.md"
        skill_md.write_text(
            "---\nname: x\ndescription: Lyhyt kuvaus\n---\n\n# Body\n",
            encoding="utf-8",
        )
        with patch.object(build, "SKILL_MD", skill_md):
            _, desc_short = build.parse_skill()
        self.assertFalse(desc_short.endswith(".."), f"Kaksoispistet: {desc_short!r}")


class TestChatGPTPatterns(unittest.TestCase):

    def setUp(self):
        self._tmpdir = TemporaryDirectory()
        self.tmpdir = Path(self._tmpdir.name)

    def tearDown(self):
        self._tmpdir.cleanup()

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
        # Intro starts with the expected title line
        self.assertTrue(
            content.startswith("# Finnish Humanizer: Täysi patternilista"),
            "Intro-otsikko puuttuu",
        )


if __name__ == "__main__":
    unittest.main()
