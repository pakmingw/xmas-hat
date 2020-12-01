
#!/usr/bin/env python

import time

import rainbowhat

print("Rainbow HAT Christmas Edition:  Press Control+C to quit.")

# Merry Christmas
rainbowhat.display.print_str("XMAS")
rainbowhat.display.show()

while True:
    isFlip = True
    for x in range(7):
        # red 
        if isFlip: 
            if x % 2 == 1:
                rainbowhat.rainbow.set_pixel(6 - x, 0, 1, 0, brightness=0.1)
            else: 
                rainbowhat.rainbow.set_pixel(6 - x, 1, 0, 0, brightness=0.1)
        else:
            if x % 2 == 1:
                rainbowhat.rainbow.set_pixel(6 - x, 0, 1, 0, brightness=0.2)
            else: 
                rainbowhat.rainbow.set_pixel(6 - x, 1, 0, 0, brightness=0.2)
    rainbowhat.rainbow.show()
    time.sleep(1)