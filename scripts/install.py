#!/usr/bin/env python3
"""Link this checkout's skill and add a scoped Sites instruction; stdlib only."""
import argparse
import os
from pathlib import Path

NAME = "sites-park-design"
START = "<!-- sites-park-design:start -->"
END = "<!-- sites-park-design:end -->"
SOURCE = Path(__file__).resolve().parents[1] / "skills" / NAME


def hook(skill_path):
    return (
        f"{START}\n"
        "## Default Sites art direction\n\n"
        "For new ChatGPT Sites and explicitly requested Site redesigns, read "
        f"`{skill_path / 'SKILL.md'}` and apply it alongside Sites building before "
        "choosing the visual direction. Load frontend-design when available as "
        "the general design foundation, with this companion supplying Sites-specific "
        "constraints. Use one combined plan and review. Select the park and concept internally; "
        "the user does not need to request the skill or art-direct the build. "
        "This is internal exploration before Sites' single visual thesis, not "
        "user-facing design options. Explicit user branding and references take "
        "precedence. Preserve existing design during ordinary maintenance. "
        "Do not apply this to unrelated web projects or non-Sites work.\n"
        f"{END}"
    )


def update_text(text, block):
    if START not in text and END not in text:
        return text + ("\n\n" if text and not text.endswith("\n\n") else "") + block + "\n"
    if text.count(START) != 1 or text.count(END) != 1:
        raise ValueError("Malformed or duplicate managed block; no changes made")
    begin, finish = text.index(START), text.index(END) + len(END)
    if finish < begin:
        raise ValueError("Reversed managed markers; no changes made")
    return text[:begin] + block + text[finish:]


def install(skills_dir, instructions, source=SOURCE):
    skills_dir, instructions, source = map(lambda p: Path(p).absolute(), (skills_dir, instructions, source))
    link = skills_dir / NAME
    if not (source / "SKILL.md").is_file():
        raise ValueError(f"Missing skill at {source}")
    if "`" in str(link) or "\n" in str(link):
        raise ValueError("Installation path cannot contain backticks or newlines")
    if instructions.with_name("AGENTS.override.md").exists():
        raise ValueError("AGENTS.override.md shadows this hook; integrate explicitly instead")
    if instructions.is_symlink():
        raise ValueError("Refusing to modify a symlinked instruction file")
    if link.exists() or link.is_symlink():
        if not link.is_symlink() or link.resolve() != source.resolve():
            raise ValueError(f"Refusing to replace existing skill: {link}")
    old = instructions.read_text() if instructions.exists() else ""
    new = update_text(old, hook(link))
    skills_dir.mkdir(parents=True, exist_ok=True)
    instructions.parent.mkdir(parents=True, exist_ok=True)
    created = not link.is_symlink()
    if created:
        link.symlink_to(source, target_is_directory=True)
    try:
        if new != old:
            instructions.write_text(new)
    except OSError:
        if created:
            link.unlink()
        raise
    return link, instructions


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    scope = parser.add_mutually_exclusive_group(required=True)
    scope.add_argument("--workspace", type=Path, help="Enable for one Sites workspace")
    scope.add_argument("--user", action="store_true", help="Enable for all local Codex Sites work")
    args = parser.parse_args()
    if args.user:
        skills_dir = Path.home() / ".agents" / "skills"
        instructions = Path(os.environ.get("CODEX_HOME", str(Path.home() / ".codex"))) / "AGENTS.md"
    else:
        workspace = args.workspace.expanduser().resolve()
        if not workspace.is_dir():
            parser.error("Workspace must already exist")
        skills_dir = workspace / ".agents" / "skills"
        instructions = workspace / "AGENTS.md"
    try:
        link, instructions = install(skills_dir, instructions)
    except (ValueError, OSError) as error:
        parser.exit(1, f"Install failed: {error}\n")
    print(f"Skill: {link}\nWorkflow hook: {instructions}\nStart a new chat to load the instruction hook.")


if __name__ == "__main__":
    main()
