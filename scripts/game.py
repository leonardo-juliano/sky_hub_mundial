import random
import pygame
from scripts.animatedbg import AnimatedBg
from scripts.obj import Obj
from scripts.scene import Scene
from scripts.settings import *
from scripts.text import Text
from scripts.fade import Fade

class Game(Scene):
    def __init__(self):
        super().__init__()
        self.bg = AnimatedBg("assets/menu/bg.jpg", (0,0), (0,-HEIGHT), self.all_sprites)

    def events(self, event):
        pass


    def update(self):
        self.bg.update()
        