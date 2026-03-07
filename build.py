"""Finnish Humanizer build script.

Generates all dist files from the canonical finnish-humanizer/SKILL.md source.
Usage: py build.py
"""

import re
import zipfile
from pathlib import Path

REPO = Path(__file__).parent
SKILL_MD = REPO / "finnish-humanizer" / "SKILL.md"
PATTERNS_MD = REPO / "finnish-humanizer" / "references" / "patterns.md"
DIST = REPO / "dist"

GITHUB_REPO = "https://github.com/Hakku/finnish-humanizer"
GITHUB_PATTERNS_URL = f"{GITHUB_REPO}/blob/main/finnish-humanizer/references/patterns.md"
LOCAL_REF = "ks. references/patterns.md"

PLATFORMS = {
    "cursor": {
        "path": "cursor/finnish-humanizer.mdc",
        "frontmatter": lambda d: [
            f"description: {d}",
            'globs: "**/*.md,**/*.txt"',
            "alwaysApply: false",
        ],
    },
    "copilot": {
        "path": "copilot/finnish-humanizer.instructions.md",
        "frontmatter": lambda d: [
            "name: Finnish Humanizer",
            'applyTo: "**/*.md,**/*.txt"',
            f"description: {d}",
        ],
    },
    "windsurf": {"path": "windsurf/finnish-humanizer.md", "char_limit": 12_000},
    "cline": {"path": "cline/finnish-humanizer.md"},
    "continue": {
        "path": "continue/finnish-humanizer.md",
        "frontmatter": lambda d: [
            "name: finnish-humanizer",
            'globs: "**/*.md,**/*.txt"',
            "alwaysApply: false",
            f"description: {d}",
        ],
    },
    "jetbrains": {"path": "jetbrains/finnish-humanizer.md"},
    "generic": {"path": "generic/finnish-humanizer.md"},
    "agents": {"path": "agents/AGENTS.md"},
}

CHATGPT_INTRO = (
    "# Finnish Humanizer: Täysi patternilista\n\n"
    "Kaikki 26 AI-patternia esimerkkeineen + 5 tyylimerkintää."
    " instructions.md sisältää kanonisia esimerkkejä; tämä tiedosto sisältää loput.\n\n"
    "---"
)


def _truncate_desc(desc_full: str, limit: int = 200) -> str:
    """Return at most 2 sentences from desc_full, truncated to limit chars."""
    short = ". ".join(desc_full.split(". ")[:2]).rstrip(".") + "."
    if len(short) > limit:
        short = short[: limit - 3] + "..."
    return short


def parse_skill():
    """Return (body, short_description) from SKILL.md."""
    text = SKILL_MD.read_text(encoding="utf-8")
    parts = text.split("---", 2)
    if len(parts) < 3:
        raise ValueError("SKILL.md: frontmatter puuttuu")

    fm = parts[1]
    match = re.search(r"^description:\s*(.+)$", fm, re.MULTILINE)
    if not match:
        raise ValueError("SKILL.md: description-kenttä puuttuu frontmatterista")
    desc_full = match.group(1).strip()
    if not desc_full:
        raise ValueError("SKILL.md: description-kenttä on tyhjä")
    desc_short = _truncate_desc(desc_full)

    body = parts[2].lstrip("\n")
    return body, desc_short


def build_platforms(body, desc):
    """Generate platform-specific dist files."""
    dist_body = body.replace(LOCAL_REF, GITHUB_PATTERNS_URL)
    results = []

    for name, cfg in PLATFORMS.items():
        out = DIST / cfg["path"]
        out.parent.mkdir(parents=True, exist_ok=True)

        fm_fn = cfg.get("frontmatter")
        if fm_fn:
            fm_lines = fm_fn(desc)
            content = "---\n" + "\n".join(fm_lines) + "\n---\n\n" + dist_body
        else:
            content = dist_body

        out.write_text(content, encoding="utf-8", newline="\n")
        chars = len(content)
        warn = ""
        limit = cfg.get("char_limit")
        if limit and chars > limit:
            warn = f"  [!] RAJA YLITETTY ({limit:,})"
        results.append((name, cfg["path"], chars, warn))

    return results


def build_chatgpt_patterns():
    """Generate dist/chatgpt/patterns.md: source copy without TOC, fixed intro."""
    text = PATTERNS_MD.read_text(encoding="utf-8")

    # Remove TOC — fail build if not found (structure guard)
    text, n = re.subn(
        r"\n## Sisällysluettelo\n.*?\n---\n",
        "\n---\n",
        text,
        count=1,
        flags=re.DOTALL,
    )
    if n == 0:
        raise ValueError(
            "build_chatgpt_patterns: TOC-korvaus epäonnistui — patterns.md:n rakenne muuttunut"
        )

    # Structural intro replace: swap everything before first ## heading
    first_pattern = text.find("\n## ")
    if first_pattern == -1:
        raise ValueError("build_chatgpt_patterns: ensimmäistä ## -otsikkoa ei löydy")
    text = CHATGPT_INTRO + text[first_pattern:]

    out = DIST / "chatgpt" / "patterns.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8", newline="\n")
    return len(text)


def build_skill():
    """Build dist/finnish-humanizer.skill for Claude.ai.

    Claude.ai skill upload only accepts name + description in YAML frontmatter.
    Strip license, allowed-tools, metadata before packaging.
    """
    text = SKILL_MD.read_text(encoding="utf-8")
    parts = text.split("---", 2)
    if len(parts) < 3:
        raise ValueError("SKILL.md: frontmatter puuttuu")

    fm = parts[1]
    kept = []
    for line in fm.strip().splitlines():
        if re.match(r"^name:", line):
            kept.append(line)
        elif re.match(r"^description:", line):
            desc = line.split(":", 1)[1].strip()
            kept.append(f"description: {_truncate_desc(desc)}")
    stripped = "---\n" + "\n".join(kept) + "\n---" + parts[2]

    skill_path = DIST / "finnish-humanizer.skill"
    try:
        with zipfile.ZipFile(skill_path, "w", zipfile.ZIP_DEFLATED) as zf:
            zf.writestr("finnish-humanizer/SKILL.md", stripped)
            zf.write(PATTERNS_MD, "finnish-humanizer/references/patterns.md")
    except OSError as e:
        skill_path.unlink(missing_ok=True)
        raise RuntimeError(f"Skill zip -kirjoitus epäonnistui: {e}") from e
    return skill_path


def main():
    body, desc = parse_skill()
    print("Finnish Humanizer -- Build\n")

    results = build_platforms(body, desc)
    print("Alustapaketit:")
    for name, path, chars, warn in results:
        print(f"  {name:12s} {path:50s} {chars:>6,} merkkia{warn}")

    chars = build_chatgpt_patterns()
    print(f"  {'chatgpt':12s} {'chatgpt/patterns.md':50s} {chars:>6,} merkkia")
    print("[!] dist/chatgpt/ manuaaliset tiedostot (ei buildattuja):")
    print("    instructions.md -- erilainen rakenne, ei XML-tageja")
    print("    GPT-SPEC.md     -- GPT-konfiguraatio")
    print("    test-texts.md   -- testiaineisto")
    print("    Tarkista synkroni kun SKILL.md body muuttuu.")

    skill_path = build_skill()
    print(f"\nSKILL: {skill_path.relative_to(REPO)}")
    with zipfile.ZipFile(skill_path) as zf:
        print(f"  Sisalto: {', '.join(zf.namelist())}")

    print("\nValmis.")


if __name__ == "__main__":
    main()
