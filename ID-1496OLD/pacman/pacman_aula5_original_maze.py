import pygame
pygame.init()
screen = pygame.display.set_mode((800, 600), 0)
AMARELO = (255, 255, 0)
PRETO = (0, 0, 0)
AZUL = (0, 0, 255)
TAMANHO = 16
VELOCIDADE = 1.0


class Cenario:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.pacman = None
        self.cenario = [
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
            [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2],
            [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
            [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
            [2, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 0, 0, 0, 0, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 2],
            [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
            [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
            [2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
        ]

    def pintar_linha(self, linha_id, linha, tela, ppc):
        for coluna_id, coluna in enumerate(linha):
            cor = PRETO
            x_initial = coluna_id * ppc
            y_initial = linha_id * ppc
            if self.cenario[linha_id][coluna_id] == 2:
                cor = AZUL
            bloco = pygame.Rect((x_initial, y_initial), (ppc, ppc))
            pygame.draw.rect(tela, cor, bloco, 0)

            if self.cenario[linha_id][coluna_id] == 1:
                x_middle = x_initial + ppc // 2
                y_middle = y_initial + ppc // 2
                raio = ppc // 10
                pygame.draw.circle(tela, AMARELO, (x_middle, y_middle), raio, 0)

    def pintar(self, tela):
        for linha_id, linha in enumerate(self.cenario):
            self.pintar_linha(linha_id, linha, tela, self.tamanho)

    def calcular_regras(self):
        coluna, linha = self.pacman.get_pos()
        if 0 < coluna < len(self.cenario[0]) \
                and 0 < linha < len(self.cenario):
            celula = self.cenario[int(linha)][int(coluna)]
            if celula != 2:
                self.pacman.aceitar_x()
                self.pacman.aceitar_y()
                if celula == 1:
                    self.cenario[int(linha)][int(coluna)] = 0

    def set_pacman(self, pacman):
        self.pacman = pacman


class Pacman:
    def __init__(self, tamanho):
        self.coluna = 1.0  # Coluna onde será desenhado
        self.linha = 1.0  # Linha onde será desenhado
        self.tamanho = tamanho
        self.velx = 0.0
        self.vely = 0.0
        self.temp_coluna = self.coluna
        self.temp_linha = self.linha

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
        self.temp_coluna = self.coluna + self.velx
        self.temp_linha = self.linha + self.vely

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

    def get_pos(self):
        return self.temp_coluna, self.temp_linha

    def aceitar_x(self):
        self.coluna = self.temp_coluna

    def aceitar_y(self):
        self.linha = self.temp_linha


if __name__ == "__main__":
    pacman = Pacman(TAMANHO)
    cenario = Cenario(TAMANHO)
    cenario.set_pacman(pacman)
    while True:
        # Calcular regras
        cenario.calcular_regras()
        pacman.calcular_regras()

        # Pintar a tela
        screen.fill(PRETO)
        cenario.pintar(screen)
        pacman.pintar(screen)
        pygame.display.update()
        pygame.time.delay(100)

        # Capturar eventos
        ev = pygame.event.get()
        pacman.processar_eventos(ev)
