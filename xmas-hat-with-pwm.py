
#!/usr/bin/env python

import time

import rainbowhat
import RPi.GPIO as GPIO

print("Rainbow HAT Christmas Edition:  Press Control+C to quit.")

# Merry Christmas

# Pin definitions
led_pin = 18

# Use "GPIO" pin numbering
GPIO.setmode(GPIO.BCM)

# Set LED pin as output
GPIO.setup(led_pin, GPIO.OUT)

# Code constants
BRIGHTNESS_VAL = 0.3
PWM_BRIGHT = 90
PWM_DIM = 30

# initialise rainbow hat
rainbowhat.display.print_str("XMAS")
rainbowhat.display.show()
isFlip = True
# Initialize pwm object with 50 Hz and 0% duty cycle
pwm = GPIO.PWM(led_pin, 50)
pwm.start(0)
while True:
    # rainbow hat leds
    for x in range(7):
        # red 
        if isFlip: 
            if x % 2 == 1:
                rainbowhat.rainbow.set_pixel(6 - x, 0, 1, 0, brightness=BRIGHTNESS_VAL)
            else: 
                rainbowhat.rainbow.set_pixel(6 - x, 1, 0, 0, brightness=BRIGHTNESS_VAL)
            # set lights
            pwm.ChangeDutyCycle(PWM_BRIGHT)
        else:
            if x % 2 == 0:
                rainbowhat.rainbow.set_pixel(6 - x, 0, 1, 0, brightness=BRIGHTNESS_VAL)
            else: 
                rainbowhat.rainbow.set_pixel(6 - x, 1, 0, 0, brightness=BRIGHTNESS_VAL)
            pwm.ChangeDutyCycle(PWM_DIM)
    rainbowhat.rainbow.show()

    time.sleep(1)
    isFlip = not(isFlip)

# Never gets here : Stop, cleanup, and exit
pwm.stop()
GPIO.cleanup()