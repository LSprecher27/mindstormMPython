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

def check_obstacle_and_avoid(threshold_mm=150):
    """Check ultrasonic distance and perform avoidance maneuver if obstacle is detected."""
    distance_mm = obstacle_sensor.distance()
    if distance_mm < threshold_mm:
        robot.stop()
        # back up for 0.5 seconds
        ev3.speaker.say("Obstacle detected")
        robot.drive(-100, 0)  # back up (negative for backward)
        wait(500)
        robot.stop()
        # turn around 180 degrees
        robot.turn(180)
        # resume forward drive
        robot.drive(100, 0)  # forward
        return True
    return False

def display_status():
    """Display current sensor readings on EV3 screen."""
    distance = obstacle_sensor.distance()
    ev3.screen.clear()
    ev3.screen.print("Distance: {} mm".format(distance))

def main():
    """Main loop to drive the robot, avoid obstacles, and check surface."""
    robot.drive(100, 0)  # drive forward

    while True:
        display_status()
        if check_obstacle_and_avoid(300):
            # immediately continue with forward drive after turning
            continue

        wait(100)

if __name__ == '__main__':
    main()