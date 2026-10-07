---
name: issue-walkthrough
description: Create a local visual HTML walkthrough for reproducing, understanding, troubleshooting, or managing an issue. Use when step-by-step guidance with screenshots, expected versus actual behavior, causes, and proposed fixes would help the user follow the work. Also use when the user asks for the previous issue walkthrough style. Skip simple answers that do not benefit from an artifact.
---

# Issue walkthrough

Create an easy-to-follow local HTML guide using [assets/walkthrough.html](assets/walkthrough.html). The default template uses pale background, navy headings, rounded white sections, numbered steps, navigation pills, green expected/evidence panels, and red observed-problem panels.

## Workflow

1. Identify the issue, intended outcome, starting screen, and what the user must do. Reuse the current application and task context. A walkthrough request does not authorize fixing code or changing account/data settings.
2. Reproduce the relevant interactions when access permits. Capture only meaningful states: where to start/click, visible evidence, and the resulting problem. If a step cannot be performed, label it **Not verified** or **Proposed**; do not present expected behavior as an observation.
3. Save in the user's requested directory. Otherwise use `<workspace>/usability-reports/<issue-slug>-visual/`, choosing a new name if a guide already exists. Write HTML as UTF-8 and retain its `<meta charset="utf-8">`. Keep `index.html` and its screenshot assets together with relative links so it opens offline with `file://`. No hosted deployment or external upload is needed.
4. Copy and adapt the bundled HTML. Replace all template tokens; duplicate sections only when needed. Each section should contain:
   - A specific action title and status: Reproduced, Verified, Proposed, or Not verified.
   - Short ordered steps using the interface's exact visible labels, plus the checkpoint that tells the user whether the step worked.
   - Expected and actual behavior for a defect; action and verification for a proposed remedy.
   - A relevant screenshot, numbered callouts, and a short caption. Keep originals available through expandable details and direct links.
   - **Cause:** observed evidence and the explanation it supports. Explicitly label a hypothesis or unverified inference. Link to the exact source file, API diagnosis, log excerpt, or issue comment where useful; distinguish the inspected source revision from the running version.
   - **Possible solution:** a concrete next change, its scope/owner, and how to verify it. Do not claim it is implemented. Include a stop/rollback condition only when the action warrants one.
5. End with the next action and unresolved questions. Link related issue/diagnosis documents. Cover only verified cases, and state any important coverage gaps.
6. Open the HTML for the user and check it visually. Verify images load, navigation anchors work, callouts point to the right elements, links resolve, and steps remain readable at narrow widths. Return a short local file link. A ZIP is optional when portability would help.

## Screenshots and annotations

Read [references/annotations.md](references/annotations.md) when capturing images or placing SVG callouts.

- Preserve captured originals. Do not turn generated UI into evidence, invent missing controls, or hide text essential to reproduction.
- Prefer an HTML/SVG annotation layer over the unmodified image for the local guide: use an SVG `viewBox` matching the screenshot's pixel dimensions and scale both together. Place explanations outside the image and connect them with numbered boxes/arrows. The template includes a commented example. This is page composition, not repainting screenshot pixels.
- If actual raster image editing is requested, follow the available image-editing tool/skill instructions, inspect the output against the original, and label it as an explanatory rendering. Always retain a direct link to the original.
- Match numbers in the instructions, callouts, and captions. Use color plus labels, never color alone. Avoid covering the clicked control or missing-connection area with commentary.
- Do not capture unrelated tabs, credentials, or unrelated personal content. Keep local evidence local unless the user asks to publish it. A failed external attachment must not block delivery of the local guide; do not invent hosted links.

## Keep the guide practical

Use concise plain language. Explain what to click and what to look for before implementation details. Do not carry project names, issue numbers, fixture names, machine paths, screenshots, or diagnoses from a previous guide into a new one. Prefer useful sections over a fixed number of steps. For a one-screen task, a single annotated section is enough.

This skill may be selected automatically when a visual issue walkthrough is useful, or invoked as `$issue-walkthrough`.
