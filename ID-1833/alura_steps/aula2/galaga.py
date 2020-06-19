import pygame
from alura_steps.aula2.config import *
from alura_steps.aula2.nave import Nave

pygame.init()
tela = pygame.display.set_mode((WIDTH, HEIGHT), 0)
naves = pygame.image.load("./images/naves.png").convert_alpha()
r = pygame.Rect((160, 55), (40, 16))
nave1 = Nave(naves.subsurface(r))
aliadas = pygame.sprite.Group(nave1)


def game_loop():
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


if __name__ == "__main__":
    game_loop()

