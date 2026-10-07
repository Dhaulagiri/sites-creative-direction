# Rendered design review

Inspect the real implementation, not just its written rationale. Use the main desktop view, a narrow view around 390px, and relevant focus/empty/error states. Reuse the normal Sites QA rather than duplicating it.

## Gates

- Can someone begin the primary task immediately, with required controls and useful content visible?
- Are type, contrast, keyboard focus, and responsive behavior usable? Measure text contrast: 4.5:1 for normal text, 3:1 for qualifying large text; check relevant non-text control boundaries too. Do not approve colors from swatches alone.
- Does the design preserve the requested functionality, information, brand, and scope?
- Is the chosen interaction model appropriate to the actual task, with meaningful value/context and feedback where relevant?
- Does every visible line help identify, interpret, decide, or act? Remove decorative eyebrows, generic welcome copy, repeated subtitles, and descriptions of self-evident controls. Preserve necessary instructions and accessible labels.

Fix failed gates before comparing visual character. Never trade them for novelty.

## Task walkthrough

Perform the main task, not just a screenshot review. For an interactive surface, use a representative input, selection, or edit and verify its result; check relevant failure/recovery and return-from-detail behavior. For a reading surface, follow its main reading/navigation path. Confirm active scope, selection, and work survive transitions as intended. Check the applicable flow with keyboard and at a narrow width; include 320 CSS pixel reflow/enlargement where relevant, while respecting genuine two-dimensional content exceptions. Record what was actually checked and what remains unverified. Do not add product features solely to make a checklist item applicable.

## Character

- **Structure:** Can you identify a specific composition or grouping decision beyond the palette? If replacing the colors makes this indistinguishable from a generic hero and card grid, revisit the structure where the task permits.
- **Specificity:** Can you name two distinct choices traceable to the selected profile? Include one beyond color, such as spacing rhythm, typography hierarchy, edges, or alignment.
- **Favicon:** For a new Site, an existing-Site refresh with a missing/starter icon, or requested icon replacement, does the referenced favicon load and read clearly at 16 and 32 pixels, using the chosen palette and a simple motif? Confirm supplied branding and existing custom icons are preserved where required.
- **Coherence:** Do the same decisions hold through controls, secondary content, and mobile rather than only the opening section?
- **Restraint:** Does the signature detail help hierarchy or orientation? Remove competing ornaments, landscape clichés, filler headings, and gratuitous motion.
- **Variety:** If prior accessible briefs exist, compare structure as well as park names. Different parks should not all converge on the same cream/serif/rounded-card treatment.

Record observations and remaining limitations in the brief. This checklist cannot prove aesthetic quality. Real rendered comparisons across multiple products are the next evidence for improving the skill.
