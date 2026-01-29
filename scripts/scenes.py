from pygame.display import toggle_fullscreen

from scripts import engine, globs, entities
from scripts.engine import SceneManager as SM
import pygame as pg
from pygame import Vector2

from scripts.globs import SCREENSIZE


class Level(engine.Scene):
    def __init__(self):
        super().__init__()
        paddle_h = 40
        paddle_w = 10
        ball_r = 3
        self.p1 = entities.Paddle(5, (10, (SCREENSIZE.y - paddle_h)/2), (paddle_w, paddle_h), pg.Color("white"))
        self.p2 = entities.Paddle(64, (SCREENSIZE.x - 10 - paddle_w, (SCREENSIZE.y - paddle_h)/2), (paddle_w, paddle_h), pg.Color("white"))
        self.ball = entities.Ball(32, (SCREENSIZE.x/2 - ball_r, SCREENSIZE.y/2 - ball_r), ball_r, pg.Color("white"))
        self.entities = pg.sprite.Group(self.p1, self.p2, self.ball)
        # renderer
        self.background = pg.Surface(globs.SCREENSIZE).convert_alpha()
        self.background.fill("red")
        s_n = 15
        s_s = 5
        s_h = (globs.SCREENSIZE.y - s_s * (s_n + 1)) / s_n
        s_w = 4
        for i in range(s_n):
            pg.draw.rect(self.background, pg.Color("white"), pg.Rect((globs.SCREENSIZE.x - s_w) / 2, 0 + s_s + i * (s_h + s_s), s_w, s_h))

    def get_keys(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_ESCAPE]:
            engine.running = False

        if keys[pg.K_w]:
            self.p1.move(-1)
        if keys[pg.K_s]:
            self.p1.move(1)


    def tick(self):
        self.get_keys()
        self.entities.update()
        self.ball_movement()
        self.cpu_movement()

    def cpu_movement(self):
        self.p2.rect.y = self.ball.rect.y - (self.p2.size.y + self.ball.size.y) / 2

    def ball_movement(self):

        if self.ball.rect.x < globs.SCREENSIZE.x / 2:
            if engine.Collision.two_segment(self.ball.rect.center, self.ball.rect.center + self.ball.velocity, self.p1.rect.topright, self.p1.rect.bottomright):
              self.ball.velocity.x *= -1
        else:
            if engine.Collision.two_segment(self.ball.rect.center, self.ball.rect.center + self.ball.velocity, self.p2.rect.topleft, self.p2.rect.bottomleft):
                self.ball.velocity.x *= -1
        self.ball.rect.center += self.ball.velocity

    def draw(self):
        engine.screen.blit(self.background, (0, 0))
        self.entities.draw(engine.screen)
        self.get_events()
