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



def check_obstacle_and_avoid(threshold_mm=150):
    """Check ultrasonic distance and perform avoidance maneuver."""
    distance_mm = obstacle_sensor.distance()
    if distance_mm < threshold_mm:
        robot.stop()
        # back up for 0.5 seconds
        robot.drive(200, 0)
        wait(500)
        robot.stop()
        # turn around 180 degrees
        robot.turn(180)
        # resume forward drive
        robot.drive(-500, 0)
        return True

    return False


def main():
    """Main loop to drive the robot and avoid obstacles."""
    robot.drive(-200, 0)

    while True:
        if check_obstacle_and_avoid(300):
            # immediately continue with forward drive after turning
            continue

        # keep driving forward while unobstructed
        robot.drive(-500, 0)
        wait(100)


if __name__ == '__main__':
    main()