#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


ev3 = EV3Brick()

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

robot.drive_time(200, 0, 2000) 
ev3.speaker.beep()

robot.drive_time(-200, 0, 2000)  
ev3.speaker.beep()
print("moved backwards for 2 seconds")

robot.turn(-90)
ev3.speaker.beep()
print("turned left")

robot.turn(90)
ev3.speaker.beep()
print("turned right")

robot.turn(90)
robot.drive_time(200, 0, 2000)
ev3.speaker.beep()

robot.turn(90)
robot.drive_time(200, 0, 2000)
ev3.speaker.beep()

robot.turn(90)
robot.drive_time(200, 0, 2000)
ev3.speaker.beep()

robot.turn(90)
robot.drive_time(200, 0, 2000)
ev3.speaker.beep()

print("created a square")

robot.turn(90)
robot.drive_time(200, 0, 2000)
ev3.speaker.beep()

robot.turn(90)
robot.drive_time(200, 0, 2000)
ev3.speaker.beep()

robot.turn(90)
robot.drive_time(200, 0, 2000)
ev3.speaker.beep()

robot.turn(90)
robot.drive_time(200, 0, 2000)
ev3.speaker.beep()

robot.turn(-90)
robot.drive_time(200, 0, 2000)
ev3.speaker.beep()

robot.turn(-90)
robot.drive_time(200, 0, 2000)
ev3.speaker.beep()

robot.turn(-90)
robot.drive_time(200, 0, 2000)
ev3.speaker.beep()

print("created an eight-figure pattern")