# UX principles and task patterns

Read before choosing a park or layout. These six ideals and the pattern taxonomy below are our synthesis of [the research](research/ux-foundations.md), not a universal standard or a prescribed component library. Infer the task from the request; ask only when an unresolved choice materially changes the product.

## Six ideals

### 1. Start with the person's next useful outcome

Complete this sentence internally: "When I open this, I need to ___ so I can ___." Choose the primary task pattern below from that outcome. For a working surface, open on useful content and controls. For a narrative surface, open with a clear subject and a reason to continue. A word like "dashboard" does not require charts, metric tiles, a sidebar, or an overview page.

**Check:** Can a new visitor identify what to do or learn, and begin it without navigating through an introductory shell?

### 2. Make attention proportional to consequence

Give the most consequential unresolved work or decision the strongest hierarchy. Group by how the person thinks about the task, not by database entities. Remove summary counts that do not change a decision. A calm "nothing needs attention" state is a successful outcome; do not manufacture urgency or recommendations. Density should support scanning and comparison, with readable text and comfortable controls.

**Check:** Does the first screen make the important difference visible without making every item look urgent?

Apply a deletion test to visible copy: if removing a line does not impair identification, interpretation, a decision, or an action, remove it. Omit decorative eyebrow labels above headings, generic greetings, repeated subtitles, section introductions, and prose that merely says what the adjacent controls already show. Keep genuine category labels, necessary instructions, units, sources, and actionable feedback. The six ideals are internal guidance; never turn them into six visible sections.

### 3. Put meaning beside information

Show the context needed to interpret a value: units, period, comparison, scope, and source or freshness when consequential. Make active filters and their scope apparent. Distinguish unknown, unavailable, zero, stale, and empty. Choose tables for precise lookup/comparison, charts for patterns, and plain text for a simple answer. Never invent totals, targets, trends, confidence scores, or update timestamps to fill a design.

**Check:** Can someone explain what the displayed result means, what it covers, and whether it is reliable enough for the task?

### 4. Reveal depth without losing orientation

Keep frequent and essential information visible; defer supplementary detail behind a clear, predictable action. Expand a row, open a detail panel, or navigate to a dedicated view according to the amount of work involved. Keep filters, selection, and place when returning. Essential comparison values and the main action do not belong behind hover, nested menus, or repeated expansion. Add search or filtering only when the requested workflow and collection size justify them.

**Check:** Can someone inspect a detail and return to the same working context without rebuilding it?

### 5. Close the loop on every action

Use specific verb labels and familiar control behavior. Put actions near what they affect. Make pending, success, and failure perceptible; do not claim "saved" before the actual save succeeds. Preserve entered work when an operation fails, explain the recovery step, and support cancel or undo where appropriate. Interrupt only for consequences that justify it. Loading, first use, no matches, partial failure, and completion have different meanings; implement the relevant states rather than one generic empty message.

**Check:** After acting, can someone tell what changed, whether it persisted, and how to recover if it failed?

### 6. Preserve the task across devices and visits

Design a narrow-screen workflow, not just smaller boxes. Keep necessary labels, comparison context, and actions available when rearranging content. Support keyboard operation, visible focus, accessible status updates, and enlargement/reflow. Preserve progress or view state when the requested workflow requires continuity, using the authorized storage boundary. Do not add accounts, cross-device sync, or analytics merely to satisfy this ideal. Be accurate about whether data is temporary, browser-local, or shared when it affects expectations.

**Check:** Can someone complete the core task on a narrow screen and with a keyboard, and resume without surprising loss of work where continuity is expected?

## Choose a primary task pattern

These are starting models, not mandatory routes or layouts. Combine one primary pattern with a secondary pattern only when the brief needs it. Park selection follows this choice; a landscape must not choose the user's workflow.

Do not implement every model as a sidebar, eyebrow, title, subtitle, KPI row, then card grid. Pick groupings and proportions from the content and its relationships. A useful table, plain list, split view, or single focused tool can be the whole main surface. Express character through type, alignment, rhythm, and restrained geometry rather than more headings or explanatory copy.

| Pattern | Person's question | Useful structure | Common failure |
| --- | --- | --- | --- |
| Monitor and investigate | Is something wrong or changing? | Meaningful overview, exceptions, contextual trend/detail | Vanity metrics or a sea of equal-weight charts |
| Triage and act | What needs my attention next? | Prioritized queue, relevant facts, nearby action, resolved state | Totals dominating while actual work is hidden |
| Explore and compare | Which items matter or fit? | Collection with comparable attributes and a clear path to detail | Decorative cards hiding tradeoffs; filters with unclear scope |
| Plan and progress | What happens when, and what remains? | Schedule for time relationships; ordered steps for dependencies; task list for independent work | Calendar without a time-based need, or a checklist hiding required order |
| Create and adjust | What happens if I change this? | Inputs/editor near result, understandable feedback, appropriate save behavior | A landing page before the tool or output separated from its inputs |
| Read and understand | What is the story, and why does it matter? | Coherent reading order, evidence, useful navigation, relevant next step | Turning an explanation into arbitrary metric tiles |

Favor known interaction conventions within any pattern. If a requested conversation is central to the task, use a conversation view with visible results and action status. Being built by ChatGPT does not itself make a chat box useful; do not introduce chat or AI features without a product reason and available capability.

## Applying this without expanding scope

Record the primary pattern, main outcome, key context, and essential action/state loop in the existing design brief. Mark irrelevant concerns as not applicable rather than inventing features. For maintenance, apply these checks to the changed flow and preserve existing behavior elsewhere. Evaluate the actual task in the rendered product; these principles are design hypotheses until tested with representative users.
