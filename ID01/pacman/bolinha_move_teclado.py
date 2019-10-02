import pygame
pygame.init()
tela = pygame.display.set_mode((800, 640), 0)
x = 50
y = 50
velX = 0
velY = 0
while True:
    # Calcular regras
    if x < 0 or x > 800:
        velX = velX * -1
    if y < 0 or y > 640:
        velY = velY * -1
    x = x + velX
    y = y + velY

    # Pintar
    tela.fill((0, 0, 0))
    pygame.draw.circle(tela, (255, 255, 0), (x, y), 20, 0)
    pygame.display.update()

    # Capturar eventos
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()
        if e.type == pygame.MOUSEMOTION:
            x, y = e.pos