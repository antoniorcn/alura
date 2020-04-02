import pygame
pygame.init()
screen = pygame.display.set_mode((800, 600), 0)
AMARELO = (255, 255, 0)
PRETO = (0, 0, 0)
AZUL = (0, 0, 0)
TAMANHO = 36
VELOCIDADE = 0.1


class Pacman:
    def __init__(self, tamanho):
        self.coluna = 1.0  # Coluna onde será desenhado
        self.linha = 1.0  # Linha onde será desenhado
        self.tamanho = tamanho
        self.velx = VELOCIDADE
        self.vely = VELOCIDADE

    def pintar(self, tela):
        # Desenha o pacman
        px = int(self.coluna * self.tamanho)
        py = int(self.linha * self.tamanho)
        corpo_x = px + (self.tamanho // 2)
        corpo_y = py + (self.tamanho // 2)
        corpo_raio = self.tamanho // 2
        pygame.draw.circle(tela, AMARELO, (corpo_x, corpo_y), corpo_raio, 0)

        # Desenha o recorte da boca
        boca_labio_inferior = (px + self.tamanho, corpo_y)
        boca_fundo = (corpo_x, corpo_y)
        boca_labio_superior = (px + self.tamanho, py)

        polygon = [boca_fundo, boca_labio_inferior, boca_labio_superior]
        pygame.draw.polygon(tela, PRETO, polygon, 0)

        # Desenha o olho
        olho_x = px + round(self.tamanho // 1.7)
        olho_y = py + round(self.tamanho / 5)
        olho_raio = self.tamanho // 10
        pygame.draw.circle(tela, PRETO, (olho_x, olho_y), olho_raio, 0)

    def calcular_regras(self):
        px = self.coluna * self.tamanho
        py = self.linha * self.tamanho
        if px < 0 or px + self.tamanho > 800:
            self.velx = self.velx * -1
        if py < 0 or py + self.tamanho > 600:
            self.vely = self.vely * -1
        self.coluna = self.coluna + self.velx
        self.linha = self.linha + self.vely


if __name__ == "__main__":
    pacman = Pacman(TAMANHO)
    while True:
        # Calcular regras
        pacman.calcular_regras()

        # Pintar a tela
        screen.fill(PRETO)
        pacman.pintar(screen)
        pygame.display.update()

        # Capturar eventos
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                exit()
