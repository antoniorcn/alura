import pygame
import operator

pygame.init()
WIDTH = 800
HEIGHT = 400
PRETO = (0, 0, 0)
CENTRO_X_TELA = WIDTH // 2
CENTRO_Y_TELA = HEIGHT // 2
tela = pygame.display.set_mode((WIDTH, HEIGHT), 0)
naves = pygame.image.load("./images/naves.png").convert_alpha()


def circular(iterable):
    while iterable:
        for element in iterable:
            yield element


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.frames = circular([
            pygame.Rect((160, 104), (16, 16)),
            pygame.Rect((184, 104), (16, 16))
        ])
        self.velocity = [1, 1]
        self.image = naves.subsurface(next(self.frames))
        self.rect = pygame.Rect((CENTRO_X_TELA, 200),
                                self.image.get_size())

    def update(self):
        self.image = naves.subsurface(next(self.frames))

class Nave(pygame.sprite.Sprite):
    def __init__(self):
        r = pygame.Rect((160, 55), (16, 16))
        pygame.sprite.Sprite.__init__(self)
        self.velocity = [1, 0]
        self.image = naves.subsurface(r)
        self.rect = pygame.Rect((CENTRO_X_TELA, 300),
                                self.image.get_size())

    def update(self):
        self.rect.center = list(map(operator.add, self.rect.center, self.velocity))
        if self.rect.right > WIDTH:
            self.velocity[0] = -1
        if self.rect.left < 0:
            self.velocity[0] = 1

nave1 = Nave()
aliadas = pygame.sprite.Group()
aliadas.add(nave1)

inimigo1 = Enemy()
inimigos = pygame.sprite.Group()
inimigos.add(inimigo1)

while True:
    # calcular regras
    aliadas.update()
    inimigos.update()

    # pintar
    tela.fill(PRETO)
    aliadas.draw(tela)
    inimigos.draw(tela)
    pygame.display.update()

    # capturar eventos
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()
