#include <Servo.h>

// Unloaded, single-servo suitability test. See README.md before powering.
// D9 is the signal; servo power comes directly from the bench supply.
Servo eye;
int positionUs = 1500;

void moveTo(int targetUs) {
  while (positionUs != targetUs) {
    positionUs += (targetUs > positionUs) ? 1 : -1;
    eye.writeMicroseconds(positionUs);
    delay(10);  // 200 us of command travel takes about 2 seconds.
  }
  delay(2000);  // Hold and observe jitter.
}

void setup() {
  eye.attach(9, 1300, 1700);
  eye.writeMicroseconds(1500);
  delay(3000);
}

void loop() {
  moveTo(1300);
  moveTo(1500);
  moveTo(1700);
  moveTo(1500);
}
