import pygame, sys
from scripts.menu import Menu
from scripts.settings import *
from scripts.game import Game


class StartGame:
    def __init__(self):
        pygame.init()
        self.display = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Palmeiras não tem mundial")
        self.clock = pygame.time.Clock()

        self.scene = "menu"
        self.current_scene = Menu()

    def events(self):   
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            self.scene.events(event)

    def run(self):
        while True:
            if self.scene == "menu" and self.current_scene.active == False:
                self.scene = "game"
                self.current_scene = Game()
            elif self.scene == "game" and self.current_scene.active == False:
                self.scene = "menu"
                self.current_scene = Menu()

            self.events()
            self.display.fill(BG_COLOR)
            self.scene.draw()
            self.scene.update()
            pygame.display.update()
