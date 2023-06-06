import pygame
from pygame.locals import *
import random

# Shape parameters
size = width, height = (800, 800)
road_w = int(width / 1.6)
roadmark_w = int(width / 80)

# Location parameters
right_lane = width / 2 + road_w / 4
left_lane = width / 2 - road_w / 4

# Animation parameters
speed = 1

# Initialize the app
pygame.init()
running = True

# Set window size
screen = pygame.display.set_mode(size)
# Set window title
pygame.display.set_caption("Erman's car game")
# Set background color
screen.fill((60, 220, 0))
# Apply changes
pygame.display.update()

# Load player vehicle
car = pygame.image.load("car.png")
car_loc = car.get_rect()
car_loc.center = right_lane, height * 0.8

# Load enemy vehicle
car2 = pygame.image.load("otherCar.png")
car2_loc = car2.get_rect()
car2_loc.center = left_lane, height * 0.2

# Road markings
roadmarks = []
for i in range(height // 100):
    roadmarks.append([width / 2, i * 100])

counter = 0
# Game loop
while running:
    counter += 1

    # Increase game difficulty overtime
    if counter == 5000:
        speed += 0.15
        counter = 0
        print("level up", speed)

    # Animate enemy vehicle
    car2_loc[1] += speed
    if car2_loc[1] > height:
        # Randomly select lane
        if random.randint(0, 1) == 0:
            car2_loc.center = right_lane, -200
        else:
            car2_loc.center = left_lane, -200

    # End game logic
    if car_loc[0] == car2_loc[0] and car2_loc[1] > car_loc[1] - 250:
        print("GAME OVER! YOU LOST!")
        break

    # Event listeners
    for event in pygame.event.get():
        if event.type == QUIT:
            # Collapse the app
            running = False
        if event.type == KEYDOWN:
            # Move user car to the left
            if event.key in [K_a, K_LEFT]:
                car_loc = car_loc.move([-int(road_w / 2), 0])
            # Move user car to the right
            if event.key in [K_d, K_RIGHT]:
                car_loc = car_loc.move([int(road_w / 2), 0])

    # Draw road
    pygame.draw.rect(screen, (50, 50, 50), (width / 2 - road_w / 2, 0, road_w, height))

    # Update road markings
    for mark in roadmarks:
        mark[1] += speed
        if mark[1] > height:
            mark[1] = -100

    # Draw center line
    for mark in roadmarks:
        pygame.draw.rect(screen, (255, 240, 60), (mark[0] - roadmark_w / 2, mark[1], roadmark_w, 100))

    # Draw left road marking
    pygame.draw.rect(screen, (255, 255, 255),
                     (width / 2 - road_w / 2 + roadmark_w * 2, 0, roadmark_w, height))
    # Draw right road marking
    pygame.draw.rect(screen, (255, 255, 255),
                     (width / 2 + road_w / 2 - roadmark_w * 3, 0, roadmark_w, height))

    # Place car images on the screen
    screen.blit(car, car_loc)
    screen.blit(car2, car2_loc)
    # Apply changes
    pygame.display.update()

# Collapse application window
pygame.quit()
