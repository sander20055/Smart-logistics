---
version: alpha
name: FreshWay Data
description: >
  Dashboard and 3D data-visualisation style for FreshWay, the fictional
  supermarket chain in the Smart Logistics case. Keynote style: soft rounded
  shapes with a subtle gradient, soft shadows, lots of space, large type and
  one insight per view. Light by default, dark as presentation mode.
colors:
  primary: "#00702E"          # FreshWay green, from the logo
  on-primary: "#FFFFFF"
  focus: "#E8321E"            # apple red, from the logo: the one insight per view
  focus-text: "#C42B1A"       # apple red for text, 5.4:1 on paper
  paper: "#FBF9F5"            # background of the logo
  surface: "#FFFFFF"
  stage: "#F4F3EF"            # light stage, middle of the gradient
  stage-glow: "#FFFFFF"       # light stage, highlight
  stage-edge: "#DFE1DC"       # light stage, edge
  stage-dark: "#101B18"       # dark stage, middle
  stage-dark-glow: "#22342F"  # dark stage, highlight
  stage-dark-edge: "#060B0A"  # dark stage, edge
  on-dark: "#F2F4F3"          # text on dark
  on-dark-muted: "#A9B8B4"    # labels on dark
  focus-on-dark: "#FF6A55"    # apple red for text on dark
  ink: "#16302A"              # text on light
  land-light: "#FBF9F5"       # map land, light mode
  land-dark: "#2A3834"        # map land, dark mode: deep green-grey
  ink-muted: "#4F5F5A"
  ink-meta: "#5E6B67"
  hairline: "#D3DAD7"
  data-base: "#86A6A1"        # sage: single series, calm bars
  cat-1: "#1F5C74"            # petrol
  cat-2: "#D79B1E"            # ochre
  cat-3: "#8CBBD9"            # sky
  cat-4: "#A8805F"            # clay
  cat-other: "#C9CFCC"        # other, always last
  cat-2-line: "#8A5F00"       # ochre for thin lines and text
  cat-3-line: "#2F6E9A"       # sky for thin lines and text
  cat-4-line: "#7A5A3E"       # clay for thin lines and text
  seq-1: "#E3EEF2"
  seq-2: "#B5D0DB"
  seq-3: "#7FAFC2"
  seq-4: "#4A89A3"
  seq-5: "#1F5C74"
  seq-6: "#123E50"
  div-neg-2: "#D79B1E"
  div-neg-1: "#EBCB86"
  div-mid: "#EFECE5"
  div-pos-1: "#8FB5C6"
  div-pos-2: "#1F5C74"
typography:
  display-kpi:
    fontFamily: Source Sans 3
    fontSize: 120px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: -0.02em
    fontFeature: '"tnum" 1, "lnum" 1'
  kpi:
    fontFamily: Source Sans 3
    fontSize: 72px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: -0.015em
    fontFeature: '"tnum" 1, "lnum" 1'
  headline:
    fontFamily: Source Sans 3
    fontSize: 40px
    fontWeight: 600
    lineHeight: 1.12
    letterSpacing: -0.01em
  title:
    fontFamily: Source Sans 3
    fontSize: 26px
    fontWeight: 600
    lineHeight: 1.25
  body:
    fontFamily: Source Sans 3
    fontSize: 17px
    fontWeight: 400
    lineHeight: 1.55
  label:
    fontFamily: Source Sans 3
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.01em
    fontFeature: '"tnum" 1'
  eyebrow:
    fontFamily: Source Sans 3
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.08em
rounded:
  none: 0px
  sm: 6px
  md: 10px
  lg: 20px
  full: 9999px
spacing:
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 40px
  2xl: 64px
  3xl: 104px
  stage-padding: 24px
  chapter-gap: 104px
