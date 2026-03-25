#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, UltrasonicSensor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase
from pybricks.tools import wait

ev3 = EV3Brick()
left_motor  = Motor(Port.B)
right_motor = Motor(Port.C)
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

obstacle_sensor = UltrasonicSensor(Port.S4)

ev3.speaker.beep()

# Drive forward until something is closer than 200 mm (about 8 inches).
while True:
    distance = obstacle_sensor.distance()

    if distance < 300:
        robot.drive(400,0)
        wait(50)
    else:
        robot.drive(-900, 0)

    wait(10)
    ev3.screen.print("Object detected!")
ev3.screen.print("Dist: " + str(distance) + " mm")