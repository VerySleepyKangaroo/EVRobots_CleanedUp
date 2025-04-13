#!/usr/bin/env pybricks-micropython
import sys
import time
import math
import random
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

# Create your objects here.
ev3 = EV3Brick()

FRONT_KEY = 'w'
BACK_KEY = 's'
LEFT_KEY = 'a'
RIGHT_KEY = 'd'
STOP_KEY = 'q'

turn = 1

obstacle_sensor = UltrasonicSensor(Port.S4)  # Ultrasonic sensor
color_sensor = ColorSensor(Port.S3)  # Color sensor
touch_sensor = TouchSensor(Port.S1)  # Touch sensor

robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=118)

print("Click Q to make it Autonomous")

# Write your program here.
ev3.speaker.beep()

def checkforobstacles():
    if obstacle_sensor.distance() < 200:
        robot.stop()
        ev3.screen.clear()
        ev3.screen.print("Object detected!")
        wait(1000)
        ev3.speaker.beep()
        wait(100)
        ev3.speaker.beep()
        wait(100)
        ev3.screen.clear()
        robot.drive_time(-300, 0, 1000)
    else:
        ev3.screen.print("No Obstacles Detected")
        wait(500)
        ev3.screen.clear()

def autonomous():
    print("Autonomous session is active")
    while True:
        ev3.screen.clear()
        ev3.screen.print("Autonomous")
        robot.drive_time(100, 0, 1000)
        if obstacle_sensor.distance() < 150:
            turn = random.randint(1, 2)
            print(color = color_sensor.color)
            if turn == 1:
                robot.turn(100)
                robot.drive_time(250, 0, 2000)
                robot.turn(100)
            if turn == 2:
                robot.turn(-100)
                robot.drive_time(250, 0, 2000)
                robot.turn(-100)


while True:
    char = sys.stdin.read(1)
    if char == FRONT_KEY:
        ev3.screen.print("Going Forawrds")
        robot.drive_time(200, 0, 1000)
        ev3.screen.clear()
        robot.stop()
        checkforobstacles()
    elif char == BACK_KEY:
        ev3.screen.print("Going Backwards")
        robot.drive_time(-200, 0, 1000)
        ev3.screen.clear()
        robot.stop()
        checkforobstacles()
    elif char == LEFT_KEY:
        ev3.screen.print("Turning Left")
        robot.turn(-50)
        ev3.screen.clear()
        robot.stop()
        checkforobstacles()
    elif char == RIGHT_KEY:
        ev3.screen.print("Turning Right")
        robot.turn(50)
        ev3.screen.clear()
        robot.stop()
        checkforobstacles()
    elif char == STOP_KEY:
        robot.stop()
        ev3.screen.print("Loading . . .")
        print("Loading . . .")
        autonomous()
        break
    elif touch_sensor.pressed():
        robot.stop()
        ev3.screen.print("Touch Sensor Pressed")
        break
    time.sleep(0.1)