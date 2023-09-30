import pygame
import sys
from scripts.animatedbg import AnimatedBg
from scripts.obj import Obj
from scripts.scene import Scene
from scripts.settings import *

class Menu(Scene):
    def __init__(self):
        super().__init__()
        pygame.font.init()
        self.bg = AnimatedBg("assets/menu/menu.jpg", (0,0), (0,-HEIGHT), self.all_sprites)
        # self.title = self.font.render("Press ENTER to play", True, "white")
        # self.title_rect = self.title.get_rect(center=(WIDTH / 2, HEIGHT / 2))
        
    def next_scene(self):
        self.active = False

    def quit_game(self):
        pygame.quit()
        sys.exit()

    def update(self):
        self.bg.update()
        return super().update()



    def events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.active = False
        if event.type == pygame.K_ESCAPE:
            if event.key == pygame.K_RETURN:
                self.quit_game()
    