components:
  page:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
  stage:
    backgroundColor: "{colors.stage}"
    rounded: "{rounded.lg}"
    padding: "{spacing.stage-padding}"
  stage-dark:
    backgroundColor: "{colors.stage-dark}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.lg}"
    padding: "{spacing.stage-padding}"
  label-3d-dark:
    textColor: "{colors.on-dark-muted}"
    typography: "{typography.label}"
  label-3d-focus-dark:
    textColor: "{colors.focus-on-dark}"
    typography: "{typography.label}"
  kpi-figure:
    textColor: "{colors.ink}"
    typography: "{typography.kpi}"
  kpi-label:
    textColor: "{colors.ink-muted}"
    typography: "{typography.body}"
  insight-headline:
    textColor: "{colors.ink}"
    typography: "{typography.headline}"
  eyebrow:
    textColor: "{colors.ink-meta}"
    typography: "{typography.eyebrow}"
  label-3d:
    textColor: "{colors.ink}"
    typography: "{typography.label}"
  label-3d-focus:
    textColor: "{colors.focus-text}"
    typography: "{typography.label}"
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label}"
    rounded: "{rounded.md}"
    height: 44px
    padding: 16px
  button-secondary:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.label}"
    rounded: "{rounded.md}"
    height: 44px
    padding: 16px
  genai-chip:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.label}"
    rounded: "{rounded.full}"
    height: 40px
    padding: 16px
  confidence-tag:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink-muted}"
    typography: "{typography.label}"
    rounded: "{rounded.sm}"
    height: 24px
    padding: 6px
  making-of:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.lg}"
    padding: 40px
---
# FreshWay Data

*Style guide for dashboards and 3D data visualisation · Smart Logistics · autumn 2026*

This file is written for an AI coding agent and for you. The YAML block above holds the exact values (tokens). The text below explains why they exist and how to apply them. Give the whole file to your agent.

## Overview

FreshWay is a regional supermarket chain with 120 stores, three distribution centres and an online shop. Its company dossier is businesslike and precise: every figure has a unit and a confidence label (H hard, A derived, S estimate). This style follows that attitude. The visuals should impress, and they should still be correct.

- Guiding idea: keynote. One insight per view, shown large, with plenty of space around it. Shapes are soft and physical: rounded blocks with a subtle gradient, a light sheen and a soft shadow on a floor you do not see.
- The brand comes from the logo: green word mark, red apple, off-white paper. Green is identity and action. The apple is the one place the viewer should look.
- Two modes. Light is the default, for the browser and for a projector in a lit room. Dark is the presentation mode, full screen in a dimmed room. Same palette, same scene, different stage.
- 3D is there to draw the viewer in. The camera always ends in a reading position where values can be compared.
- Page language: English.

## Colors

Brand
- FreshWay green `primary #00702E`: logo, primary button, focus ring, links. Never a data colour.
- Apple red `focus #E8321E`: marks the one insight in a view with a single data series. For text use `focus-text #C42B1A` on light and `focus-on-dark #FF6A55` on dark. Red means "look here", not "wrong".

Stage
- Light: a radial gradient from `stage-glow #FFFFFF` through `stage #F4F3EF` to `stage-edge #DFE1DC`, with the highlight slightly right of centre, behind the insight.
- Dark: the same gradient from `stage-dark-glow #22342F` through `stage-dark #101B18` to `stage-dark-edge #060B0A`. A green-black that belongs to the brand ink, not a neutral black.
- Text on dark: `on-dark #F2F4F3` (16:1), labels `on-dark-muted #A9B8B4` (8.6:1).
- The page around the stage is `paper #FBF9F5` with `ink #16302A`.

Maps
- Land in light mode `land-light #FBF9F5`, in dark mode `land-dark #2A3834`, a deep green-grey. In both modes the land fades out towards the edges of the stage, so the map has no hard frame.

Data, one series
- Calm bars in sage `data-base #86A6A1`, the insight in apple red.

Data, several series
- Petrol `cat-1`, ochre `cat-2`, sky `cat-3`, clay `cat-4`, and `cat-other` for "other". At most four colours plus "other" in one view.
- The palette is checked with a colour-vision simulation (deuteranopia and protanopia): every pair stays clearly distinct. Colour is never the only signal. Each series also has its own marker shape (see Shapes) and a label at the end of the series.
- No apple red in a view with several series, because red and ochre look alike for people with red-green colour blindness. There the key figure carries the insight.
- Thin lines and text use the `-line` variants.

