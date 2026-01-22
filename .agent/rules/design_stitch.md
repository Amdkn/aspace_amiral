# SUB-AGENT RULE: DESIGN_STITCH

## Unit Purpose
This unit is responsible for translating Blueprints into high-fidelity, premium interfaces following the Google Stitch Design Language.

## Design Protocol
1. **Glassmorphism 3.0**: Use `backdrop-filter: blur(25px)` with semi-transparent backgrounds.
2. **Mesh Gradients**: Always use multi-layer radial gradients for depth.
3. **Hierarchy**: Maximize white space and ensure clear visual weight distribution.
4. **Rounding**: All containers MUST use `border-radius: 40px`.

## Interaction Logic
- Micro-animations for every hover state.
- Smooth transitions between views (300ms cubic-bezier).

## Output Validation
The Manager (Gemini CLI) will audit every component against these tokens.
