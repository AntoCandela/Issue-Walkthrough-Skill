---
name: screenshot-annotations
description: Add SVG boxes, arrows and numbered callouts over real screenshots in a local HTML file. Use for tutorials, reviews or visual issue explanations. Does not generate UI screenshots or repaint image pixels.
---

# Screenshot annotations

Use [assets/annotated-screenshot.html](assets/annotated-screenshot.html) for a standalone explanation, or embed its figure and scoped styles into a report.

Copy both [assets/annotated-screenshot.html](assets/annotated-screenshot.html) and [assets/annotated-screenshot.css](assets/annotated-screenshot.css) into the output folder. Keep the relative stylesheet link intact, including when renaming the HTML to `index.html`. Edit structure in HTML and presentation in CSS.
When embedding a figure into another report, copy only the `.annotated-*` rules into that report's stylesheet; do not import the standalone body and main styles.

## Annotate the screenshot

1. Use a supplied screenshot or capture one with an available tool. Save the original image bytes with the matching PNG or JPEG extension. Do not invent missing UI or evidence. If capture is blocked, explain what is missing.
2. Keep the original unchanged. Read the saved image's dimensions with an image decoder; do not infer its format from the filename. The dimensions may differ from the browser viewport.
3. Replace the template tokens with measured coordinates and escaped text. Set the SVG `viewBox` to the image dimensions. Read [references/coordinates.md](references/coordinates.md) when positioning callouts, especially for scaled or cropped images.
4. Mark the relevant controls with visible SVG boxes, arrows and numbers. In a report, show the annotated screenshot in the main step, never only inside collapsed details. Keep explanations in captions outside the image. Match numbers to surrounding steps, and do not cover the control or error.
5. Give each SVG marker a unique ID. Add image alt text and explain each callout in the caption. Use labels as well as color; hide decorative SVG from screen readers.

Keep evidence local unless publication is requested. Exclude credentials and unrelated personal content. For requested raster edits, use an available image-editing tool, retain the original and label the edited result as an explanatory rendering.

## Save and check

Write UTF-8 HTML. Keep images beside it with relative links and a direct link to each original. Use the requested folder, or `<workspace>/usability-reports/<topic>-annotations/`. Choose a new folder if one already exists.

Open the result at wide and narrow widths. Check image loading, box alignment, arrow tips, readable numbers and original-image links. Check punctuation for broken characters. If preview is unavailable, report that visual checking is incomplete.

Return a link to the HTML file. This skill does not require a full issue walkthrough.
