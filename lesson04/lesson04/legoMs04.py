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

'''
Robot Movement Idea:
    - Start Driving
        - Loop forever
            - If the obstacle is within 150 mm, play sound and stop
                - Else, keep driving
'''



while True:
    # If an object is detected within 150 mm, stop the robot and play music
    if obstacle_sensor.distance() < 150:
        # stop the robot
        robot.stop()
        # set speaker to 50% volume
        ev3.speaker.set_volume(50)
        # play the sound 
        ev3.speaker.beep(800, 500)
    else:
        # if not, keep the robot driving
        robot.drive(-100, 0)
        #stop the robot after a while
    wait(100)