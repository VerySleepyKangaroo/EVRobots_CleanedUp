import pygame
import math as m
import time
from time import sleep

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("EV3 Robot Representation")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Robot settings
robot_width = 10
robot_height = 10
robot_x = 375
robot_y = 275
robot_speed = 0.05
direction = "STOP"  # Initial direction
robot_dir = 0
movement = "STOP"  # Initial movement

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Controls to change the direction
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        movement = "UP"
    elif keys[pygame.K_DOWN]:
        movement = "DOWN"
    else:
        movement = "STOP"
    if keys[pygame.K_LEFT]:
        direction = "LEFT"
    elif keys[pygame.K_RIGHT]:
        direction = "RIGHT"
    else:
        direction = "STOP"  # Stop moving if no key is pressed

    # Move the robot based on the direction
    if movement == "UP":
        robot_y -= m.sin(m.radians(robot_dir)) * robot_speed
        robot_x -= m.cos(m.radians(robot_dir)) * robot_speed
    elif movement == "DOWN":
        robot_y += m.sin(m.radians(robot_dir)) * robot_speed
        robot_x += m.cos(m.radians(robot_dir)) * robot_speed
    
    if direction == "LEFT":
        robot_dir -= 20
        print(robot_dir)
        print(robot_x, robot_y)
        sleep(0.1)
    elif direction == "RIGHT":
        robot_dir += 20
        print(robot_dir)
        print(robot_x, robot_y)
        sleep(0.1)

    # Update the screen
    screen.fill(WHITE)  # Background color
    pygame.draw.rect(screen, RED, (robot_x, robot_y, robot_width, robot_height))  # Draw the robot
    pygame.display.flip()

# Quit Pygame
pygame.quit()