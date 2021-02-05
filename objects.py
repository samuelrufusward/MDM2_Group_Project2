import random


class Car:

    def __init__(self, velocity, stop_distance, direction, sprite_dir, x_pos, y_pos):

        self.velocity = velocity
        self.stop_distance = stop_distance
        self.direction = direction
        self.sprite_dir = sprite_dir
        self.x_pos = x_pos
        self.y_pos = y_pos
