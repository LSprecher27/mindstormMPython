#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase
from pybricks.tools import wait

# Create the EV3 object
ev3 = EV3Brick()

# Set up motors
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

# Set up the color sensor on port S3
color_sensor = ColorSensor(Port.S3)

# Create the robot drive base
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

# Beep when program starts
ev3.speaker.beep()

base_speed = -120   # forward / backward speed
turn_rate = 80      # how strongly it turns
threshold = 20      # point where black and white switch

while True:
    light = color_sensor.reflection()

    if light < threshold:
        robot.drive(base_speed, turn_rate)
   
    else:
        robot.drive(base_speed, -turn_rate)

    wait(20)