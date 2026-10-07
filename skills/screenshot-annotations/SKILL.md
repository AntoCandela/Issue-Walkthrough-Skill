---
name: screenshot-annotations
description: Annotate real screenshots with SVG boxes, arrows and numbered callouts in a local HTML file. Use for visual explanations, tutorials, reviews or issue evidence, with or without a full walkthrough. Does not generate replacement UI screenshots or edit screenshot pixels.
---

# Screenshot annotations

Create an annotated screenshot using [assets/annotated-screenshot.html](assets/annotated-screenshot.html). Use this skill independently for a visual explanation, or embed its figure and scoped styles into an existing report. It does not require the issue-walkthrough skill.

Replace every template token with observed image dimensions, element coordinates and escaped text. The template is a starting point, not evidence. For a standalone output, save the adapted HTML and screenshot together in the requested directory, or `<workspace>/usability-reports/<topic>-annotations/`. Choose a new directory if one already exists.

## Capture and save

Use the browser or screenshot tool available in the current environment. Save the returned image bytes directly as PNG or JPEG using the matching extension. Do not recreate the application as an image and call it a screenshot. If capture is unavailable, label the step Not verified and explain what evidence is missing.

Keep the captured original unchanged. Use ordered filenames such as `01-start.png`, `02-result.png`. Store them beside the HTML, with relative image links. Record the actual saved image dimensions, which may differ from the browser viewport dimensions.

## Place callouts

Use the template's `.annotated-shot` wrapper and SVG overlay. For a saved image of width W and height H, set `viewBox="0 0 W H"`. Position boxes, arrows and numbered markers in that image's coordinate system. Let the image determine wrapper height; scale the SVG with the image, without fixed display heights or object-fit cropping.

If an element was measured in a displayed image of width D, convert its displayed coordinates to saved-image pixels using scale W/D. Apply the same scale to its x, y, width and height. When using viewport DOM bounds, first account for screenshot origin, scrolling and device pixel ratio; do not assume CSS pixels equal image pixels.

Prefer the full original image. If a crop helps, retain and link the original separately, label the crop, and subtract the crop origin from each annotation coordinate before applying any resize scale. Use the cropped image dimensions for its viewBox.

Give SVG markers unique IDs per figure, such as `arrow-step-2-shot-1`, and reference that exact ID in `marker-end`. Duplicate IDs across a page can attach arrows to the wrong marker.

Keep explanations in captions outside the screenshot. Match numbers between the instructions, markers and captions. Do not cover the relevant control or error. Keep the SVG aria-hidden when the caption supplies the equivalent explanation, and give the image useful alt text.

## Check the result

Open the completed HTML at a wide and narrow width. Check that images load, boxes stay aligned, arrow tips hit their targets, numbers remain readable, and original-image links work. Keep UTF-8 encoding through every file read and write; inspect arrows and punctuation for broken characters. Do not claim visual verification if no browser preview was available.

Match callout numbers with surrounding instructions when embedding into a walkthrough. Use labels as well as color. Keep evidence local unless publishing is requested; avoid capturing unrelated personal content or credentials. If raster editing is requested, use the available image-editing tools, label the result as an explanatory rendering, and retain the original.

Invoke as `$screenshot-annotations`, or select it when an annotated screenshot would help explain a task.
