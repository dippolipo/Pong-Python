from pygame import Vector2
from scripts import globs

class Paddle:
    def __init__(self, max_speed):
        self.h_pos = 216/2
        self.max_speed = max_speed
        self.size = Vector2(6, 48)
        self.hitbox_w = 4


class Ball:
    def __init__(self):
        self.position = Vector2(384/2,216/2)
        self.velocity = Vector2(0,0)
