import random
import pygame
from scripts.animatedbg import AnimatedBg
from scripts.obj import Obj
from scripts.scene import Scene
from scripts.settings import *
from scripts.text import Text
from scripts.fade import Fade
from scripts.player import Player  # Importe a classe Player

class Game(Scene):
    def __init__(self):
        super().__init__()
        self.bg = AnimatedBg("assets/menu/bg.jpg", (0,0), (0,-HEIGHT), self.all_sprites)
        # Crie uma instância do jogador
        self.player = Player()

    def events(self, event):
        pass

    def update(self):
        self.bg.update()

        # Atualize o jogador
        self.player.update()

    def draw(self, screen):
        super().draw(screen)  # Certifique-se de chamar o método pai para desenhar o resto do conteúdo
        # Desenhe o jogador
        self.player.draw(screen)
