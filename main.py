import pygame
from objects import *
import random
pygame.init()

# display screen dimensions
screenWidth = 1400
screenHeight = 600

# Initialises game window
win = pygame.display.set_mode((screenWidth, screenHeight))

# Sets display window caption
pygame.display.set_caption("Tunnel Sim")

directions = [-1, 1]


def GenerateVehicle():
    # generates random selector for car
    car_no = random.randint(1, 5)
    car_obj = object

    if car_no == 1:

        velocity = 25
        stop_distance = 15
        direction = random.choice(directions)
        if direction == 1:
            sprite_dir = "sprites/car1right.png"
            x_pos = 0
            y_pos = 275
        else:
            sprite_dir = "sprites/car1left.png"
            x_pos = screenWidth - 64
            y_pos = 325

        car_obj = Car(velocity, stop_distance, direction, sprite_dir, x_pos, y_pos)

    elif car_no == 2:

        velocity = 20
        stop_distance = 15
        direction = random.choice(directions)
        if direction == 1:
            sprite_dir = "sprites/car2right.png"
            x_pos = 0
            y_pos = 275
        else:
            sprite_dir = "sprites/car2left.png"
            x_pos = screenWidth - 64
            y_pos = 325

        car_obj = Car(velocity, stop_distance, direction, sprite_dir, x_pos, y_pos)

    elif car_no == 3:

        velocity = 17
        stop_distance = 15
        direction = random.choice(directions)
        if direction == 1:
            sprite_dir = "sprites/car3right.png"
            x_pos = 0
            y_pos = 275
        else:
            sprite_dir = "sprites/car3left.png"
            x_pos = screenWidth - 64
            y_pos = 325

        car_obj = Car(velocity, stop_distance, direction, sprite_dir, x_pos, y_pos)

    elif car_no == 4:

        velocity = 16
        stop_distance = 15
        direction = random.choice(directions)
        if direction == 1:
            sprite_dir = "sprites/car4right.png"
            x_pos = 0
            y_pos = 275
        else:
            sprite_dir = "sprites/car4left.png"
            x_pos = screenWidth - 64
            y_pos = 325

        car_obj = Car(velocity, stop_distance, direction, sprite_dir, x_pos, y_pos)

    elif car_no == 5:

        velocity = 13
        stop_distance = 15
        direction = random.choice(directions)
        if direction == 1:
            sprite_dir = "sprites/car5right.png"
            x_pos = 0
            y_pos = 275
        else:
            sprite_dir = "sprites/car5left.png"
            x_pos = screenWidth - 64
            y_pos = 325

        car_obj = Car(velocity, stop_distance, direction, sprite_dir, x_pos, y_pos)

    return car_obj


def RedrawWindow(vehicles):

    # Draws background
    pygame.draw.rect(win, (255, 255, 255), (0, 0, screenWidth, screenHeight))

    for vehicle in vehicles:
        # Loads sprite image using directory
        sprite = pygame.image.load(vehicle.sprite_dir)
        # Draws sprite using image an co-ordinates from the dictionary
        win.blit(sprite, (vehicle.x_pos, vehicle.y_pos))

    pygame.display.update()


def Main():

    vehicles = []
    car1 = GenerateVehicle()
    vehicles.append(car1)

    RedrawWindow(vehicles)

    # main loop
    run = True
    while run:

        pygame.time.delay(1000)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for vehicle in vehicles:

            vehicle.x_pos += vehicle.direction * vehicle.velocity

        # 15% chance of generating new random vehicle
        if random.randint(1, 100) > 85:

            new_car = GenerateVehicle()
            vehicles.append(new_car)

        RedrawWindow(vehicles)

    pygame.quit()

Main()