import pygame
from alura_steps.aula5.utils import *
import operator
import math
from random import randint, choice


class Enemy(pygame.sprite.Sprite):
    def __init__(self, spritesheet, sounds):
        pygame.sprite.Sprite.__init__(self)
        self.startpoint = [0, 0]
        self.endpoint = [0, 0]
        self.velocity = [0.0, 0.0]
        self.image = pygame.Surface((16, 16))
        self.define_target()
        self.estado_time = 100
        self.spritesheet = spritesheet
        self.sounds = sounds
        self.frames_normal = circular([
            pygame.Rect((160, 104), (16, 16)),
            pygame.Rect((184, 104), (16, 16))
        ])
        self.frames_explosao = circular([
            pygame.Rect((198, 190), (32, 32)),
            pygame.Rect((224, 190), (32, 32)),
            pygame.Rect((248, 190), (32, 32)),
            pygame.Rect((280, 190), (32, 32)),
            pygame.Rect((320, 190), (32, 32)),
            pygame.Rect((280, 190), (32, 32)),
            pygame.Rect((248, 190), (32, 32)),
            pygame.Rect((224, 190), (32, 32)),
            pygame.Rect((196, 190), (32, 32))
        ])
        self.estado = 0
        self.define_frame()
        self.rect = pygame.Rect(self.startpoint,
                                self.image.get_size())
        self.pos = self.rect.center
        self.update()

    def define_target(self):
        self.startpoint = [choice([1, 770]), randint(10, HEIGHT-150)]
        self.endpoint = [randint(10, WIDTH-10), randint(10, HEIGHT-70)]
        dx = self.startpoint[0] - self.endpoint[0]
        dy = self.startpoint[1] - self.endpoint[1]
        movements = math.sqrt(dx ** 2 + dy ** 2)
        speed = 0.1
        self.velocity = [- dx / movements * speed, - dy / movements * speed]

    def define_frame(self):
        if self.estado == 0:
            self.image = self.spritesheet.subsurface(next(self.frames_normal))
        else:
            self.image = self.spritesheet.subsurface(next(self.frames_explosao))

    def update(self):
        self.define_frame()
        if self.estado == 0:
            if self.rect.bottom > HEIGHT or self.rect.top < 0 or self.rect.left < 0 or self.rect.right > WIDTH:
                self.kill()
            self.pos = list(map(operator.add, self.pos, self.velocity))
        else:
            self.estado_time -= 1
            if self.estado_time <= 0:
                self.kill()
        self.rect.center = self.pos

    def matou(self):
        self.estado = 1
        self.sounds['tiro'].stop()
        self.sounds['kill_enemy'].stop()
        self.sounds['kill_enemy'].play()
