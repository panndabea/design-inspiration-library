# Accessibility and Performance Principles

Report 19 is explicit: accessibility is not a side topic; design "eine semantische Information mit mehreren gleichberechtigten Renderern" (one semantic information model with several equal renderers, Umwelt). Report 18 notes that older WebGL/audio projects can have browser-compatibility issues. Everything else here is general guidance **[G]**.

## Accessibility (mandatory for every direction)
- Keyboard operation for every control, including drag interactions (arrow keys / input fields as equivalents). [G]
- Visible focus states; logical focus order across narrative steps. [G]
- WCAG 2.2 AA contrast; never encode meaning with colour alone. [G]
- `prefers-reduced-motion`: replace animated transitions with discrete state changes. [G]
- Text equivalents generated from the same data as the visual (aria-live summaries, data tables, outline views). [R19 Umwelt] [G]
- Responsive behaviour: define the mobile version of each signature interaction explicitly. [G]
- Clear hierarchy: one heading structure that also works as a table of contents. [G]

## Performance (proportional to value)
- Prefer SVG/Canvas 2D; use WebGL/3D only when space carries meaning. [R19 "Use space when space means something"] [G]
- No large animation frameworks for a few transitions; CSS and small libraries first. [G]
- Lazy-load figures and heavy libraries; start simulations paused; stop work in hidden tabs. [G]
- Run heavy computation in Web Workers. [G]
- Budget: state an explicit JS and asset budget per direction during design review. [G]
