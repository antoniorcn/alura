import pygame
from pygame.rect import Rect

pygame.init()


cenario = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

tela = pygame.display.set_mode((800, 640), pygame.FULLSCREEN, 32, 1)
# tela2 = pygame.display.set_mode((800, 640), 0, 32, 2)

PPC = (640//16) - 2

personagem = [1, 1]

while True:
    # Calcular regras
    if 0 > personagem[0] > 16 and 0 > personagem[1] > 16:
        pass    # Pode mover

    # Pintar
    for linha in range(len(cenario)):
        for coluna in range(len(cenario[linha])):
            cor = (0, 0, 255)
            if cenario[linha][coluna] == 0:
                cor = (0, 0, 0)
            pygame.draw.rect(tela, cor, Rect((coluna*PPC, linha*PPC), (PPC, PPC)), 0)
    px = personagem[0] * PPC + (PPC//2)
    py = personagem[1] * PPC + (PPC//2)
    pygame.draw.circle(tela, (255, 255, 0), (px, py), PPC//2, 0)
    pygame.display.update()

    # Capturar eventos
    for e in pygame.event.get():
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_DOWN:
                personagem[1] += 1
            elif e.key == pygame.K_UP:
                personagem[1] -= 1
            elif e.key == pygame.K_LEFT:
                personagem[0] -= 1
            elif e.key == pygame.K_RIGHT:
                personagem[0] += 1
        if e.type == pygame.QUIT:
            exit()