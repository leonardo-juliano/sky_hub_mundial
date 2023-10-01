import pygame
import random
from pygame.locals import *

class Plataform(pygame.sprite.Sprite):
    def __init__(self, x, y, static=False, image=None):
        super().__init__()
        if image is not None:
            self.image = pygame.image.load(image)
        else:
            self.image = pygame.Surface((100, 20))  
            self.image.fill((0, 255, 0))  
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.static = static  # Se for True, a plataforma é estática
        self.falling = not static  # Define se a plataforma está caindo ou não

    def update(self):
        if self.falling:
            self.rect.y += 2  # Plataforma cai
            if self.rect.top > 600:  # Se a plataforma cai abaixo da tela
                self.rect.y = random.randint(-30, -10)  # Recria a plataforma acima da tela
                self.rect.x = random.randint(0, 700)  
                self.falling = random.choice([True, False])  

platforms = pygame.sprite.Group()
platform_images = ["assets/menu/palataforma-01.png", "assets/menu/palataforma-02.png"]

for _ in range(10):
    x = random.randint(0, 700) 
    y = random.randint(100, 500)  
    is_static = random.choice([True, False])  
    image = random.choice(platform_images)  
    platform = Plataform(x, y, is_static, image)  
    platforms.add(platform)
    print("Plataformas geradas")