Scales
- Sequential: `seq-1` to `seq-6`, one petrol hue. Darker means more.
- Diverging: ochre through `div-mid` to petrol, along the blue-yellow axis.

## Typography

One family: Source Sans 3 (free, Google Fonts), with tabular figures so numbers do not jump.

- Six sizes: 120, 72, 40, 26, 17 and 15 px. The eyebrow is a 15 px variant in capitals with wide spacing.
- Slide or full-screen view: the insight sentence 56 to 72 px, the key figure 120 px.
- Body text at least 17 px. Labels in the 3D scene at least 15 px on screen, whatever their distance to the camera. Full screen at 1920 px wide: labels 17 px, the insight value 28 px.
- Two weights: 400 and 600. 700 only for the red insight label.

## Layout

- Spacing scale 4, 8, 16, 24, 40, 64, 104 px.
- The page is a series of chapters, one insight per chapter, 104 px apart.
- A chapter: a text column of 5 of 12 columns (eyebrow, insight sentence, key figure, short explanation, source) and the 3D stage in 7 columns. Below 900 px the stage goes under the text.
- Full screen: the stage fills the screen. The insight sentence sits top left; the scene sits to the right and lower, so text and chart never touch.
- Leave room: the data takes at most 60% of the stage width.

## Elevation & Depth

On the page there is no depth: no shadows on cards or buttons.

In the scene, depth comes from light and material:
- A soft, short cast shadow from one key light almost straight above.
- A contact shadow under every shape, as a soft blob or through ambient occlusion.
- A subtle gradient in every shape: 22% darker than the colour at the bottom, 6% lighter at the top.
- In dark mode a rim light from behind makes edges light up. Bloom only on the insight.
- No hard reflections, no glass, no neon.

## Shapes

- Corners on the page: 6 px for tags, 10 px for buttons, 20 px for the stage.
- Bars: rounded blocks, corner radius 0.1 at a width of 0.62. The top stays flat enough to read the height.
- Series markers each have their own shape: cube (petrol), sphere (ochre), cone (sky), octahedron (clay), torus (other). In 2D: square, circle, triangle, diamond, ring.
- On a map, stores are small discs in sage.

## Components

- Chapter: eyebrow, insight sentence as h2, key figure with label, explanation, source line with confidence tag, and the 3D stage.
- Key figure: the number in `kpi`, the label below in `body`, muted. No colour, no arrows.
- Confidence tag: `H`, `A` or `S`, as in the company dossier, with the word next to it (hard, derived, estimate).
- Controls under the stage: Replay, Reset view, Show as flat chart, Present. Height 44 px, icons 24 px, always with text. Present goes full screen and switches to dark; Esc or Exit present goes back.
- A "Made with GenAI" chip in the page header that links to the last chapter.
- Making-of: the last chapter, as large as the others. Three steps (data, made with GenAI, checked by a person), your Human-AI Agency label shown large, and a transparency statement.

## Dataviz & 3D

Use 3D to draw the viewer into the scene, or to give room to a second dimension (for example site × category). Values are read in the reading position. If there is no second dimension and no reason to draw the viewer in, use a flat chart.

Forms
- Bars: rounded blocks, 0.62 wide and deep, on a pitch of 1.0. Always from zero.
- Surfaces (3D heat maps): soft tiles per cell with a small gap, no smooth interpolation between measured points.
- Lines: tubes of 0.06 with round ends, markers on the measured values, the label at the end of the line.
- Points: markers with their own shape, diameter 0.3.
- Estimated values (S): semi-transparent (opacity 0.45) with a fine hatch on the top face. H and A are solid.
- Maps: the land is a thin plate with a slightly rounded edge, like a scale model. The sea is not a plane; the stage gradient is the sea. Borders as thin lines in `hairline`.

Material and light (details in "For your coding agent")
- Soft glossy material, like lacquered plastic: low roughness, clear coat, no metal.
- One key light almost straight above, slightly from the front left. A hemisphere light as fill. In dark mode a rim light from behind.
- The background is a radial gradient without a horizon. The floor is invisible and only catches shadow.

