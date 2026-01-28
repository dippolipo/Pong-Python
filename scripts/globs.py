from scripts import engine
import pygame as pg

SCREENSIZE = pg.Vector2(384, 216)
engine.pygame_init("Snake", None, SCREENSIZE)
fullscreen = True