#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


ev3 = EV3Brick()
obstacle_sensor = UltrasonicSensor(Port.S4)  # Ultrasonic sensor
color_sensor = ColorSensor(Port.S3)  # Color sensor
touch_sensor = TouchSensor(Port.S1)  # Touch sensor

# Initialize motors and DriveBase
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

# Custom message based on sensor input
def display_message():
    ev3.screen.clear()
    ev3.screen.print("Sensor Triggered!")
    wait(1000)
    ev3.screen.clear()

# Main program loop
while True:
    # Begin driving forward
    robot.drive(200, 0)

    # Ultrasonic Sensor: Stop if an object is less than 10 cm away
    if obstacle_sensor.distance() < 100:
        robot.stop()
        ev3.screen.clear()
        ev3.screen.print("Object detected!")
        wait(1000)
        ev3.screen.clear()

    # Color Sensor: Detect colors and print to console
    detected_color = color_sensor.color()
    if detected_color == Color.RED:
        print("Red detected")
        display_message()
    elif detected_color == Color.BLUE:
        print("Blue detected")
        display_message()
    elif detected_color == Color.GREEN:
        print("Green detected")
        display_message()

    # Touch Sensor: Stop robot when pressed
    if touch_sensor.pressed():
        robot.stop()
        ev3.screen.print("Touch Sensor Pressed!")
        break