Camera
- Perspective camera with a 22° field of view.
- Entry position: azimuth −40°, elevation 30°.
- Reading position depends on the kind of chart: the position in which the metric reads best. Bars: azimuth −18°, elevation 9°. Maps: elevation 50° to 60°, because you read a map from above. On a map, heights (such as floor area) are read from their labels, so those labels are required.
- Orbiting is allowed within limits (azimuth ±40° around the reading position). No panning, zoom 0.8 to 1.2 at most, no auto-rotation.

Readability despite perspective
- Labels are HTML labels that follow the camera: always upright, fixed screen size, never hidden behind a shape, with a soft halo in the stage colour.
- Reference plane: a very thin plane at a meaningful value (average, norm, target), 7% opacity, with a bright front edge and a label at its right end.
- No grid lines or back wall in the scene. The flat chart has a full axis.
- By default only the insight gets a value label. Other values appear on hover or keyboard focus.
- No depth of field, not even during the camera move.

Several series and maps
- No apple red. The key figure carries the insight, large and without colour.
- In dark mode only things that move during the build-up may glow, for example a small point of light that travels along each arc and then fades. In the final view nothing glows.
- Arcs between locations: fresh flows dashed, ambient flows solid. Dashing is the second signal next to colour. In the final view arcs at 45% opacity; hovering a location sets its arcs to 100% and the rest to 15%.

## Motion

Calm and precise: one long camera move, nothing jerky. 5.0 seconds in total, played once. Order and easing are the same for every chart type; only the parts differ.

Map or network
1. 0.0 s: stage and light are there, camera in the entry position.
2. 0.71 to 2.43 s: the distribution centres grow from the land, ease-out without overshoot.
3. 1.14 to 2.71 s: the stores appear.
4. 1.71 to 4.0 s: the camera moves to the reading position (cubic ease-in-out).
5. 1.86 to 4.29 s: the arcs draw themselves, each with its travelling point of light.
6. From 4.29 s: labels fade in over 0.36 s.
7. 5.0 s: final view. After that: stillness, no loop, no rotating camera.

Bar chart
1. 0.0 s: stage and light, camera in the entry position.
2. 0.43 to 1.14 s: the reference plane fades in and widens.
3. From 0.86 s: bars grow from the floor, 1.14 s per bar, 71 ms apart, ease-out without overshoot.
4. 1.71 to 4.0 s: the camera moves to the reading position (cubic ease-in-out).
5. From 4.0 s: the camera stands still, labels fade in over 0.36 s. The insight is already red; in dark mode its glow fades in over 0.57 s.
6. 5.0 s: final view, then stillness.

- Start when the stage is half in view. Stop rendering when it is out of view.
- Text never moves with the camera. Key figures do not count up.
- When the data changes, bars grow to their new height in 0.4 s; the camera stays put.
- Switching light and dark: background and light cross-fade in 0.4 s; the camera stays put. This is part of the controls, so it stays fast.
- With `prefers-reduced-motion`: show the final view straight away, with a 0.2 s fade.

## For your coding agent

Three.js r170 or newer, or React Three Fiber with drei and `@react-three/postprocessing`.

Renderer
- `toneMapping: THREE.NeutralToneMapping`, `toneMappingExposure: 0.95`. Neutral keeps the brand colours true; ACES turns the red orange.
- `outputColorSpace: SRGBColorSpace`, pixel ratio at most 2.
- `shadowMap.type: PCFSoftShadowMap`.
- Environment: `PMREMGenerator.fromScene(new RoomEnvironment(), 0.04)`, `scene.environmentIntensity` 0.55.
- Background: the radial gradient as a `CanvasTexture` in `scene.background`, with the stage colours. Do not put a CSS gradient behind a transparent canvas: the bloom pass makes the canvas opaque.

