#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, UltrasonicSensor
from pybricks.parameters import Port, Stop
from pybricks.tools import wait

# 1. Setup
ev3 = EV3Brick()
hinge_motor = Motor(Port.B)
distance_sensor = UltrasonicSensor(Port.S1)

ev3.speaker.say("Starting the mission")


                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
print("Forward until the eyes see an object...")

# 2. Main Loop
while True:
    # Start the car moving forward
    hinge_motor.run(500)

    try:
        # Check if something is closer than 300mm (30cm)
        if distance_sensor.distance() < 300:
            # Stop immediately
            hinge_motor.stop(Stop.BRAKE)
            print("Object spotted! Reversing...")
            
        
            # 3. Move the other direction for 2.5 seconds
            # Speed is -500 for reverse
            hinge_motor.run_time(-500, 2500)
            
            hinge_motor.stop(Stop.BRAKE)
            break
            
    except OSError:
        pass

    wait(10)

ev3.speaker.say("Mission complete")
ev3.speaker.play_file('test.wav')