
#!/usr/bin/python

import time
import sys
import rainbowhat
import RPi.GPIO as GPIO

print('Number of arguments:', len(sys.argv), 'arguments.\n')
print('Argument List:', str(sys.argv), '\n')

# input check
if (len(sys.argv) != 4):
    if (sys.argv[1] > 1.0 or sys.argv[2] > 10 or sys.argv[3] > 10):
        print("""Error: Values are dangerous! See recommendations below.
        Rainbow HAT Christmas Edition:  python xmas-hat-cmd.py hat_brightness pwm_bright pwm_dim cycle_time timing
        - hat_brightness: Value between 0.0 and 1.0, recommend 0.4
        - pwm_bright: Bright value for led lights, recommend 5, or 5 percent of duty cycle
        - pwm_dim: Dim value for led lights, recommend 1, or 1 percent of duty cycle
        - cycle_time: Cycle time in seconds, recommend 1

        PWM values are low assuming that you are connecting without a resistor.
        # see https://cs.stanford.edu/people/nick/led-without-resistor/

        Press Control+C to quit.""")
    else:
        print("""Rainbow HAT Christmas Edition:  python xmas-hat-cmd.py hat_brightness pwm_bright pwm_dim cycle_time timing
        - hat_brightness: Value between 0.0 and 1.0, recommend 0.4
        - pwm_bright: Bright value for led lights, recommend 5, or 5 percent of duty cycle
        - pwm_dim: Dim value for led lights, recommend 1, or 1 percent of duty cycle
        - cycle_time: Cycle time in seconds, recommend 1

        PWM values are low assuming that you are connecting without a resistor.
        # see https://cs.stanford.edu/people/nick/led-without-resistor/

        Press Control+C to quit.""")
else:
    # Merry Christmas

    # Pin definitions
    led_pin = 18

    # Use "GPIO" pin numbering
    GPIO.setmode(GPIO.BCM)

    # Set LED pin as output
    GPIO.setup(led_pin, GPIO.OUT)

    # Code constants
    hat_brightness = sys.argv[1]
    # drive leds without resistor
    pwm_bright = sys.argv[2]
    pwm_dim = sys.argv[3]
    cycle_time = sys.argv[4]

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
                    rainbowhat.rainbow.set_pixel(6 - x, 0, 1, 0, brightness=hat_brightness)
                else: 
                    rainbowhat.rainbow.set_pixel(6 - x, 1, 0, 0, brightness=hat_brightness)
                # set lights
                pwm.ChangeDutyCycle(pwm_bright)
            else:
                if x % 2 == 0:
                    rainbowhat.rainbow.set_pixel(6 - x, 0, 1, 0, brightness=hat_brightness)
                else: 
                    rainbowhat.rainbow.set_pixel(6 - x, 1, 0, 0, brightness=hat_brightness)
                pwm.ChangeDutyCycle(pwm_dim)
        rainbowhat.rainbow.show()

        time.sleep(cycle_time)
        isFlip = not(isFlip)