Material
- Bars: `RoundedBoxGeometry(0.62, h, 0.62, 5, 0.1)` with `MeshPhysicalMaterial`: `roughness 0.34`, `metalness 0`, `clearcoat 0.6`, `clearcoatRoughness 0.28`, `sheen 0.25`, `sheenRoughness 0.6`.
- Gradient via `vertexColors`: factor 0.78 at the bottom to 1.06 at the top (`0.78 + 0.28 * t^0.8`).
- Growth: scale the mesh on `scale.y`, with the geometry origin on the floor.
- Reference plane: `BoxGeometry(width, 0.01, 1.5)` with a transparent `MeshBasicMaterial`, opacity 0.07, `depthWrite false`. Its front edge is a cylinder with radius 0.012 at opacity 0.75.
- Map land: `ExtrudeGeometry`, depth 0.15, `bevelSize 0.03`, `MeshStandardMaterial` in the land colour, roughness 0.9. Fade towards the edges with a radial `alphaMap` or by mixing into the stage colour in the shader.

Light
- Key light: `DirectionalLight`, white, intensity 2.2 (light) or 3.0 (dark), position (−5, 22, 9) relative to the scene, `castShadow`, `mapSize 2048`, shadow frustum −14 to 14, `bias −0.0004`, `normalBias 0.02`. Call `updateProjectionMatrix()` on the shadow camera after changing the frustum.
- `HemisphereLight` white to floor colour, intensity 0.9 (light) or 0.25 (dark).
- Rim light: `DirectionalLight` `#CFE3DE` from (12, 5, −10), intensity 0.8 (light) or 4.0 (dark).

Shadow and occlusion
- Floor: a `PlaneGeometry` with `ShadowMaterial`, opacity 0.16 (light) or 0.45 (dark).
- Contact shadow: a soft radial blob of 1.25 × 1.25 under every bar, opacity 0.8. In React Three Fiber, drei `ContactShadows` does the same (`opacity 0.5`, `blur 2.5`, `far 1.5`, `resolution 512`).
- Ambient occlusion: N8AO (`aoRadius 0.5`, `intensity 2`, quality medium). The GTAO pass in three.js can give rectangular artefacts at the screen edge.

Post-processing: at most three passes
- Light: render pass, N8AO, output pass.
- Dark: render pass, N8AO, `UnrealBloomPass(strength 0.45, radius 0.6, threshold 1.2)`, output pass.
- The bloom threshold is 1.2, so normal lit surfaces never glow. Give the one element that may glow an emissive intensity that passes it (roughly 1.5 to 2.5): the red insight, or the travelling points of light on a map.
- No depth of field, chromatic aberration, vignette, noise or lens flares.

Labels
- `CSS2DRenderer` or drei `<Html>`, `pointer-events: none` except on hover. Source Sans 3, sizes from Typography.

Budget for 60 fps on a laptop with integrated graphics
- At most 150,000 triangles per scene. One rounded bar with 5 segments is about 1,300 triangles.
- One shadow-casting light, shadow map 2048. At most 60 draw calls; use `InstancedMesh` for more than 50 identical shapes (stores, for example) and merge many arcs into one geometry.
- Measure with `renderer.info` and the browser's performance panel. If the frame rate drops below 50, set N8AO to quality low first, then halve the bloom resolution.
- Render only when something moves (`frameloop="demand"` in React Three Fiber), and not at all when the stage is out of view.

## Do's and Don'ts

- Do: one insight per view, in one sentence above or next to the scene.
- Do: always give unit, source and confidence (H, A, S) with a number.
- Do: colour plus a second signal: shape, position or label.
- Do: end in the reading position, with labels only once the camera stands still.
- Do: light by default, dark only as presentation mode.
- Do: a flat-chart version of every 3D chart.
- Do: say how the page was made, with your Human-AI Agency label.
- Don't: apple red next to ochre, or in a view with several series.
- Don't: green as a data colour or as a sign for "good".
- Don't: neon, glass, hard reflections, or glow on anything but the insight.
- Don't: bars that overshoot or bounce, numbers that count up.
- Don't: depth of field, or labels that are slanted or hidden behind a shape.
- Don't: text smaller than 15 px, buttons lower than 44 px.
