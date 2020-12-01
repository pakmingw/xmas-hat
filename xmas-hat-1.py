
#!/usr/bin/env python

import time

import rainbowhat

print("""Rainbow HAT Christmas Edition

Press Control+C to quit.
""")

# Merry Christmas

while True:
    rainbowhat.display.print_str("XMAS")
    rainbowhat.display.show()
    time.sleep(1.0)

