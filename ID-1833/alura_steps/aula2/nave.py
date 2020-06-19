import pygame
from alura_steps.aula2.config import *

class Nave(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
        self.velocity = [1, 1]
        self.image = img
        self.rect = pygame.Rect((CENTRO_X_TELA, CENTRO_Y_TELA),
                                self.image.get_size())

    def update(self):
        self.rect.center = list(map(sum, zip(self.rect.center, self.velocity)))
        if self.rect.right > WIDTH:
            self.velocity[0] = -1
        if self.rect.bottom > HEIGHT:
            self.velocity[1] = -1
        if self.rect.top < 0:
            self.velocity[1] = 1
        if self.rect.left < 0:
            self.velocity[0] = 1