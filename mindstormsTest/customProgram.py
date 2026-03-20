#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.parameters import Color
from pybricks.tools import wait
# Create the EV3Brick object. We need this in every program.
ev3 = EV3Brick()
# -------------------------------------------------------
# SCREEN
# -------------------------------------------------------
# Clear the screen so it's blank before we write anything.
for i in range(3):
print("This prints 3 times")
wait(500)