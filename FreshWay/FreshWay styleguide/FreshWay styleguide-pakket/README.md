# FreshWay style guide for AI agents

This package is a style guide for FreshWay, the case company in Smart Logistics. You give it to an AI coding agent (Claude Code, Cursor, ChatGPT, Copilot or similar) so that the dashboards and 3D visuals it builds for you look like one company, and look good.

A good style guide is the difference between "make me a chart" and a visual you can put in front of a board. The agent gets exact colours, sizes and rules instead of guessing.

## What is in the package

| File | What it is |
|---|---|
| `DESIGN.md` | The style guide for your agent: colours, type, layout, 3D material, light, camera and motion. Written in the open DESIGN.md format, so agents can read it directly. |
| `FreshWay style guide.pdf` | The same style as a visual overview, for you to read. |
| `assets/logo/` | The FreshWay logo, a cropped version for page headers, and a favicon. |
| `assets/examples/` | Stills of finished examples in this style: a 3D network map and a bar chart, in light and dark. |

## How to give it to your agent

1. Copy the whole folder into your project, for example as `styleguide/`.
2. In your prompt, point to it: "Follow `styleguide/DESIGN.md`." Most agents read the file when you name it. In ChatGPT or another chat tool without file access, upload `DESIGN.md` or paste its contents into the chat.
3. Tell the agent which one insight the visual should show, and give it the numbers with their unit and source. The style guide says how it should look; you decide what it says.
4. Check the result against the Do's and Don'ts at the end of `DESIGN.md`, and ask the agent to fix what does not match.

## Three example prompts

> Follow `styleguide/DESIGN.md`. Build a single web page with Three.js that shows the floor area of FreshWay's three distribution centres as 3D bars in light mode. Source: FreshWay company dossier, A2. Use the logo from `styleguide/assets/logo/`. Include the flat-chart version.

> Follow `styleguide/DESIGN.md`. Our advice to the board is [your insight in one sentence]. Make one full-screen slide in the dark presentation mode that shows this with [your numbers, unit, source and confidence label]. One insight, key figure large, nothing else.

> Here is my dashboard page. Review it against `styleguide/DESIGN.md` and list every place where it breaks the style: colours, type sizes, button sizes, labels, the second signal next to colour. Then fix them one by one.

## Say how you made it

If you use GenAI for your work, say so. Put a short transparency statement at the bottom of your product: what you made with or together with GenAI, and which Human-AI Agency label fits how you worked (for example Co-Creator, Creative Director or AI Refiner). The labels come from Boetje & Baake (2026), *Nine prototypical human-AI agency patterns*, https://doi.org/10.6084/m9.figshare.31706884. The style guide has a place for this: the "Made with GenAI" chip and the making-of chapter.

---

> **Transparency GenAI.** This style guide, its examples and this README were made together with GenAI, based on the requirements and feedback of the teacher, who directed the work and checked the result. Human-AI Agency Label: **Co-Creator**.
> Labels: Boetje, J., & Baake, G. (2026). *Nine prototypical human-AI agency patterns* [Figure]. figshare. https://doi.org/10.6084/m9.figshare.31706884 (CC BY 4.0).
