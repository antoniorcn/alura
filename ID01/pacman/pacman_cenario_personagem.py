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

tela = pygame.display.set_mode((800, 640), 0)
# tela2 = pygame.display.set_mode((800, 640), 0, 32, 2)

PPC = (640//16) - 2
personagem = [1, 1]

while True:
    # Calcular regras

    # Pintar
    for linha in range(len(cenario)):
        for coluna in range(len(cenario[linha])):
            cor = (0, 0, 255)
            if cenario[linha][coluna] == 0:
                cor = (0, 0, 0)
            pygame.draw.rect(tela, cor, Rect((coluna*PPC, linha*PPC), (PPC, PPC)), 0)

    # Desenhar o personagem
    px = personagem[0] * PPC
    py = personagem[1] * PPC
    pygame.draw.circle(tela, (255, 255, 0), (px + (PPC//2), py + (PPC//2)), PPC//2, 0)

    # Desenha o recorte da boca
    polygon = [(px + (PPC//2), py + (PPC//2)),
               (px + PPC, py + (PPC//2)),
               (px + PPC, py)]
    pygame.draw.polygon(tela, (0, 0, 0), polygon, 0)

    # Desenha o olho
    pygame.draw.circle(tela, (0, 0, 0), (px + int(PPC // 1.7), py + int(PPC / 5)), PPC // 10, 0)

    pygame.display.update()

    # Capturar eventos
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()