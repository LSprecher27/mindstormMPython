#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Stop, Button
from pybricks.tools import wait
ev3 = EV3Brick()
motor = Motor(Port.B)
motor.run_angle(360, 720) # rotate forward exactly 360 degrees (one full turn)

ev3.speaker.say("Please stop moving me, this is torture")
motor.stop 