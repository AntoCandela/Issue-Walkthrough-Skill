---
name: issue-walkthrough
description: Create a local HTML guide that explains how to reproduce an issue, what went wrong, and how to verify a fix. Use when steps and screenshots help someone follow the work. Skip simple questions that need only a short answer.
---

# Issue walkthrough

Use [assets/walkthrough.html](assets/walkthrough.html) to turn an issue into a guide someone can follow.

Copy both [assets/walkthrough.html](assets/walkthrough.html) and [assets/walkthrough.css](assets/walkthrough.css) into the output folder. Keep the relative stylesheet link intact, including when renaming the HTML to `index.html`. Edit structure in HTML and presentation in CSS.

## Build the guide

1. Identify the starting screen, the intended result and the actions to test. Creating a guide does not authorize code fixes or account changes.
2. Try the steps. Capture real screenshots of the starting point, relevant actions and result. Keep originals unchanged. Exclude credentials and unrelated personal content.
3. Start with the problem, its impact and the verification status. Use **Reproduced**, **Verified**, **Proposed** or **Not verified**. Never present an untested step as a result.
4. Put each action directly above its screenshot. Use the interface's exact labels, a short "Look for" checkpoint and a caption explaining what happened. Link the original image. For backend or CLI issues, use real requests or terminal output where more useful.
5. Finish with what should change, the next action and how to check success. Use "Working result" only after verifying a fix. State any checks still missing.
6. Put causes, code links, logs and version details in the expandable **Technical details** section. Label hypotheses and distinguish inspected code from the running version. Keep essential steps and results outside this section.

Before each issue's steps, add a short plain-language paragraph explaining what is wrong, what the user expects and why the difference matters. Keep it separate from the verification status and technical cause. For multiple issues, repeat this sequence with unique section IDs. Omit navigation and unused blocks for a short guide.

Explain what to do and look for before technical details. Use short sentences and consistent terms. Do not reuse another project's names, paths or evidence.

## Design

Keep the template's plain document layout. Use one neutral font, the shared 8px spacing scale and large screenshots. Let headings and text use the full content width; do not impose character-width limits. Keep 8px between related lines, 16px before screenshots, 24px before step lists and 32px between sections. Put navigation outside the header so it stays sticky across the report. Use a subtle active underline, a horizontally scrollable row on narrow screens, and anchor offsets that clear the navbar. Separate content with space and occasional horizontal rules. Avoid coloured left borders, decorative cards, gradients, badge pills and oversized headings. Use colour for useful annotations and links. Do not add a framework, web fonts or remote assets.

## Save and check

Replace all template tokens. Write UTF-8 HTML and keep its charset declaration. Store `index.html` and screenshots together with relative links so the guide opens offline.

Use the requested folder, or `<workspace>/usability-reports/<issue-slug>-visual/`. Choose a new folder if one already exists. Keep the guide local unless publication is requested.

Open the guide at wide and narrow widths. Check images, links, navigation and readability. If preview is unavailable, say that visual checking is incomplete. Return a link to the local HTML file.

## Screenshot annotations

Capture the relevant states from the running application when access is available. Inspect each capture and add visible SVG boxes, arrows and numbered callouts over the unchanged image. Put this annotated image directly in the step, not inside collapsed details. Link the original separately. Existing screenshots may be used when requested; label historical evidence clearly.

When a comparison helps explain a difference between views, include an annotated comparison after the relevant steps as well as the individual step screenshots. Preserve existing comparisons when updating a report.

Use `$screenshot-annotations` when installed for placement guidance. The walkthrough template also includes an SVG layer so this skill can work alone. Match its viewBox to image dimensions verified by an image decoder, not guessed from the filename, use measured coordinates and unique marker IDs, and match numbers to steps and captions. Never fabricate an annotation target. If access prevents capture or accurate placement, label that step incomplete and explain the missing evidence.
