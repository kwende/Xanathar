# Motor and electronics inventory

Updated October 12, 2026, 1:34 PM CDT. Inventory complete per Ben. Existing Amazon purchases collected over years; no new motor purchase recorded. **Ben confirms all these motors work.** Project-specific position/smoothness/current/load tests have not been reported.

| Item | Evidence / specifications | Project assessment |
|---|---|---|
| Buehler 1.61.031.111.06 | Label photographed, dated November 98; two leads and right-angle gearbox. Historical MPJA catalog: 12 V DC, approximately 21 RPM at 12 V, 0.3 A no-load, 4.5 A stall, 8 mm shaft. Seller data, not measured or manufacturer-certified here; torque unknown. | Backup for repeating sweep via crank. No accessible feedback apparent; programmable gaze would require added sensor/driver/control. Deprioritized. |
| EcoPower WP110T | Label photographed: waterproof, 6.0 V; clamping horn attached. Original AMain announcement: 4.8–6 V, 280 oz-in (~20.2 kgf-cm / 1.98 Nm) at 6 V, 0.16 s/60°, 53 g, 25T spline, metal gears. | First positional-servo candidate for one axis. Keep this labeled unit at/below 6 V despite higher-voltage claims in newer listings. Published torque is not a continuous-load guarantee. |
| Deegoo-FPV MG996R | Exact brand/model photographed; three-wire lead and retaining screw; horn not attached in photo. Earlier purchase description was a four-pack; actual available quantity and horns need counting. | Second-axis/spare candidate. Confirm commanded position holding and smoothness. Do not copy TowerPro ratings onto Deegoo units. Exact current, travel and torque remain unverified. |
| WANPTEK DPS3010U | Model photographed; manufacturer specifies 0–30 V, 0–10 A. | Enough rated capacity for planned one-servo tests; actual transient behavior/wiring still matter. Initial test 5 V, 2 A limit. |
| Arduino Mega 2560 R3 | Box photographed. | Laptop USB power; D9 test signal; GND shared with supply negative. |

## Decision

No demonstrated motor/supply shortage; do not purchase replacements speculatively. Test EcoPower and one MG996R using [the bench sketch and instructions](firmware/servo-bench-test/README.md). Different servo models can operate separate axes. Choose final axes after mechanism geometry and tests.

If existing candidates fail the actual requirement, promptly research an appropriate positional servo on Amazon, checking voltage, torque margin, mounting/horns, price and actual delivery timing. No replacement selected or ordered yet.

## Evidence and sources

Photos were inspected in conversation but **are not stored in this repository**. Ben's operability confirmation is user-reported evidence, not our test measurement.

- [Historical MPJA catalog mirror, exact Buehler part number](https://device.report/m/d05f36f1f59c309b9b80fba573a9eea94a294435e12cd85f35e93d082f34c8b8)
- [AMain EcoPower WP110T listing](https://www.amainhobbies.com/ecopower-wp110t-waterproof-high-torque-metal-gear-servo-ecp-110t/p734713)
- [Original AMain announcement reproduced by LiveRC](https://www.liverc.com/news/new-ecopower-waterproof-servos-from-amain-hobbies/)
- [WANPTEK specifications](https://www.wanptek.com/productinfo/1171926.html)

Sources checked October 12. Published specifications and engineering estimates are not physical measurements of these units.
