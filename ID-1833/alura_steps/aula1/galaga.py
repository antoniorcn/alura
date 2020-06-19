import pygame

pygame.init()
WIDTH = 800
HEIGHT = 400
PRETO = (0, 0, 0)
CENTRO_X_TELA = WIDTH // 2
CENTRO_Y_TELA = HEIGHT // 2

tela = pygame.display.set_mode((WIDTH, HEIGHT), 0)

naves = pygame.image.load("./images/naves.png").convert_alpha()
r = pygame.Rect((160, 55), (40, 16))
nave1 = naves.subsurface(r)

while True:
    # calcular regras

    # pintar
    tela.fill(PRETO)
    tela.blit(nave1, (CENTRO_X_TELA, CENTRO_Y_TELA))
    pygame.display.update()

    # capturar eventos
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()
