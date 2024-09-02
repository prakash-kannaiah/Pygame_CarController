# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 09:24:53 2024

@author: edute
"""

import pygame
import sys

# Initialize pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Car Control")

# Initialize car speed and steering angle
car_speed = 0
steering_angle = 0
angle_change_rate = 1  # Change rate for steering angle

try:
    # Main game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Get the state of all keys
        keys = pygame.key.get_pressed()

        # Handle speed control
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            car_speed = 5
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            car_speed = -5
        else:
            car_speed = 0

        # Handle steering angle control
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            steering_angle += angle_change_rate
            if steering_angle > 30:
                steering_angle = 30
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            steering_angle -= angle_change_rate
            if steering_angle < -30:
                steering_angle = -30
        else:
            # Gradually return steering angle to 0 if no key is pressed
            if steering_angle > 0:
                steering_angle -= angle_change_rate
                if steering_angle < 0:
                    steering_angle = 0
            elif steering_angle < 0:
                steering_angle += angle_change_rate
                if steering_angle > 0:
                    steering_angle = 0

        # Clear screen
        screen.fill((0, 0, 0))

        # Print the speed and steering angle
        print(f"Car Speed: {car_speed}")
        print(f"Steering Angle: {steering_angle}")

        # Update display
        pygame.display.flip()

        # Cap the frame rate
        pygame.time.Clock().tick(30)

except KeyboardInterrupt:
    # Handle Ctrl+C gracefully
    print("\nProgram interrupted by user. Exiting...")

finally:
    # Quit pygame
    pygame.quit()
    sys.exit()
