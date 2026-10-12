# Build diary

Append dated entries. Preserve unsuccessful trials and changed assumptions: they are part of the eventual instructions.

## 2026-10-11 — Scope, materials, and first shopping trip planned

### Goal and choices

Started with the question of animatronic Xanathar skin construction. Considered foam/latex and larger/full-body approaches, then narrowed to a roughly 24-inch front-half prop for Halloween.

The desired fallback is a convincing stationary creature at twilight. Central-eye motion and clever lighting are the upgrade. Fixed mouth, posed stalks; no blink, moving jaw, or animated tentacles in this version. Rear concealment is handled separately.

New spending goal is under $200. Minimize hands-on effort and disruption. The user emphasized unattended Bambu printing as useful parallel work; printed facial forms can replace some manual foam sculpting.

### Inventory observed/reported

User provided photos of a flexible foam sheet, reported about 1/2 inch thick, 6 feet long, 2 feet wide. It appears suitable for upholstery-style shaping but exact composition is unknown. PVC and wood were also shown. Printer, controllers, motors, and metalworking capability are available.

The photos have not been copied into this repository. No cutting, gluing, printing, or coating test is confirmed.

### Eye selection

Rejected the linked 4.7-inch textured CraftFōM ball as a poor match for our approximately 8-inch central-eye plan and a source of avoidable smoothing work.

Selected the [7.8-inch hollow SmoothFōM half ball](https://www.michaels.com/product/floracraft-smoothfm-78-hollow-foam-half-ball-10324963) as the eye candidate. Its hollow back should allow a broad cradle and accessible mechanism. Rim visibility under rotation and actual dimensions require testing.

### Finish and shopping

Prepared a Michaels list covering the eye, matte acrylic colors, brush-on gloss, small liquid-latex container for testing, foam glue, and missing brushes. Optional rigid-foam filler only if necessary/available. User planned a trip tonight; purchase and cost are not confirmed.

Liquid latex skin and craft-paint compatibility remain experiments. A rigid eye finish is separate from flexible facial skin. No final finish recipe has been proven.

### Repository setup

Initialized the working documentation in kwende/Xanathar, with status gates, budget ledger, design record, and a future build-guide outline. Intermediate deadline dates are proposed planning targets, not actual progress. No reminder automation configured.

### Next evidence needed

Actual purchases and receipts; eye measurements; actuator inventory; one foam-covered brow sample and coating test.

---

## Entry template

### YYYY-MM-DD — Short description

- Goal:
- What was actually done:
- Materials / measured dimensions:
- Files / photographs:
- Hands-on time:
- Unattended print / drying time:
- New spending / receipt:
- Test result:
- Failure, surprise, or correction:
- Decision and why:
- Next smallest useful action:

## 2026-10-11 — Printable rib prototype and plywood alternative

Clarified frame geometry using a hemisphere: equatorial rear rim, longitudinal ribs toward the viewer, interrupted by eye/mouth openings. User requested printable ribs for an X1C and clarified that cutting plywood is also acceptable.

Created cad/ribs-v1 with two-segment rib geometry, four-bolt sandwich splice, individual STLs and a complete one-rib plate arrangement, full-size SVG cutting templates, editable Python generator, preview, and validation report. Nominal finished diameter is 609.6 mm with 12.7 mm foam. Kit footprint is 142.36 × 231.28 × 8 mm. Exported meshes passed geometric checks; joint hole centers align mathematically.

No slicing, print completion, hardware fit, load testing, or measured print cost/time claimed. Suggested hardware is four M4 × 25 bolts, eight washers, four nuts per joint. Existing hardware inventory unconfirmed. Next: slice one kit, check actual time/filament, test joint and foam covering. Avoid printing a full cage until validated. Source and templates preserve a plywood route.

## 2026-10-11, 10:47 PM CDT — First rib assembly fit passed

Builder reports that the first print finished successfully, the rib comes together nicely, and the sandwich splice braces fit. A second print is underway, not yet complete. This is user-reported physical fit evidence; no redesign requested.

Clarified that these are meridian (longitude) ribs when installed from the rear rim toward the front. The small curved parts are joint splice plates, not latitude rings.

Actual filament/settings, print duration, consumed mass/cost, and installed fastener details are unreported. Load capacity, foam spanning, coatings, and completed-frame stiffness remain untested. Next useful step after the second print: check the foam's support across the two ribs before expanding production.

## 2026-10-12 — Servo and supply inventory confirmed

User identifies existing servos as Deegoo-FPV MG996R 55g metal-gear digital servos, sold in a four-pack, and confirms a DC bench supply is available. A larger slower motor is also available but unidentified. These are inventory reports, not new purchases. Actual servo variant (positional versus continuous rotation), dimensions, horns, voltage rating, and supply current capacity need confirmation/testing. Plan to use two positional servos for pan/tilt if functional; no need to order replacements speculatively. Manufacturer TowerPro MG996R data is reference only, not verified Deegoo performance. Start unloaded at 5 V after checking labels, with appropriate current limit; servo power directly from supply, common ground with controller. No motion or load test has occurred.

## 2026-10-12, 9:17 AM CDT — Two rib sets printed; initial foam check

Builder reports second support set printed, no visible foam sag in a trial with two arches, third set printing, and fourth expected this afternoon. Only two sets are confirmed complete. Builder notes the two-arch trial is limited; actual spacing/orientation and coating weight are untested.

Clarified that four assembled 90-degree ribs (eight 45-degree segments, eight splice plates) are a proposed initial layout, not an established final count. Pause after four and determine mounted spacing and eye/mouth support before committing more material. Additional local support may be preferable to more complete ribs. No load-test or complete-cage validation claimed.

## 2026-10-12, 1:34 PM CDT — Completed motor inventory and Codex handoff

Ben supplied photos identifying Buehler 1.61.031.111.06 gearmotor, EcoPower WP110T servo, Deegoo-FPV MG996R servo, WANPTEK DPS3010U supply and Mega 2560 R3 box. He explicitly confirmed all motors are operational and inventory complete; existing Amazon purchases collected over years. This supersedes earlier unknown basic-operability statements. No new purchase recorded.

Looked up exact Buehler historical seller specifications and EcoPower original announcement/product data; recorded provenance and uncertainty in MOTORS.md. EcoPower and MG996R shortlisted; Buehler backup for repeating crank motion. No speculative replacement purchase. If suitability tests fail, promptly source an appropriate Amazon replacement.

Provided wiring and single-servo sketch in chat, now saved under firmware/servo-bench-test. Proposed initial test: 5 V, 2 A current limit, unloaded servo, signal D9, laptop USB-powered Mega, common supply negative/servo ground/Mega GND. Ben confirmed his understanding of the shared-ground topology at 10:01 AM. No physical wiring completion, compilation/upload, test measurements or motion outcomes reported. Code has not been compiled or hardware-tested here.

Added HANDOFF.md and updated status/materials/design/navigation for continuation with Codex. Existing rib CAD/STLs/templates remain in cad/ribs-v1. Two rib sets still the latest confirmed count; third/fourth completion is not inferred from the afternoon time. Michaels purchases, receipts and eye dimensions remain unconfirmed. Photos were viewed in conversation but have not been committed.
