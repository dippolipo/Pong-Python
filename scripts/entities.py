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
        self.radius = radius
        self.position = Vector2(384/2,216/2)
        self.velocity = Vector2(math.cos(initial_degree) * random.choice((-1, 1)), math.sin(initial_degree))*2

    def check_collision(self, a, b):
        a, b = engine.convert_to_vector2(a, b)
        normal = self.velocity.normalize()
        v_ort = Vector2(normal.y * -1, normal.x) * self.radius
        ray1 = engine.Collision.two_segment(v_ort + self.rect.center, v_ort + self.rect.center + self.velocity, a, b)
        v_ort *= -1
        ray2 = engine.Collision.two_segment(v_ort + self.rect.center, v_ort + self.rect.center + self.velocity, a, b)
        if (not ray1) or  (not ray2):
            self.rect.center += self.velocity
            #self.image.fill(pg.Color("green"))
        # debug start
        engine.debug_screen.fill(pg.Color(0,0,0,0))
        pg.draw.line(engine.debug_screen, pg.Color("green"), a, b)
        pg.draw.line(engine.debug_screen, pg.Color("red"), self.rect.center,self.rect.center)
        pg.draw.line(engine.debug_screen, pg.Color("black"), v_ort + self.rect.center, v_ort + self.rect.center + self.velocity)
        pg.draw.line(engine.debug_screen, pg.Color("black"), v_ort * -1  + self.rect.center, v_ort * -1 + self.rect.center + self.velocity)
        # debug
        """if ray1.length() < ray2.length():
                self.rect.center += ray1                
            else:                                       
                self.rect.center += ray2"""