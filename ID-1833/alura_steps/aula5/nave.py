import pygame
import operator
from alura_steps.aula5.utils import *


class Nave(pygame.sprite.Sprite):
    def __init__(self, spritesheet, sounds):
        pygame.sprite.Sprite.__init__(self)
        r = pygame.Rect((160, 55), (16, 16))
        self.spritesheet = spritesheet
        self.sounds = sounds
        self.velocity = [0, 0]
        self.image = self.spritesheet.subsurface(r)
        self.rect = pygame.Rect((CENTRO_X_TELA, 300),
                                self.image.get_size())

    def update(self):
        self.rect.center = list(map(operator.add, self.rect.center, self.velocity))
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

    def processar_eventos(self, evt):
        if evt.type == pygame.KEYDOWN:
            if evt.key == pygame.K_LEFT:
                self.velocity[0] = -1
            if evt.key == pygame.K_RIGHT:
                self.velocity[0] = 1
        if evt.type == pygame.KEYUP:
            if evt.key == pygame.K_LEFT:
                self.velocity[0] = 0
            if evt.key == pygame.K_RIGHT:
                self.velocity[0] = 0
