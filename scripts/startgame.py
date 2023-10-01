import pygame, sys
from scripts.menu import Menu
from scripts.settings import *
from scripts.game import Game
from scripts.player import Player
from scripts.plataform import Plataform
import random

class StartGame:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Palmeiras não tem mundial")
        self.display = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Palmeiras não tem mundial")
        self.clock = pygame.time.Clock()

        self.scene = "menu"
        self.current_scene = Menu()

        # Crie o jogador e as plataformas aqui, uma única vez
        self.player = Player()
        self.platforms = pygame.sprite.Group()
        for _ in range(10):
            x = random.randint(0, WIDTH - 100)  # Ajuste os valores de acordo com a largura da tela
            y = random.randint(100, HEIGHT - 20)  # Ajuste os valores de acordo com a altura da tela
            is_static = random.choice([True, False])  # Decide se a plataforma será estática ou móvel
            platform = Plataform(x, y, is_static)
            self.platforms.add(platform)

    def events(self):   
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            self.current_scene.events(event)

    def run(self):
        while True:
            if self.scene == "menu" and not self.current_scene.active:
                self.scene = "game"
                self.current_scene = Game()
            elif self.scene == "game" and not self.current_scene.active:
                self.scene = "menu"
                self.current_scene = Menu()

            self.events()
            keys = pygame.key.get_pressed()

            # Atualize o jogador
            self.player.move(keys)
            self.player.update()

            # Atualize as plataformas
            self.platforms.update()

            self.display.fill(BG_COLOR)
            self.current_scene.draw(self.display)  # Apenas passe o objeto 'display' como argumento

            # Desenhe o jogador e as plataformas
            self.player.draw(self.display)
            self.platforms.draw(self.display)

            pygame.display.update()
            self.clock.tick(60)
