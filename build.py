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

GITHUB_PATTERNS_URL = (
    "https://github.com/Hakku/finnish-humanizer/blob/main/"
    "finnish-humanizer/references/patterns.md"
)
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
    "windsurf": {"path": "windsurf/finnish-humanizer.md"},
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

CHAR_LIMITS = {"windsurf": 12_000}


def parse_skill():
    """Return (body, short_description) from SKILL.md."""
    text = SKILL_MD.read_text(encoding="utf-8")
    parts = text.split("---", 2)
    if len(parts) < 3:
        raise ValueError("SKILL.md: frontmatter puuttuu")

    fm = parts[1]
    match = re.search(r"^description:\s*(.+)$", fm, re.MULTILINE)
    desc_full = match.group(1).strip() if match else ""
    desc_short = ". ".join(desc_full.split(". ")[:2]) + "."

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
        if name in CHAR_LIMITS and chars > CHAR_LIMITS[name]:
            warn = f"  [!] RAJA YLITETTY ({CHAR_LIMITS[name]:,})"
        results.append((name, cfg["path"], chars, warn))

    return results


def build_chatgpt_patterns():
    """Generate dist/chatgpt/patterns.md: source copy without TOC."""
    text = PATTERNS_MD.read_text(encoding="utf-8")
    text = re.sub(
        r"\n## Sisällysluettelo\n.*?\n---\n",
        "\n---\n",
        text,
        count=1,
        flags=re.DOTALL,
    )
    text = text.replace(
        "esimerkkeineen. SKILL.md sisältää 6 kanonista esimerkkiä;"
        " tämä tiedosto sisältää loput.",
        "esimerkkeineen + 5 tyylimerkintää.",
    )
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
            short = ". ".join(desc.split(". ")[:2]) + "."
            if len(short) > 200:
                short = short[:197] + "..."
            kept.append(f"description: {short}")
    stripped = "---\n" + "\n".join(kept) + "\n---" + parts[2]

    skill_path = DIST / "finnish-humanizer.skill"
    with zipfile.ZipFile(skill_path, "w", zipfile.ZIP_DEFLATED) as zf:
        zf.writestr("finnish-humanizer/SKILL.md", stripped)
        zf.write(PATTERNS_MD, "finnish-humanizer/references/patterns.md")
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

    skill_path = build_skill()
    print(f"\nSKILL: {skill_path.relative_to(REPO)}")
    with zipfile.ZipFile(skill_path) as zf:
        print(f"  Sisalto: {', '.join(zf.namelist())}")

    print("\n[!] dist/chatgpt/instructions.md on manuaalinen -- tarkista synkroni")
    print("Valmis.")


if __name__ == "__main__":
    main()
