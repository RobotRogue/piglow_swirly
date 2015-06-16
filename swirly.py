import piglow
from time import sleep

piglow.auto_update = True

# Addressing Each LED Syntax Below:
# piglow.led(LED_ID,LED_BRIGHTNESS)

def swirly():
#LEDs On:
    piglow.led(1,25)
    sleep(0.05)
    piglow.led(7,25)
    sleep(0.05)
    piglow.led(18,25)
    sleep(0.05)

    piglow.led(2,25)
    sleep(0.05)
    piglow.led(8,25)
    sleep(0.05)
    piglow.led(17,25)
    sleep(0.05)

    piglow.led(3,25)
    sleep(0.05)
    piglow.led(9,25)
    sleep(0.05)
    piglow.led(16,25)
    sleep(0.05)

    piglow.led(4,25)
    sleep(0.05)
    piglow.led(14,25)
    sleep(0.05)
    piglow.led(6,25)
    sleep(0.05)

    piglow.led(5,25)
    sleep(0.05)
    piglow.led(15,25)
    sleep(0.05)
    piglow.led(12,25)
    sleep(0.05)

    piglow.led(10,25)
    sleep(0.05)
    piglow.led(11,25)
    sleep(0.05)
    piglow.led(13,25)
    sleep(0.05)

#LEDs Off:
    piglow.led(1,0)
    sleep(0.05)
    piglow.led(7,0)
    sleep(0.05)
    piglow.led(18,0)
    sleep(0.05)

    piglow.led(2,0)
    sleep(0.05)
    piglow.led(8,0)
    sleep(0.05)
    piglow.led(17,0)
    sleep(0.05)
    
    piglow.led(3,0)
    sleep(0.05)
    piglow.led(9,0)
    sleep(0.05)
    piglow.led(16,0)
    sleep(0.05)
    
    piglow.led(4,0)
    sleep(0.05)
    piglow.led(14,0)
    sleep(0.05)
    piglow.led(6,0)
    sleep(0.05)
    
    piglow.led(5,0)
    sleep(0.05)
    piglow.led(15,0)
    sleep(0.05)
    piglow.led(12,0)
    sleep(0.05)
    
    piglow.led(10,0)
    sleep(0.05)
    piglow.led(11,0)
    sleep(0.05)
    piglow.led(13,0)
    sleep(0.05)
    
while True:
    swirly()
