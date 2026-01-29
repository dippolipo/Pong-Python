import math

import pygame as pg
from pygame import Vector2
from scripts import globs, engine
import random

class Paddle(engine.Sprite):
    def __init__(self, max_speed, pos, size, color):
        super().__init__(pos, size, color)
        self.h_pos = 216/2
        self.max_speed = max_speed

    def move(self, intensity): #intensity must be between -1 and 1
        self.rect.center += Vector2(0,1) * intensity * self.max_speed
        if self.rect.y < 0:
            self.rect.y = 0
        elif self.rect.y > globs.SCREENSIZE.y - self.size.y:
            self.rect.y = globs.SCREENSIZE.y - self.size.y


class Ball(engine.Sprite):
    def __init__(self, max_speed, pos, radius, color):
        super().__init__(pos, (radius*2, radius*2))
        pg.draw.circle(self.image, color, (radius, radius), radius)
        ran = 0 # random.randint(-10, 10)
        initial_degree = math.radians(ran)
        print(ran)
        self.position = Vector2(384/2,216/2)
        self.velocity = Vector2(math.cos(initial_degree) * random.choice((-1, 1)), math.sin(initial_degree)) * 150
        print(self.velocity)

    def check_paddle_collision(self, a, b):
        pass


