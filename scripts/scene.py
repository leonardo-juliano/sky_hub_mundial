import pygame
from scripts.fade import Fade
from scripts.settings import *

class Scene:

    def __init__(self):        
        self.display = pygame.display.get_surface()
        self.all_sprites = pygame.sprite.Group()
        self.active = True

    def events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                self.active = False

    def draw(self, screen):
        self.all_sprites.draw(self.display)

    def update(self):
        self.all_sprites.update()
