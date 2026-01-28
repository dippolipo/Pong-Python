import pygame as pg
from pygame import Vector2
from scripts import globs, engine

class Paddle(engine.Sprite):
    def __init__(self, max_speed, pos, size, color):
        super().__init__(pos, size, color)
        self.h_pos = 216/2
        self.max_speed = max_speed

    def move(self, intensity): #intensity must be between -1 and 1
        self.rect += Vector2(0,1) * intensity * self.max_speed


class Ball(engine.Sprite):
    def __init__(self, max_speed, pos, radius, color):
        super().__init__(pos, (radius*2, radius*2), color)
        self.position = Vector2(384/2,216/2)
        self.velocity = Vector2(0,0)
