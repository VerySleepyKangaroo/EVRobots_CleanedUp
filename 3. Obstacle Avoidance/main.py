#!/usr/bin/env pybricks-micropython
import random
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


ev3 = EV3Brick()
obstacle_sensor = UltrasonicSensor(Port.S4)  # Ultrasonic sensor
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

# Main program loop
while True:
    # Move forward
    ev3.screen.print("Moving Straight")
    robot.drive(200, 0)

    # Stop if an obstacle is detected less than 10 cm away
    if obstacle_sensor.distance() < 100:
        robot.stop()
        ev3.screen.clear()
        ev3.screen.print("Obstacle detected!")

        # Randomly decide to turn left or right
        turn_direction = random.choice(["left", "right"])
        
        if turn_direction == "left":
            ev3.screen.print("Turning left")
            robot.turn(-90)  # Turn left
        else:
            ev3.screen.print("Turning right")
            robot.turn(90)  # Turn right

        # Resume moving forward
        ev3.screen.clear()
        ev3.screen.print("Resuming movement")
