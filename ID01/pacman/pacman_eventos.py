import pygame
pygame.init()
screen = pygame.display.set_mode((800, 600), 0)
AMARELO = (255, 255, 0)
PRETO = (0, 0, 0)
ACERELERACAO = 1


class Pacman:
    def __init__(self):
        self.px = 400.0
        self.py = 300.0
        self.velx = 0.0
        self.vely = 0.0

    def calcular_regras(self):
        if self.px < 0 or self.px > 800:
            self.velx = self.velx * -1
        if self.py < 0 or self.py > 640:
            self.vely = self.vely * -1
        self.px = self.px + self.velx
        self.py = self.py + self.vely

    def pintar(self, tela):
        # Limpar a tela
        tela.fill(PRETO)

        # Desenha o pacman
        tamanho = 64
        corpo_x = round(self.px) + (tamanho // 2)
        corpo_y = round(self.py) + (tamanho // 2)
        corpo_raio = tamanho // 2
        pygame.draw.circle(tela, AMARELO, (corpo_x, corpo_y), corpo_raio, 0)

        # Desenha o recorte da boca
        boca_labio_inferior = (self.px + tamanho, corpo_y)
        boca_fundo = (corpo_x, corpo_y)
        boca_labio_superior = (self.px + tamanho, self.py)

        polygon = [boca_fundo, boca_labio_inferior, boca_labio_superior]
        pygame.draw.polygon(tela, PRETO, polygon, 0)

        # Desenha o olho
        olho_x = round(self.px + tamanho // 1.7)
        olho_y = round(self.py + tamanho / 5)
        olho_raio = tamanho // 10
        pygame.draw.circle(tela, PRETO, (olho_x, olho_y), olho_raio, 0)

        # Atualizar a tela
        pygame.display.update()

    def processar_eventos(self, eventos):
        for e in eventos:
            if e.type == pygame.QUIT:
                exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_DOWN:
                    self.vely = ACERELERACAO
                elif e.key == pygame.K_UP:
                    self.vely = -ACERELERACAO
                elif e.key == pygame.K_LEFT:
                    self.velx = -ACERELERACAO
                elif e.key == pygame.K_RIGHT:
                    self.velx = ACERELERACAO
            if e.type == pygame.KEYUP:
                if e.key == pygame.K_DOWN:
                    self.vely = 0.0
                elif e.key == pygame.K_UP:
                    self.vely = 0.0
                elif e.key == pygame.K_LEFT:
                    self.velx = 0.0
                elif e.key == pygame.K_RIGHT:
                    self.velx = 0.0


if __name__ == "__main__":
    pacman = Pacman()
    # Loop do Jogo
    while True:
        # Calcular as regras
        pacman.calcular_regras()

        # Pintar a tela
        pacman.pintar(screen)

        # Capturar eventos
        ev = pygame.event.get()
        pacman.processar_eventos(ev)



