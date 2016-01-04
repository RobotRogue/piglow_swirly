#Thanks for checking out my PiGlow code! https://github.com/RobotRogue

import piglow
from time import sleep

piglow.auto_update = True

slp = 0.005 #setting the sleep value to a variable to make changing it a lot easier.
br = 125 #brightness of the LEDs when they are on.

# Addressing Each LED Syntax Below:
# piglow.led(LED_ID,LED_BRIGHTNESS)

def swirly():
#LEDs On:
    piglow.led(1,br)
    sleep(slp)
    piglow.led(7,br)
    sleep(slp)
    piglow.led(18,br)
    sleep(slp)

    piglow.led(2,br)
    sleep(slp)
    piglow.led(8,br)
    sleep(slp)
    piglow.led(17,br)
    sleep(slp)

    piglow.led(3,br)
    sleep(slp)
    piglow.led(9,br)
    sleep(slp)
    piglow.led(16,br)
    sleep(slp)

    piglow.led(4,br)
    sleep(slp)
    piglow.led(14,br)
    sleep(slp)
    piglow.led(6,br)
    sleep(slp)

    piglow.led(5,br)
    sleep(slp)
    piglow.led(15,br)
    sleep(slp)
    piglow.led(12,br)
    sleep(slp)

    piglow.led(10,br)
    sleep(slp)
    piglow.led(11,br)
    sleep(slp)
    piglow.led(13,br)
    sleep(slp)

#LEDs Off:
    piglow.led(1,0)
    sleep(slp)
    piglow.led(7,0)
    sleep(slp)
    piglow.led(18,0)
    sleep(slp)

    piglow.led(2,0)
    sleep(slp)
    piglow.led(8,0)
    sleep(slp)
    piglow.led(17,0)
    sleep(slp)

    piglow.led(3,0)
    sleep(slp)
    piglow.led(9,0)
    sleep(slp)
    piglow.led(16,0)
    sleep(slp)

    piglow.led(4,0)
    sleep(slp)
    piglow.led(14,0)
    sleep(slp)
    piglow.led(6,0)
    sleep(slp)

    piglow.led(5,0)
    sleep(slp)
    piglow.led(15,0)
    sleep(slp)
    piglow.led(12,0)
    sleep(slp)

    piglow.led(10,0)
    sleep(slp)
    piglow.led(11,0)
    sleep(slp)
    piglow.led(13,0)
    sleep(slp)

while True:
    swirly()
