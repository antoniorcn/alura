import pygame
import operator
from alura_steps.aula5.utils import *


class Tiro(pygame.sprite.Sprite):
    def __init__(self, spritesheet, sounds, pos):
        pygame.sprite.Sprite.__init__(self)
        self.frames = circular([
            pygame.Rect((365, 195), (3, 8))])
        self.velocity = [0, -1]
        self.spritesheet = spritesheet
        self.image = self.spritesheet.subsurface(next(self.frames))
        self.rect = pygame.Rect(pos,
                                self.image.get_size())
        sounds['tiro'].stop()
        sounds['tiro'].play()

    def update(self):
        self.image = self.spritesheet.subsurface(next(self.frames))
        self.rect.center = list(map(operator.add, self.rect.center, self.velocity))
        if self.rect.left < 0:
            self.kill()
