import pygame

AMARELO = (255, 255, 0)
PRETO = (0, 0, 0)
pygame.init()

screen = pygame.display.set_mode((1024, 300), 0)
x = 0
y = 0
vel_x = 0.5
vel_y = 0.5
raio = 30
while True:
    # Calcular regras
    x += vel_x
    y += vel_y
    if x + raio > screen.get_width():
        vel_x = -0.5
    if x - raio < 0:
        vel_x = 0.5
    if y + raio > screen.get_height():
        vel_y = -0.5
    if y - raio < 0:
        vel_y = 0.5

    # Pintar
    screen.fill(PRETO)
    pygame.draw.circle(screen, AMARELO, (int(x), int(y)), raio, 0)
    pygame.display.update()

    # Capturar eventos
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()