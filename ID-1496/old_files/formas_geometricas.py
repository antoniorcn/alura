import pygame
from pygame.rect import Rect
pygame.init()
tela = pygame.display.set_mode((800, 600), 0)
while True:
    # Pintar na tela um ponto
    tela.set_at((400, 300), (255, 255, 0))
    # Desenhar uma Linha
    pygame.draw.line(tela, (255, 255, 0), (200, 150), (600, 450), 3)
    # Desenhar um Circulo
    pygame.draw.circle(tela, (255, 255, 0), (400, 300), 50, 3)
    # Desenhar um Retangulo
    pygame.draw.rect(tela, (255, 255, 0), Rect((350, 250), (100, 100)), 3)
    pygame.display.update()
    # Capturar eventos
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()
