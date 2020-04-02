import pygame
from abc import ABCMeta, abstractmethod
pygame.init()
screen = pygame.display.set_mode((800, 600), 0)


class Movivel(metaclass=ABCMeta):
    @abstractmethod
    def get_pos(self):
        pass

    @abstractmethod
    def notificar(self, aceita):
        pass


class ObservadorMovivel(metaclass=ABCMeta):
    @abstractmethod
    def verificar_movimento(self):
        pass

    def adicionar_movivel(self, obj):
        pass


class ElementoJogo(metaclass=ABCMeta):
    AMARELO = (255, 255, 0)
    PRETO = (0, 0, 0)
    AZUL = (0, 0, 255)
    VERMELHO = (255, 0, 0)
    CIANO = (0, 255, 255)
    LARANJA = (255, 140, 0)
    ROSA = (255, 15, 192)
    BRANCO = (255, 255, 255)
    TAMANHO = 36
    VELOCIDADE = 1.0

    @abstractmethod
    def pintar(self, tela):
        pass

    @abstractmethod
    def calcular_regras(self):
        pass

    @abstractmethod
    def processar_eventos(self, eventos):
        pass


class Cenario(ElementoJogo, ObservadorMovivel):
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.moviveis = []
        self.cenario = [
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
            [2, 1, 1, 2, 1, 2, 1, 2, 2, 1, 2, 1, 2, 1, 1, 2],
            [2, 1, 2, 2, 1, 2, 1, 2, 2, 1, 2, 1, 2, 2, 1, 2],
            [2, 1, 1, 2, 1, 2, 1, 1, 1, 1, 2, 1, 2, 1, 1, 2],
            [2, 1, 1, 1, 1, 2, 1, 2, 2, 1, 2, 1, 1, 1, 1, 2],
            [2, 2, 2, 2, 1, 2, 1, 2, 2, 1, 2, 1, 2, 2, 2, 2],
            [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
            [2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2],
            [2, 1, 1, 1, 1, 1, 2, 0, 0, 2, 1, 1, 1, 1, 1, 2],
            [2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2],
            [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
            [2, 2, 2, 2, 1, 2, 1, 2, 2, 1, 2, 1, 2, 2, 2, 2],
            [2, 1, 1, 1, 1, 2, 1, 2, 2, 1, 2, 1, 1, 1, 1, 2],
            [2, 1, 1, 2, 1, 2, 1, 1, 1, 1, 2, 1, 2, 1, 1, 2],
            [2, 1, 2, 2, 1, 2, 1, 2, 2, 1, 2, 1, 2, 2, 1, 2],
            [2, 1, 1, 2, 1, 2, 1, 2, 2, 1, 2, 1, 2, 1, 1, 2],
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
        ]

    def pintar_linha(self, linha_id, linha, tela, ppc):
        for coluna_id, coluna in enumerate(linha):
            cor = ElementoJogo.PRETO
            x_initial = coluna_id * ppc
            y_initial = linha_id * ppc
            if self.cenario[linha_id][coluna_id] == 2:
                cor = ElementoJogo.AZUL
            bloco = pygame.Rect((x_initial, y_initial), (ppc, ppc))
            pygame.draw.rect(tela, cor, bloco, 0)

            if self.cenario[linha_id][coluna_id] == 1:
                x_middle = x_initial + ppc // 2
                y_middle = y_initial + ppc // 2
                raio = ppc // 10
                pygame.draw.circle(tela, ElementoJogo.AMARELO, (x_middle, y_middle), raio, 0)

    def pintar(self, tela):
        for linha_id, linha in enumerate(self.cenario):
            self.pintar_linha(linha_id, linha, tela, self.tamanho)

    def get_celula(self, coluna, linha):
        celula = None
        if 0 < coluna < 16 and 0 < linha < 16:
            celula = self.cenario[int(linha)][int(coluna)]
        return celula

    def calcular_regras(self):
        self.verificar_movimento()

    def processar_eventos(self, eventos):
        for evento in eventos:
            if evento.type == pygame.QUIT:
                exit()

    def verificar_movimento(self):
        for movivel in self.moviveis:
            coluna, linha = movivel.get_pos()
            celula = self.get_celula(coluna, linha)
            aceitar = False
            if celula is not None and celula != 2:
                aceitar = True
                if celula == 1:
                    self.cenario[int(linha)][int(coluna)] = 0
            movivel.notificar(aceitar)

    def adicionar_movivel(self, obj):
        self.moviveis.append(obj)


class Pacman(ElementoJogo, Movivel):
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
        pygame.draw.circle(tela, ElementoJogo.AMARELO, (corpo_x, corpo_y), corpo_raio, 0)

        # Desenha o recorte da boca
        boca_labio_inferior = (px + self.tamanho, corpo_y)
        boca_fundo = (corpo_x, corpo_y)
        boca_labio_superior = (px + self.tamanho, py)

        polygon = [boca_fundo, boca_labio_inferior, boca_labio_superior]
        pygame.draw.polygon(tela, ElementoJogo.PRETO, polygon, 0)

        # Desenha o olho
        olho_x = px + round(self.tamanho // 1.7)
        olho_y = py + round(self.tamanho / 5)
        olho_raio = self.tamanho // 10
        pygame.draw.circle(tela, ElementoJogo.PRETO, (olho_x, olho_y), olho_raio, 0)

    def calcular_regras(self):
        self.temp_coluna = self.coluna + self.velx
        self.temp_linha = self.linha + self.vely

    def processar_eventos(self, eventos):
        for evento in eventos:
            if evento.type == pygame.QUIT:
                exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_DOWN:
                    self.vely = ElementoJogo.VELOCIDADE
                elif evento.key == pygame.K_UP:
                    self.vely = -ElementoJogo.VELOCIDADE
                elif evento.key == pygame.K_LEFT:
                    self.velx = -ElementoJogo.VELOCIDADE
                elif evento.key == pygame.K_RIGHT:
                    self.velx = ElementoJogo.VELOCIDADE
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

    def notificar(self, aceita):
        if aceita:
            self.coluna = self.temp_coluna
            self.linha = self.temp_linha
        else:
            self.temp_coluna = self.coluna
            self.temp_linha = self.linha


class Fantasma(ElementoJogo, Movivel):
    def __init__(self, tamanho, cor):
        self.coluna = 7.0  # Coluna onde será desenhado
        self.linha = 8.0  # Linha onde será desenhado
        self.tamanho = tamanho
        self.velx = 0.0
        self.vely = 0.0
        self.intencao_coluna = self.coluna
        self.intencao_linha = self.linha
        self.cor = cor

    def pintar(self, tela):
        # Desenha o fantasma
        fatia = self.tamanho // 8
        px = int(self.coluna * self.tamanho)
        py = int(self.linha * self.tamanho)
        contorno = [(px, py + self.tamanho),
                    (px + fatia, py + fatia * 2),
                    (px + fatia * 2, py + fatia // 2),
                    (px + fatia * 3, py),
                    (px + fatia * 5, py),
                    (px + fatia * 6, py + fatia // 2),
                    (px + fatia * 7, py + fatia * 2),
                    (px + self.tamanho, py + self.tamanho)
                    ]
        pygame.draw.polygon(tela, self.cor, contorno, 0)

        olho_raio1 = fatia
        olho_raio2 = fatia // 2

        # Desenha o olho esquerdo
        olho_e_x = px + round(fatia * 2.5)
        olho_e_y = py + round(fatia * 2.5)

        olho_d_x = px + round(fatia * 5.5)
        olho_d_y = py + round(fatia * 2.5)

        pygame.draw.circle(tela, ElementoJogo.BRANCO, (olho_e_x, olho_e_y), olho_raio1, 0)
        pygame.draw.circle(tela, ElementoJogo.PRETO, (olho_e_x, olho_e_y), olho_raio2, 0)
        pygame.draw.circle(tela, ElementoJogo.BRANCO, (olho_d_x, olho_d_y), olho_raio1, 0)
        pygame.draw.circle(tela, ElementoJogo.PRETO, (olho_d_x, olho_d_y), olho_raio2, 0)

    def calcular_regras(self):
        self.intencao_coluna = self.coluna + self.velx
        self.intencao_linha = self.linha + self.vely

    def processar_eventos(self, eventos):
        pass

    def get_pos(self):
        return self.intencao_coluna, self.intencao_linha

    def notificar(self, aceita):
        if aceita:
            self.coluna = self.intencao_coluna
            self.linha = self.intencao_linha
        else:
            self.intencao_coluna = self.coluna
            self.intencao_linha = self.linha


if __name__ == "__main__":
    pacman = Pacman(ElementoJogo.TAMANHO)
    blinky = Fantasma(ElementoJogo.TAMANHO, ElementoJogo.VERMELHO)
    cenario = Cenario(ElementoJogo.TAMANHO)
    cenario.adicionar_movivel(pacman)
    cenario.adicionar_movivel(blinky)
    while True:
        # Calcular regras
        cenario.calcular_regras()
        pacman.calcular_regras()
        blinky.calcular_regras()

        # Pintar a tela
        screen.fill(ElementoJogo.PRETO)
        cenario.pintar(screen)
        pacman.pintar(screen)
        blinky.pintar(screen)
        pygame.display.update()
        pygame.time.delay(100)

        # Capturar eventos
        ev = pygame.event.get()
        cenario.processar_eventos(ev)
        pacman.processar_eventos(ev)
