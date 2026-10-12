# Design decisions

## Confirmed direction

The user’s objective is a convincing and impressive animatronic at twilight, with low hands-on burden and new spending under $200. A finished stationary prop is a successful fallback.

Build only the front half, roughly 24 inches across. The user will handle rear concealment. Eyestalks remain posed; moving jaw, blink, and animated stalks are out of scope.

Use existing materials first. Overnight 3D printing is valuable when it reduces manual sculpting: printer hours and hands-on hours must be tracked separately.

## Proposed construction — not yet tested

| Element | Proposal |
|---|---|
| Structure | Wood eye mounting plate; short PVC supports as useful |
| Face geometry | Hollow printed brow/socket/cheek/lip forms attached to supports |
| Covering | Existing half-inch flexible foam; curved panels with seams concealed by features |
| Thick features | Fold or laminate foam locally, or drape over printed forms |
| Eye | FloraCraft SmoothFōM 7.8-inch hollow half ball, item 10324963 |
| Eye mounting | Broad internal printed cradle; avoid depending on screws gripping foam |
| Motion | Pan/tilt with axes near the center of curvature; mechanism details pending |
| Finish | Test liquid latex on upholstery foam; fill/smooth rigid eye only as necessary; paint and brush-on gloss |
| Lighting | External light above and to one side; tune reflections and shadows on actual prop |

The eye product lists 7.8-inch diameter × 3.8-inch depth. Actual inner dimensions, wall thickness, roundness, and mass are unknown. Measure before CAD.

A hemisphere can expose its rim during rotation. The previously discussed 7 × 5-inch eye opening was only a starting sketch: validate aperture size, viewing angles, and motion together. Hide the rim with the fixed socket and restrict travel as needed.

## Visual direction

Heavy asymmetric brow; recessed fixed snarl; uneven ivory teeth; glossy cream/amber eye; muted olive-brown skin. Favor silhouette, large volumes, and shadows over fine scales.

Provisional proportions: 24-inch face, 10–12-inch projection, about 12 × 5-inch mouth. These are not fabrication dimensions. Prototype around the actual eye.

Print broad rounded forms with tapered edges. Allow for foam thickness. One half-inch foam layer offsets exposed geometry by roughly half an inch unless compressed; excessive padding can erase the expression.

## Material distinctions

- The photographed sheet appears to be flexible upholstery foam, but chemistry and density are not verified.
- SmoothFōM eye is rigid EPS; CraftFōM and soft upholstery foam are different materials.
- Liquid latex over upholstery foam is not cast foam latex.
- Mold Builder is a mold-making latex proposed for a small skin test, not a validated full-face finish.
- Craft acrylics are selected for rigid parts and color trials. Their adhesion/flexibility on our latex system still needs validation.
- Brush-on gloss belongs on the rigid eye, not across the flexible face.
- Adhesive choice must match the actual foam and printed material. Cosmetic glue is not a structural suspension connection.

## Open decisions

Actual eye dimensions; actuator suitability under load; pan/tilt construction; adhesive and coating compatibility; display weather exposure; final face layout and mounting. Resolve only the next dependency needed for fabrication.

## Rejected / superseded

Full 36-inch body: more surface and handling work without enough benefit. Full molded silicone skin: excessive process burden for this version. Whole-body liquid latex coverage is not mandatory; test and apply only where useful. Budget and time estimates from early scenarios were planning estimates, not simulations or measured results.

## October 11, 2026 — frame clarified and rib prototype generated

A rear ring with longitudinal curved ribs defines the dome; a separate wooden support carries the eye mechanism. PVC is optional, not a required box. The user is comfortable cutting plywood and prefers unattended printing only when useful.

[Rib prototype v1](cad/ribs-v1/README.md) uses two bolted 45-degree segments for a 90-degree meridian. Outer radius 292.1 mm allows 12.7 mm foam for a nominal 24-inch diameter. Printed ribs are 20 mm radially deep × 8 mm wide. Two 3 mm splice plates and four M4 bolts join them. CAD geometry is checked. On October 11, the builder confirmed the first print and sandwich-splice fit were successful; physical strength and foam behavior remain untested. Front terminations and rear-ring brackets remain to be designed around eye/mouth placement; ribs do not all need to meet at a pole.

## October 12 — Eye actuation candidate

Existing Deegoo-FPV MG996R servos and a DC bench supply reported. Two positional units are plausible pan/tilt candidates for a balanced lightweight eye; exact variant, function, dimensions, and current requirements remain to be tested. Keep the large unidentified motor out of the design unless needed. Do not equate TowerPro reference specifications with measured performance of these units.

## October 12 — Initial rib quantity

Use four assembled quarter ribs as a provisional starting layout, not a proven complete frame. Each rib uses two 45-degree segments and two splice plates. Rear mounting and front terminations still need layout around the eye/mouth. Do not join all front tips at a solid pole. Initial foam check with two arches showed no visible sag per builder; actual installed spacing and finished coating load remain to be tested. Decide on extra local supports after mounting rather than automatically printing more full ribs.

## October 12 — Motor shortlist and test plan

Inventory completed; all motors work per Ben. Prefer EcoPower WP110T plus a suitable Deegoo MG996R for separate pan/tilt axes; final choice pending controlled motion and loaded tests. Buehler 1.61.031.111.06 gearmotor remains a repetitive-sweep backup. Mega USB-powered, servo externally powered with common negative/GND. WANPTEK DPS3010U rated 0–30 V / 0–10 A; initial unloaded one-servo test at 5 V / 2 A limit. See MOTORS.md and firmware/servo-bench-test.

Balance gravity torque around pivots while preserving the eye's geometric rotation center and socket clearance. Center of mass and center of curvature need not coincide. Separate structural pivots/cradle support the eye; actual layout is not yet designed. Hold off motor purchases unless tests expose a shortfall. User wants prompt Amazon sourcing if replacement is necessary.
