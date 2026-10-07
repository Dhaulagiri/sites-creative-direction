# Sites Creative Direction

A Codex skill for distinctive, useful ChatGPT Sites. It chooses a UX pattern and national park as design inspiration, with minimal copy and no decorative eyebrows, repeated subtitles, or generic dashboard template.

## Install

Requires Node.js/npm and Git. The repository is public; no GitHub account is needed.

```sh
npx skills add Dhaulagiri/sites-creative-direction \
  --skill sites-park-design --agent codex --global
```

Omit `--global` to install only in the current project. Installation uses the [Skills CLI](https://github.com/vercel-labs/skills), so no Python or manual clone is required.

## Use

Start a new Codex chat and ask:

> Use $sites-park-design to build a Site for planning our family's weekly meals.

For an existing Site, open it in Codex or provide its URL and ask:

> Apply $sites-park-design to this existing Site. Refresh the design and simplify the copy while preserving its content, data, and functionality.

You can also apply just one part:

> Use $sites-park-design to replace this Site's favicon with one matching its current park-inspired design.

To use it automatically for Sites work, add this to your existing `~/.codex/AGENTS.md`, preserving any other instructions:

```markdown
For new ChatGPT Sites and requested Site redesigns, use $sites-park-design
alongside Sites building. Choose the UX pattern, park, and concept internally.
Honor explicit branding and preserve existing designs during ordinary maintenance.
Do not apply this to unrelated web projects.
```

For a project-only default, add the same text to that project's `AGENTS.md` instead. The installer makes the skill available; this instruction makes it part of your default workflow. Sites building/hosting must also be available in Codex.

## What it does

- Chooses a task model: monitor, triage, compare, plan, create, or read.
- Selects from eight park profiles covering palette, composition, typography, and restrained details.
- Applies to new Sites and requested refreshes of existing Sites.
- Creates a matching favicon for new Sites and replaces missing or starter icons during a refresh, preserving supplied brand icons and valid custom icons unless replacement is requested.
- Explores three short concepts internally, then builds one.
- Checks the actual task, responsive behavior, and unnecessary copy.

Explicit branding takes precedence. Park profiles are creative interpretations, not official identities.

[UX principles](skills/sites-park-design/references/ux-principles.md) · [Park profiles](skills/sites-park-design/references/parks/index.md) · [Research](skills/sites-park-design/references/research/ux-foundations.md)

## Update

```sh
npx skills update sites-park-design --global
```

Omit `--global` for a project installation.

## Development

```sh
python3 -m unittest discover -s tests -v
```

Python is only needed for the optional local installer and its tests. Use [the evaluation briefs](evals/briefs.md) to compare rendered Sites; design quality has not yet been validated through those evaluations.
