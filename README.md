# Issue Walkthrough Skills

Turn a software issue into a local HTML guide with real screenshots, numbered callouts, expected versus actual behavior, and clear verification steps.

Local working repository. Not published yet.

## Available skill

| Skill | What it does |
| --- | --- |
| [issue-walkthrough](skills/issue-walkthrough/SKILL.md) | Explains how to reproduce, understand and verify an issue through a visual walkthrough. |

Works with different repositories and applications. Browser screenshots need a capture-capable agent environment. Backend and CLI walkthroughs can use real request examples and terminal output instead. The skill does not include a browser automation runtime.

## Layout

```text
skills/
  issue-walkthrough/
    SKILL.md                  Workflow instructions
    agents/openai.yaml        Optional Codex metadata
    assets/walkthrough.html   Editable HTML and CSS template
    references/annotations.md Screenshot and SVG guidance
```

## Edit the HTML

Start with [walkthrough.html](skills/issue-walkthrough/assets/walkthrough.html). Its CSS is in the style element, followed by the page structure and a commented SVG annotation example. Keep the template tokens (`{{TITLE}}`, etc.) for the agent to replace in each guide. Opening the template directly shows those tokens; it is not a completed report.

Edit this repository's template to change the appearance of future walkthroughs. Installed copies of the skill are separate and do not update automatically.

## Try it locally

Copy the complete `skills/issue-walkthrough` folder into your agent's supported skill directory. For Codex this is usually `~/.codex/skills/issue-walkthrough`. If already installed, review the differences before replacing that copy.

Example request:

> Use $issue-walkthrough to reproduce this issue and create a local HTML guide with screenshots, numbered callouts, likely causes and verification steps. Clearly label anything you could not test.

Generated guides default to `usability-reports/<issue-slug>-visual/` in the target workspace. No build step is required to open a guide.

## Before publishing

Choose a GitHub repository name, review the template, and add only public demonstration material if desired. No private application screenshots, local reports or account details are included here. There is no remote configured yet.

## Structure inspiration

The [mattpocock/skills repository](https://github.com/mattpocock/skills) uses a root README and discoverable skill folders under `skills/`. This repository follows that small, editable packaging approach, without copying its skill content or adding its release/plugin infrastructure.

## License

[MIT](LICENSE). You can use, modify and redistribute the skill and template, including commercially, subject to the license terms. Screenshots and other material added to generated guides retain their own rights and permissions.
