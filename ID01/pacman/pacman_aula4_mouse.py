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
        self.velx = 0.0
        self.vely = 0.0

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

    def processar_eventos(self, eventos):
        for evento in eventos:
            if evento.type == pygame.QUIT:
                exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_DOWN:
                    self.vely = VELOCIDADE
                elif evento.key == pygame.K_UP:
                    self.vely = -VELOCIDADE
                elif evento.key == pygame.K_LEFT:
                    self.velx = -VELOCIDADE
                elif evento.key == pygame.K_RIGHT:
                    self.velx = VELOCIDADE
            if evento.type == pygame.KEYUP:
                if evento.key == pygame.K_DOWN:
                    self.vely = 0.0
                elif evento.key == pygame.K_UP:
                    self.vely = 0.0
                elif evento.key == pygame.K_LEFT:
                    self.velx = 0.0
                elif evento.key == pygame.K_RIGHT:
                    self.velx = 0.0

    def processar_eventos_mouse(self, eventos):
        for evento in eventos:
            if evento.type == pygame.QUIT:
                exit()
            if evento.type == pygame.MOUSEMOTION:
                vx, vy = evento.rel
                if vx > 0:
                    self.velx = VELOCIDADE
                elif vx < 0:
                    self.velx = -VELOCIDADE
                else:
                    self.velx = 0.0

                if vy > 0:
                    self.vely = VELOCIDADE
                elif vy < 0:
                    self.vely = -VELOCIDADE
                else:
                    self.vely = 0.0


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
        ev = pygame.event.get()
        pacman.processar_eventos_mouse(ev)
