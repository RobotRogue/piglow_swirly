#Thanks for checking out my PiGlow code! https://github.com/RobotRogue

import piglow
from time import sleep

# Future Changes:
# Try to find a better way of performing this loop
# Try to find a better way of addressing each LED, is there a way to simplify the below code?
# Consider adding in functionality to turn on and turn off
# Once the code is running there is no way to shut off the LEDs unless you kill the process
# Ideally there should be a way for the user to provide an input to stop the LED cycles
# Once the user selects stop, there should be a command to turn off all the LEDs

piglow.auto_update = True

slp = 0.05 #setting the sleep value to a variable to make changing it a lot easier.

# Addressing Each LED Syntax Below:
# piglow.led(LED_ID,LED_BRIGHTNESS)

def swirly():
#LEDs On:
    piglow.led(1,25)
    sleep(slp)
    piglow.led(7,25)
    sleep(slp)
    piglow.led(18,25)
    sleep(slp)

    piglow.led(2,25)
    sleep(slp)
    piglow.led(8,25)
    sleep(slp)
    piglow.led(17,25)
    sleep(slp)

    piglow.led(3,25)
    sleep(slp)
    piglow.led(9,25)
    sleep(slp)
    piglow.led(16,25)
    sleep(slp)

    piglow.led(4,25)
    sleep(slp)
    piglow.led(14,25)
    sleep(slp)
    piglow.led(6,25)
    sleep(slp)

    piglow.led(5,25)
    sleep(slp)
    piglow.led(15,25)
    sleep(slp)
    piglow.led(12,25)
    sleep(slp)

    piglow.led(10,25)
    sleep(slp)
    piglow.led(11,25)
    sleep(slp)
    piglow.led(13,25)
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
