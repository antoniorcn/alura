import pygame
from abc import ABCMeta, abstractmethod

pygame.init()
WIDTH = 800
HEIGHT = 400
PRETO = (0, 0, 0)
CENTRO_X_TELA = WIDTH // 2
CENTRO_Y_TELA = HEIGHT // 2
tela = pygame.display.set_mode((WIDTH, HEIGHT), 0)
naves = pygame.image.load("./images/naves.png").convert_alpha()


class AbstractMove(metaclass=ABCMeta):
    def __init__(self, parent_sprite=None):
        self.parent_sprite = parent_sprite

    @abstractmethod
    def execute(self):
        pass


class LinearMove(AbstractMove):
    def execute(self):
        self.parent_sprite.rect.center = \
            list(map(sum, zip(self.parent_sprite.rect.center, self.parent_sprite.velocity)))


class Nave(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.moves = []
        r = pygame.Rect((160, 55), (40, 16))
        self.velocity = [1, 1]
        self.image = naves.subsurface(r)
        self.rect = pygame.Rect((CENTRO_X_TELA, CENTRO_Y_TELA),
                                self.image.get_size())

    def append_move(self, move):
        self.moves.append(move)
        move.parent_sprite = self

    def update(self):
        for move in self.moves:
            move.execute()

        if self.rect.right > WIDTH:
            self.velocity[0] = -1
        if self.rect.bottom > HEIGHT:
            self.velocity[1] = -1
        if self.rect.top < 0:
            self.velocity[1] = 1
        if self.rect.left < 0:
            self.velocity[0] = 1


nave1 = Nave()
nave1.append_move(LinearMove())

aliadas = pygame.sprite.Group()
aliadas.add(nave1)

while True:
    # calcular regras
    aliadas.update()

    # pintar
    tela.fill(PRETO)
    aliadas.draw(tela)
    pygame.display.update()

    # capturar eventos
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()
