---
name: github-issue-export
description: Export an HTML issue walkthrough into GitHub-ready Markdown with rendered annotated screenshots. Use when sharing a visual report as a GitHub issue or comment. Publish only when requested.
---

# GitHub Issue Export

Turn an existing walkthrough into `issue.md` and an `images/` folder. Keep the editable HTML, CSS, SVG overlays and original screenshots intact. This skill works with any repository and does not require the other walkthrough skills.

## Render automatically

Use [scripts/render_images.py](scripts/render_images.py) with trusted local reports when local browser rendering is permitted. It uses headless Chromium, blocks remote HTTP assets, waits for images and fonts, checks SVG dimensions and saves each `.annotated-shot` and each linked comparison image (`figure > a > img`) as a PNG, in document order. This includes comparisons inside collapsed details. It does not bypass tool access restrictions.

One-time setup in your chosen Python environment:

```sh
python -m pip install -r scripts/requirements.txt
python -m playwright install chromium
```

Run from this skill folder:

```sh
python scripts/render_images.py /path/to/index.html
```

The script renders images and writes their manifest; the agent prepares the Markdown and HTML described below.

Output defaults to `.cache/exports/<unique-run>/images/` plus `manifest.json`. Always write the intended GitHub body as `issue.md` beside that manifest. Keep publishing instructions in a separate `publishing-notes.txt`, not in the issue body. For a single requested example, include only that issue and its images. Include an updated `index.html` preview and its separate `walkthrough.css` in the same folder. Keep its issue explanation, steps, annotated images, comparison, diagnosis and verification text consistent with `issue.md`; link the Markdown from the preview. The complete draft folder contains `index.html`, `walkthrough.css`, `issue.md`, `manifest.json` and `images/`; a folder of images alone is not a finished export. Failed runs retain an incomplete manifest; never publish them as a complete export. Use `--output /path/to/new-folder` for a durable destination, `--width 1440` for viewport width, or `--selector "figure > a > img"` to render existing comparison images. The selected element defines the exported region; default captures omit captions, which the manifest preserves for Markdown.

Store generated preview pages and their relative assets under `.cache/pages/<report-name>/`. These folders are ignored by Git and created as needed. Cache files may contain private screenshots; ignored does not mean encrypted. Keep valuable reports outside the cache or copy completed exports to the user's requested destination. Do not automatically delete existing runs.

## Prepare the export

1. Read the report and its linked assets. Preserve each issue's short explanation before its steps, step order, expected versus actual behavior, evidence dates and verification status. A layout update does not make historical evidence current.
2. Render each screenshot **together with its SVG boxes, arrows and labels** into a PNG using the bundled script when permitted, or an available permitted rendering tool. Capture the figure, not the whole report page. Wait for images and styles to load. Do not export the bare screenshot or use generative image editing to recreate evidence.
3. Check image dimensions with a decoder, regardless of the filename extension. SVG coordinates must match the original image dimensions. Inspect each rendered PNG: annotations must be visible, aligned, legible and unclipped. Keep numbered captions consistent with the image.
4. Write UTF-8 Markdown using [assets/issue.md](assets/issue.md) as a starting point. Put each image immediately below its matching step. Include annotated comparisons after the relevant steps, with a short explanation of what differs. Never substitute the original screenshot for an annotated export. Remove unused sections and replace every template token. Use ordinary headings, lists and optional details blocks; custom CSS, sticky navigation and scripts do not carry over.
5. Save the Markdown beside the script's manifest, or use the user's chosen destination. Use relative image paths for the local draft. Report any missing evidence or rendering limitation; a text-only draft is not a completed visual export. Respect tool access restrictions rather than bypassing a blocked file or browser route.

Keep causes supported by evidence separate from suspected causes. Link proposed fixes to the relevant step and include how to verify them. Do not silently upgrade a proposal into a tested fix.

## Publish when requested

- Use the requested repository and issue or comment destination. Creating a local export does not authorize publishing it. Existing explicit publishing authorization is sufficient.
- Check screenshots for credentials and unrelated private information before upload. If redaction is needed, make a clearly identified export copy and preserve the original locally.
- Upload PNGs through a supported GitHub attachment workflow or another user-authorized accessible location. Local paths do not work for other readers. Do not commit evidence images to a repository merely to host them without authorization.
- Replace local image paths with the returned image URLs, keeping images beside their steps. If the installed GitHub CLI supports attachments, inspect its help first; appended attachments alone may not preserve the walkthrough order.
- Read back the published issue or comment and inspect its rendered images when possible. Check order, captions, access and image loading. Report the URL and any verification limits. Check for an existing post before retrying an ambiguous submission to avoid duplicates.

Exported Markdown and PNGs are snapshots. Later HTML changes require another export and an explicit update to the GitHub post.

## GitHub constraints

PNG preserves the appearance of the screenshot and SVG overlay, but its annotations are no longer editable. Keep SVG sources locally. Split or resize large images without making labels unreadable; GitHub documents a 10 MB image attachment limit. Check current limits and available upload tooling when publishing.

Sources: [GitHub attachments](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/attaching-files), [GitHub CLI issue creation](https://cli.github.com/manual/gh_issue_create), [GitHub HTML sanitization](https://github.com/github/markup).
