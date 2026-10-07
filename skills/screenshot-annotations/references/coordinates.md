# SVG coordinates

## Match the saved image

Read dimensions with an image decoder or the browser's `naturalWidth` and `naturalHeight`. Detect the file format from its contents, not its extension: a `.png` filename can contain JPEG bytes. Never read fixed PNG header offsets without confirming the PNG signature. Compare each SVG viewBox with the decoded image dimensions before delivery; checking that boxes fit inside the viewBox alone is insufficient.

For an image W pixels wide and H pixels tall, use `viewBox="0 0 W H"`. All box, arrow and number positions use those image pixels.

Keep the template's `.annotated-shot` wrapper. Let the image set its height and scale the SVG with it. Avoid fixed display heights and `object-fit` cropping.

## Convert displayed coordinates

If you measured a screenshot displayed at width D, multiply the coordinates and box dimensions by W/D. Measure from the image's top-left corner, excluding page margins.

Example: a 1600-pixel image displayed at 800 pixels has a scale of 2. A box at (100, 50), sized 200 by 80, becomes (200, 100), sized 400 by 160.

For DOM measurements, account for the screenshot origin, scroll position and device pixel ratio. CSS pixels do not always equal saved-image pixels.

## Handle crops

Prefer the full screenshot. If a crop helps, label it and keep a separate link to the original.

Subtract the crop's top-left coordinates from each original annotation position. Then apply any resize scale to positions and dimensions. Set the viewBox to the resulting cropped image dimensions. Leave out callouts whose targets fall outside the crop.

## Avoid marker collisions

Use a unique marker ID per figure, such as `arrow-step-2-shot-1`. Use that exact ID in `marker-end="url(#arrow-step-2-shot-1)"`. Duplicate IDs can make arrows use the wrong marker.
