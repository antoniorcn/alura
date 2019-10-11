import pygame
pygame.init()
screen = pygame.display.set_mode((800, 600), 0)
AMARELO = (255, 255, 0)
PRETO = (0, 0, 0)
AZUL = (0, 0, 0)
TAMANHO = 36


class Pacman:
    def __init__(self, tamanho):
        self.x = 400  # X do canto superior esquerdo onde será desenhado
        self.y = 300  # Y do canto superior esquerdo onde será desenhado
        self.tamanho = tamanho

    def pintar(self, tela):
        # Desenha o pacman
        corpo_x = self.x + (self.tamanho // 2)
        corpo_y = self.y + (self.tamanho // 2)
        corpo_raio = self.tamanho // 2
        pygame.draw.circle(tela, AMARELO, (corpo_x, corpo_y), corpo_raio, 0)

        # Desenha o recorte da boca
        boca_labio_inferior = (self.x + self.tamanho, corpo_y)
        boca_fundo = (corpo_x, corpo_y)
        boca_labio_superior = (self.x + self.tamanho, self.y)

        polygon = [boca_fundo, boca_labio_inferior, boca_labio_superior]
        pygame.draw.polygon(tela, PRETO, polygon, 0)

        # Desenha o olho
        olho_x = self.x + round(self.tamanho // 1.7)
        olho_y = self.y + round(self.tamanho / 5)
        olho_raio = self.tamanho // 10
        pygame.draw.circle(tela, PRETO, (olho_x, olho_y), olho_raio, 0)


if __name__ == "__main__":
    pacman = Pacman(TAMANHO)
    while True:
        # Pintar a tela
        pacman.pintar(screen)
        pygame.display.update()

        # Capturar eventos
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                exit()


