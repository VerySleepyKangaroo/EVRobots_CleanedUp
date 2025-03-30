import pygame
import math as m

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

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Controls to change the direction
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        direction = "UP"
    elif keys[pygame.K_DOWN]:
        direction = "DOWN"
    elif keys[pygame.K_LEFT]:
        direction = "LEFT"
    elif keys[pygame.K_RIGHT]:
        direction = "RIGHT"
    else:
        direction = "STOP"

    # Move the robot based on the direction
    if direction == "UP":
        robot_y -= robot_speed
        robot_x -= m.sin(robot_dir) * robot_speed
    elif direction == "DOWN":
        robot_y += robot_speed
        robot_x += m.sin(robot_dir) * robot_speed
    elif direction == "LEFT":
        robot_dir -= 90
        print(robot_dir)
        sleep(0.1)
        
    elif direction == "RIGHT":
        robot_dir += 90
        print(robot_dir)
        sleep(0.1)

    # Update the screen
    screen.fill(WHITE)  # Background color
    pygame.draw.rect(screen, RED, (robot_x, robot_y, robot_width, robot_height))  # Draw the robot
    pygame.display.flip()

# Quit Pygame
pygame.quit()