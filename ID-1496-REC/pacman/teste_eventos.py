import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600), 0)

while True:

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()
        if e.type == pygame.KEYDOWN:
            print(e.key)
