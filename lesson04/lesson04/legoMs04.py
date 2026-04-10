#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, UltrasonicSensor
from pybricks.parameters import Port, Stop
from pybricks.tools import wait

# Initialize the EV3 Brick
ev3 = EV3Brick()

# Initialize Motors on Ports B and C
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

# Initialize the Ultrasonic Sensor on Port S4
ultrasonic_sensor = UltrasonicSensor(Port.S4)

# Set the speed (1000 is usually the maximum degrees per second)
DRIVE_SPEED = 1000 
STOP_DISTANCE = 200 # mm

# Start driving forward
left_motor.run(DRIVE_SPEED)
right_motor.run(DRIVE_SPEED)

# Loop that checks the sensor constantly
while True:
    # Check if an object is closer than 200mm
    if ultrasonic_sensor.distance() <= STOP_DISTANCE:
        # Stop the motors immediately
        left_motor.stop(Stop.BRAKE)
        right_motor.stop(Stop.BRAKE)
        
        # Beep to signal the stop
        ev3.speaker.beep()
        break 
    
    # Small wait to keep the CPU from overworking
    wait(10)