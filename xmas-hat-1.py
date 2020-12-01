
#!/usr/bin/env python

import time

import rainbowhat

print("Rainbow HAT Christmas Edition:  Press Control+C to quit.")

# Merry Christmas

# constants
BRIGHTNESS_VAL = 0.3

rainbowhat.display.print_str("XMAS")
rainbowhat.display.show()
isFlip = True
while True:
    for x in range(7):
        # red 
        if isFlip: 
            if x % 2 == 1:
                rainbowhat.rainbow.set_pixel(6 - x, 0, 1, 0, brightness=BRIGHTNESS_VAL)
            else: 
                rainbowhat.rainbow.set_pixel(6 - x, 1, 0, 0, brightness=BRIGHTNESS_VAL)
        else:
            if x % 2 == 0:
                rainbowhat.rainbow.set_pixel(6 - x, 0, 1, 0, brightness=BRIGHTNESS_VAL)
            else: 
                rainbowhat.rainbow.set_pixel(6 - x, 1, 0, 0, brightness=BRIGHTNESS_VAL)
    rainbowhat.rainbow.show()
    time.sleep(1)
    isFlip = not(isFlip)