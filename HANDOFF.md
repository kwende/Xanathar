# Codex handoff — October 12, 2026, 1:34 PM CDT

Read AGENTS.md, then STATUS.md, DESIGN.md, MATERIALS.md and the latest diary entries. This file summarizes the active conversation so work can resume without reinventing decisions.

## Active task

Assess existing motors for the central eye before buying anything. Inventory is complete, all motors work per Ben, and supply/controller are identified. The [single-servo sketch and wiring](firmware/servo-bench-test/README.md) were supplied in chat. Ben confirmed his understanding: Mega powered by laptop USB, supply negative shared by servo ground and Mega GND. **No completed wiring, upload, current measurement or suitability-test result has been reported.** Ask for test observations; do not mark tests passed.

EcoPower WP110T is first candidate; Deegoo MG996R second axis/spare; Buehler gearmotor is backup for a repetitive crank sweep. See MOTORS.md. No hardware purchase currently justified. If existing candidates prove inadequate, Ben wants an appropriate Amazon replacement found promptly to avoid delivery delays.

## Physical build

- Roughly 24-inch front half only; rear concealment handled by Ben.
- Static convincing twilight prop succeeds. Moving central eye plus lighting is the upgrade.
- Under $200 new spending; actual spending unknown. Minimize hands-on work and household disruption.
- Bambu X1C prints unattended; plywood is also welcome.
- Existing foam approximately 1/2 × 24 × 72 inches; soft cushion material, chemistry unknown. Existing wood and PVC available.
- cad/ribs-v1 contains editable generator, STLs, full-size SVG plywood templates, preview, requirements and mesh validation.
- Two assembled rib sets confirmed printed; first sandwich splice fits. Third was printing that morning, fourth planned that afternoon. **Do not infer later completion from time elapsed.**
- Four assembled 90° arches is a provisional starting layout, not a proven final cage. Each uses two 45° segments and two splice plates.
- Initial two-arch foam trial: no visible sag per Ben. Actual installed spans, coating weight and frame stiffness remain unvalidated.
- These are longitude/meridian ribs. They define curvature; foam bridges them. Add local cross-supports or ribs only where shape/support requires it.
- Rear ring/front termination brackets and final face layout are not yet designed. Do not converge all ribs at a solid pole; eye and mouth need openings.
- Eye mechanism needs its own rigid wood support; foam and cosmetic ribs should not carry it.

## Next dependencies

1. Obtain one-servo test observations at proposed 5 V / 2 A initial limit, using D9; resolve supply limiting before blaming jitter.
2. Confirm Michaels purchases and actual eye dimensions/mass. Selected blank: FloraCraft SmoothFōM 7.8-inch hollow half ball, item 10324963, listed 3.8-inch depth; not confirmed purchased.
3. Establish four-rib mounted layout and foam spans; keep static-face progress running alongside motion work.
4. Build accessible lightweight eye mockup and validate travel/rim concealment before final mounting CAD.
5. Record actual results, settings, costs and failures for the eventual reproducible guide.

Do not expand to blink, moving jaw, animated eyestalks, full body or larger body. Coatings and foam adhesive remain scrap-test proposals; no proven skin recipe. Aim for broad brow/cheek/lip volumes, matte olive-brown skin and glossy cream/amber eye, fixed snarl and posed stalks.

## Validation limitations

Rib CAD was computationally checked and first joint fit physically confirmed. The validation.json preserves generation-time evidence, not later print events. Servo code is the chat test sketch, not production animation firmware; it has not been compiled or run here. Uploaded photos were viewed in chat but not committed. Schedule gates in STATUS.md are targets, not reminders or promises.
