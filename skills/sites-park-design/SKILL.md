---
name: sites-park-design
description: Give new ChatGPT Sites and requested redesigns task-focused UX, minimal useful copy, and a distinctive park-inspired design. Use alongside Sites building; preserve existing designs during maintenance and honor explicit brand references.
---

# Park-inspired Sites design

Choose a useful interaction model, then use a national park as an internal art direction seed. The user describes the product; choose the direction without requiring a park, mood board, or concept selection. Follow the Sites building and hosting skills for the actual Site lifecycle. This skill adds design guidance, not deployment authorization or a new implementation stack.

## Layer over frontend-design

Read the installed `frontend-design` skill by Anthropic when available, then apply this companion's task model, park profile, and constraints to its design plan. Use frontend-design for general typography, composition, aesthetic judgment, and visual self-critique; do not duplicate or fork its instructions here. Skills do not automatically load one another: explicitly read its `SKILL.md` through the available skill catalog or installed skill directory before planning.

Within the combined guidance, honor explicit user requirements first. Keep Sites building/hosting in charge of project setup, assets, previews, publication, and access boundaries. Use this companion's more specific Sites design constraints when general frontend-design advice differs:

- A working dashboard opens on useful controls and content. Treat the opening composition as the main experience; do not add a marketing hero before it.
- Select the park and concept internally from a sufficiently clear brief. Ask only about material product ambiguity, not approval of routine art direction.
- Use real supplied content and data. Do not invent facts, metrics, or features to complete a composition.
- Apply the copy deletion test below even if a general design treatment invites extra labels or explanatory text.
- Treat park palettes as intentional inputs, while checking readability and avoiding generic composition. An upstream warning about common palettes is not a blanket prohibition on a suitable park profile.

Use one combined plan, saved brief, implementation, and review pass. If frontend-design is unavailable, mention the missing recommended foundation once and continue using this companion and Sites guidance; do not install or fetch dependencies silently during a Site build.

## Scope

- Apply to new Sites and explicit redesigns. For ordinary edits, extend the existing direction and apply UX checks only to the changed flow.
- User-supplied branding, accessibility needs, references, and requested layout take precedence. If these leave no useful room for park inspiration, skip it.
- Keep the product's purpose, content, and capabilities intact. A park is inspiration, not a reason to add outdoor content, a hero, a map, animation, or features.

## Apply to an existing Site

An explicit request to apply this skill to an existing Site authorizes a design refresh; the user need not separately say "redesign." Open the identified Site through the normal Sites workflow and inspect its current screens, capabilities, and any saved design brief before choosing changes. Improve its UX, composition, copy, and visual treatment within the requested scope while preserving content, user data, working features, routes, integrations, and access settings. Reuse the existing project and stack. For a limited request, such as a favicon update, apply only that part of the guidance.

Reuse a suitable existing park direction unless the user asks for a fresh one or the requested refresh needs a different direction. Create or update the saved brief and verify the existing core flows after changes. Ordinary maintenance without a design request still preserves the design.

## Choose and translate

Before selecting a park, read [UX principles and task patterns](references/ux-principles.md). Choose the primary outcome and interaction model. The patterns are decision aids, not page templates or a requirement to add features. Function determines structure; the park gives that structure character. Research provenance is linked from that reference and need not be loaded for every build.

1. Read [the park index](references/parks/index.md). Use the chosen task model, required first-viewport content, density, and tone to shortlist three parks with different spatial characters; choose the best fit. When fits are comparable, favor a park not used in recent accessible Site briefs. Do not scan unrelated projects for history; do not claim global uniqueness.
2. Read the selected park's profile. Develop three short internal concepts informed by it, varying at least two of composition, information grouping, navigation, density, or typography hierarchy. Each must support the same requested task. Different colors on the same grid are not different concepts.
3. Select one concept. Usability is a gate; subject fit, coherence, and originality distinguish the passing choices. Keep this to short internal notes; build only the winner unless the user asks to compare.
4. Save a concise `design/park-direction.md` in the Site source using [the brief format](references/design-brief.md) before the first product-source edit. Use the chosen profile's palette as a starting point, with explicit semantic roles and tested foreground/background pairs. Describe the composition, typography, spacing, geometry, and one signature detail. Include a concrete reason the direction serves this product.

Continue project setup while making these decisions. Do not turn this into an approval gate or expose intermediate concepts in the product UI. This is bounded internal exploration before the single visual thesis required by Sites, not a request for user-facing design options.

## Build and inspect

Use the least visible copy that makes the experience clear. Omit decorative eyebrow labels, generic welcome messages, slogans, and subtitles that repeat a heading. Do not narrate the interface ("Manage your X in one place") or add descriptions to every panel. Keep labels, instructions, context, and feedback that people actually need to identify, interpret, decide, or act. Never add copy merely to fill a layout.

Apply frontend-design’s general craft guidance through the selected park profile across views and states. Use park-specific structural principles rather than generic park-poster styling; do not give every park the same cream/serif/rounded-card treatment. Keep flourishes restrained on working surfaces.

Profiles are original creative interpretations, not official park branding. Do not use NPS marks or imply affiliation. Follow Sites' asset guidance; geometric accents are fine, representational artwork needs an appropriate asset workflow. Do not add landscapes to unrelated products just to make the inspiration obvious.

Give every new Site a custom favicon. When applying this skill to an existing Site, replace a missing or starter favicon as part of the refresh; replace a valid custom favicon only when requested. Use the selected park’s palette and one simple recognizable motif that works at 16 and 32 pixels. Reuse a suitable supplied brand mark; preserve user-provided icons and valid existing custom favicons unless replacement is requested. Follow Sites’ favicon implementation guidance to replace the starter asset and wire the icon into framework metadata or the HTML head. Verify the actual referenced icon loads and remains legible at both sizes. Do not use NPS marks, detailed scenery, or text too small to read.

After a meaningful implementation, read [the review rubric](references/review.md) and inspect the rendered result at desktop and narrow widths using available browser tools. Repair concrete problems in one focused pass and recheck affected views. If rendering is unavailable, record that limitation rather than claiming visual validation. Functional and accessibility checks still follow the underlying Sites workflow.

Retain `design/park-direction.md` for later edits. Keep it out of visible copy. The handoff can name the selected park in one sentence when useful; lead with the working product.
