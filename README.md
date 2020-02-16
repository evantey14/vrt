# Virtual Reality Telescope

Telescope education can be very erratic. Telescopes are expensive, heavy, and only really useful at night far away from light pollution, and even if you can figure out all of those things you're still at the mercy of the weather.

For ProjX Spring 2018, some friends and I built a telescope with a VR mode so it can be used anywhere to help students practice telescope use.

For the telescope, we followed a classic [Dobsonian](https://stellafane.org/tm/dob/) design. We attached an [Adafruit BNO055 IMU](https://learn.adafruit.com/adafruit-bno055-absolute-orientation-sensor/overview) with an Arduino to track the orientation of the telescope. This information is sent to [Stellarium](https://stellarium.org/) which takes care of showing what you'd actually see if you were using a telescope.
