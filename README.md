# Issue Walkthrough Skills

Turn a software issue into a local HTML guide with real screenshots, numbered callouts, expected versus actual behavior, and clear verification steps.

Local working repository. Not published yet.

## Available skills

| Skill | What it does |
| --- | --- |
| [issue-walkthrough](skills/issue-walkthrough/SKILL.md) | Plans and writes the report: steps, evidence, causes, fixes and verification. |
| [screenshot-annotations](skills/screenshot-annotations/SKILL.md) | Adds SVG boxes, arrows and numbered callouts to real screenshots, independently or inside a report. |
| [github-issue-export](skills/github-issue-export/SKILL.md) | Exports a report to Markdown and annotated PNGs for a GitHub issue or comment. |

Works with different repositories and applications. Browser screenshots need a capture-capable agent environment. Backend and CLI walkthroughs can use real request examples and terminal output instead. The skill does not include a browser automation runtime.

## Layout

```text
skills/
  issue-walkthrough/
    SKILL.md                  Workflow instructions
    agents/openai.yaml        Optional Codex metadata
    assets/walkthrough.html   Report structure
    assets/walkthrough.css    Report styles
  screenshot-annotations/
    SKILL.md                  Screenshot and SVG instructions
    agents/openai.yaml        Optional Codex metadata
    assets/annotated-screenshot.html  Screenshot and SVG structure
    assets/annotated-screenshot.css   Annotation styles
    references/coordinates.md SVG sizing and coordinate examples
  github-issue-export/
    SKILL.md                  Export and publishing instructions
    agents/openai.yaml        Optional Codex metadata
    assets/issue.md           GitHub Markdown structure
    scripts/render_images.py  Render annotated figures to PNG
    scripts/requirements.txt  Python rendering dependency
    .cache/                   Ignored previews and export runs
```

## Report structure

The guide opens with the problem and its status. Each action sits directly above its screenshot with visible SVG boxes, arrows and numbered callouts, plus a short checkpoint and caption. A final section explains the proposed change or verified result. Causes, logs and code links sit in expandable technical details.

The design uses full-width text, plain typography, a consistent 8px spacing scale, sticky navigation and full-width annotated screenshots. No decorative cards, coloured left borders, gradients or font downloads.

## Edit the HTML

Start with [walkthrough.html](skills/issue-walkthrough/assets/walkthrough.html). Its styles live in [walkthrough.css](skills/issue-walkthrough/assets/walkthrough.css). Edit [annotated-screenshot.html](skills/screenshot-annotations/assets/annotated-screenshot.html) for SVG callouts and [annotated-screenshot.css](skills/screenshot-annotations/assets/annotated-screenshot.css) for presentation. Copy the matching HTML and CSS together when creating a guide. Keep the template tokens (`{{TITLE}}`, etc.) for the agent to replace in each guide. Opening the template directly shows those tokens; it is not a completed report.

Edit this repository's template to change the appearance of future walkthroughs. Installed copies of the skill are separate and do not update automatically.

## Try it locally

Copy the desired complete skill folders from `skills/` into your agent's supported skill directory. For Codex this is usually `~/.codex/skills/issue-walkthrough`. If already installed, review the differences before replacing that copy.

Install the first two to combine reports and SVG annotations. The walkthrough skill includes a basic SVG layer and works alone; the annotation skill works alone without creating a full issue report.

Example request:

> Use $issue-walkthrough to reproduce this issue and create a local HTML guide with screenshots, numbered callouts, likely causes and verification steps. Clearly label anything you could not test.

> Use $screenshot-annotations to highlight the confusing controls in this screenshot with numbered SVG callouts.

> Use $github-issue-export to export this HTML walkthrough as a local Markdown draft with rendered annotated PNGs. Do not publish yet.

The export skill guides the agent through rendering and publishing; it includes a Playwright rendering script; install its Python dependency and Chromium before use. GitHub credentials are not included. GitHub gets a static snapshot, while the local HTML and SVG remain editable.

Generated guides default to `usability-reports/<issue-slug>-visual/` in the target workspace. No build step is required to open a guide.

## Before publishing

Choose a GitHub repository name, review the template, and add only public demonstration material if desired. No private application screenshots, local reports or account details are included here. There is no remote configured yet.

## Structure inspiration

The [mattpocock/skills repository](https://github.com/mattpocock/skills) uses a root README and discoverable skill folders under `skills/`. This repository follows that small, editable packaging approach, without copying its skill content or adding its release/plugin infrastructure.

## License

[MIT](LICENSE). You can use, modify and redistribute the skill and template, including commercially, subject to the license terms. Screenshots and other material added to generated guides retain their own rights and permissions.
