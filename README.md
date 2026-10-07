# Sites Creative Direction

A companion skill for ChatGPT Sites that automatically translates a national park into a distinctive visual direction. Describe the site you need; the builder chooses the park and composition internally and delivers one considered design.

The starter library includes Joshua Tree, Olympic, Bryce Canyon, Acadia, Yellowstone, White Sands, Glacier, and Hawaiʻi Volcanoes. Each profile includes palette seeds, spatial principles, typography, a signature detail, mobile adaptation, and clichés to avoid. These are original creative interpretations, not official park identities.

## Workflow

Understand the task → choose a park → explore three short structural concepts → select one → save a design brief → build through Sites → inspect the rendered result.

Only the selected concept is implemented. The workflow adds no user questionnaire, unsolicited product features, or publishing permission. Explicit brand references take precedence; ordinary maintenance preserves the existing design. The skill works alongside the installed Sites building/hosting skills, not as a replacement.

## Install

Requires Python 3.10+ and an existing local checkout. No third-party Python packages are needed for the installer or its tests.

Enable for a Sites workspace:

```sh
python3 scripts/install.py --workspace /path/to/sites-workspace
```

Or enable for all local Codex Sites work:

```sh
python3 scripts/install.py --user
```

The installer symlinks this checkout's skill into `.agents/skills` and adds a clearly delimited, Sites-only instruction block to the workspace `AGENTS.md` or user Codex home's `AGENTS.md`. Existing instructions are preserved; rerunning updates only the managed block. Conflicting skill installations, malformed blocks, symlinked instruction files, and shadowing `AGENTS.override.md` files cause it to stop. Keep the checkout in place. To remove, delete the `sites-park-design` symlink and its delimited instruction block only.

Start a new chat after installation. Automatic discovery alone is a routing hint; the instruction hook explicitly requests the skill for applicable Sites work. This changes the local Codex workflow where installed, not the hosted ChatGPT Sites product or other people's defaults. See [official skill discovery documentation](https://learn.chatgpt.com/docs/build-skills) and [instruction loading documentation](https://learn.chatgpt.com/docs/agent-configuration/agents-md).

## Develop and evaluate

```sh
python3 -m unittest discover -s tests -v
```

Run the bundled Codex skill-creator `quick_validate.py` against `skills/sites-park-design` if available (it requires PyYAML). Structural validation does not establish design quality.

Use [the evaluation briefs](evals/briefs.md) for real Site builds and compare screenshots, first-viewport usability, and structural variety. No rendered Site evaluation is included yet. Park profiles are guidance, not templates or a guarantee of globally unique designs.

To add a park, add a profile under `skills/sites-park-design/references/parks/` and link it from the index. Favor distinct composition and interaction principles over another palette swap. Do not copy NPS logos, illustrations, or branding into the package.
