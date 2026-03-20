#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.tools import wait
from pybricks.parameters import SoundFile



# Initialize the EV3
ev3 = EV3Brick()
# Play a built-in sound file

# To play a custom file, place it in your project folder and reference it by name
ev3.speaker.play_file("test.wav")


ev3.screen.print("LIMP BIZKIT LIMP BIZKIT LIMP BIZKIT LIMP BIZKIT LIMP BIZKIT LIMP BIZKIT LIMP BIZKIT LIMP BIZKIT LIMP BIZKIT LIMP BIZKIT")

