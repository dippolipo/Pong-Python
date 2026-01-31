import pygame as pg
from scripts import scenes, engine, globs

engine.SceneManager.reset(scenes.Level)
game = engine.Game(15, globs.fullscreen)
game.loop()