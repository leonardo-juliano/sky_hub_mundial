import pygame
from pygame.locals import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/menu/player-225.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = 1280/2
        self.rect.bottom = 720
        self.speed_x = 0

    def move(self, keys):
        self.speed_x = 0
        if keys[K_LEFT]:
            self.speed_x = -5
        if keys[K_RIGHT]:
            self.speed_x = 5

    def update(self):
        self.rect.x += self.speed_x
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > 800:
            self.rect.right = 800

    def draw(self, screen):
        screen.blit(self.image, self.rect)
