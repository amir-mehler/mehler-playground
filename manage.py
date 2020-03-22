#!/usr/bin/env python3

import time

print("Running the manage file!")

x=12
while x>0:
    print("This is build is taking a long time! ({} seconds left)".format(x))
    x -= 1
    time.sleep(1)

print("Finished at last")

