# Single-servo bench test

Prepared October 12, 2026. **Not yet compiled/uploaded or physically tested in this project.** Ben confirms all inventoried motors already work; this test evaluates suitability, not basic operability.

## Hardware and power

- Arduino Mega 2560 R3 (identified from supplied box).
- WANPTEK DPS3010U: manufacturer rates output 0–30 V, 0–10 A.
- Test EcoPower WP110T first, then one Deegoo-FPV MG996R.
- Secure the case; leave the horn clear and unloaded. No eye or linkage attached yet.
- Initial test setting: **5.0 V, 2 A current limit**, one servo at a time. This limit is a proposed test setting, not a measured requirement.
- Set/verify voltage before connection; switch supply off while wiring or swapping motors. Set the current limit using the supply's documented procedure; a no-load zero-amp reading is not the current-limit setting.
- Mega powered from laptop USB. Servo powered directly from supply; do not route servo current through the Mega or thin breadboard power rails.
- Use supply **negative**, not green protective earth, as the signal ground reference. Do not connect supply positive to Mega 5V/VIN.

| Connection | Destination |
|---|---|
| Servo red | Supply + |
| EcoPower black / Deegoo brown | Supply − |
| Mega GND | Supply − |
| EcoPower white / Deegoo orange | Mega D9 |
| Mega USB | Laptop |

The shared negative/GND makes the servo signal meaningful relative to the same reference voltage. The servo's high-current return goes directly to the supply.

## Run

1. Open servo-bench-test.ino in Arduino IDE; select Arduino Mega or Mega 2560 and its port.
2. Install the official Arduino Servo library if missing; compile/upload with servo power off.
3. With connections checked and horn clear, turn on servo supply. Reset Mega to restart the initial center hold if needed.
4. Observe at least two cycles. Switch servo power off before changing hardware.
5. Repeat with an MG996R and label which physical unit was tested.

The sketch commands 1500 us, then ramps through 1300 → 1500 → 1700 → 1500 us. Each 200 us ramp takes about two seconds, followed by a two-second hold. Exact physical angles are not calibrated. This deliberately avoids a full-range endpoint sweep. An initial repositioning when powered/reset can still be abrupt.

If the shaft rotates continuously rather than settling, switch off and record that behavior: it may be a continuous-rotation variant. If it binds/hits a stop, switch off rather than forcing travel. If the supply enters CC or OCP trips, investigate wiring/load/current limiting before interpreting jitter as servo failure. Do not deliberately stall the motor to measure current.

## Record results

| Unit | Voltage | Limit | Distinct positions held? | Slow-motion quality | Stationary twitch/noise | Displayed moving/holding current | CC/OCP? |
|---|---|---|---|---|---|---|---|
| EcoPower WP110T | Pending | Pending | Pending | Pending | Pending | Pending | Pending |
| Deegoo MG996R (identify unit) | Pending | Pending | Pending | Pending | Pending | Pending | Pending |

A little audible buzz alone is not failure. The supply display may miss brief current peaks. This test does not establish output torque, loaded reliability, final travel or final supply requirements.

If both pass, test a lightweight mock eye on the intended pivots/linkage next. Favor supporting the eye on dedicated pivots and keeping gravity torque low. Geometric center of curvature governs rotation/aperture clearance; center of mass governs gravity torque. These are not necessarily the same point for a hemisphere and cradle. Balance/lighten the assembly as useful without sacrificing rim clearance.

## Sources

- [WANPTEK DPS-series specifications](https://www.wanptek.com/productinfo/1171926.html)
- [Arduino external power and common grounds](https://support.arduino.cc/hc/en-us/articles/360018922259-What-power-supply-can-I-use-with-my-Arduino-board)
- [Arduino Servo API](https://github.com/arduino-libraries/Servo/blob/master/docs/api.md)

See [motor inventory](../../MOTORS.md) and [handoff](../../HANDOFF.md).
