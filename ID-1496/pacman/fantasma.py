import math
import pygame
from abc import ABCMeta, abstractmethod
pygame.init()
screen = pygame.display.set_mode((800, 600), 0)
AMARELO = (255, 255, 0)
PRETO = (0, 0, 0)
AZUL = (0, 0, 255)
VERMELHO = (255, 0, 0)
BRANCO = (255, 255, 255)
TAMANHO = 80
VELOCIDADE = 1.0


class ElementoJogo(metaclass=ABCMeta):
    @abstractmethod
    def pintar(self, tela):
        pass

    @abstractmethod
    def calcular_regras(self):
        pass

    @abstractmethod
    def processar_eventos(self, eventos):
        pass


class Fantasma(ElementoJogo):
    def __init__(self, tamanho):
        self.coluna = 1.0  # Coluna onde será desenhado
        self.linha = 1.0  # Linha onde será desenhado
        self.tamanho = tamanho
        self.velx = 0.0
        self.vely = 0.0
        self.temp_coluna = self.coluna
        self.temp_linha = self.linha

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
                    (px + self.tamanho, py + self.tamanho),
                    (px + fatia * 7, py + fatia * 6),
                    (px + fatia * 6, py + self.tamanho),
                    (px + fatia * 5, py + fatia * 6),
                    (px + fatia * 4, py + self.tamanho),
                    (px + fatia * 3, py + fatia * 6),
                    (px + fatia * 2, py + self.tamanho),
                    (px + fatia, py + fatia * 6)
                    ]
        pygame.draw.polygon(tela, VERMELHO, contorno, 0)

        olho_raio1 = fatia
        olho_raio2 = fatia // 2

        # Desenha o olho esquerdo
        olho_e_x = px + round(fatia * 2.5)
        olho_e_y = py + round(fatia * 2.5)

        olho_d_x = px + round(fatia * 5.5)
        olho_d_y = py + round(fatia * 2.5)

        pygame.draw.circle(tela, BRANCO, (olho_e_x, olho_e_y), olho_raio1, 0)
        pygame.draw.circle(tela, PRETO, (olho_e_x, olho_e_y), olho_raio2, 0)
        pygame.draw.circle(tela, BRANCO, (olho_d_x, olho_d_y), olho_raio1, 0)
        pygame.draw.circle(tela, PRETO, (olho_d_x, olho_d_y), olho_raio2, 0)

    def calcular_regras(self):
        self.temp_coluna = self.coluna + self.velx
        self.temp_linha = self.linha + self.vely

    def processar_eventos(self, eventos):
        for evento in eventos:
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
    ghost = Fantasma(TAMANHO)
    while True:
        # Calcular regras
        ghost.calcular_regras()

        # Pintar a tela
        screen.fill(PRETO)
        ghost.pintar(screen)
        pygame.display.update()
        pygame.time.delay(100)

        # Capturar eventos
        ev = pygame.event.get()
        ghost.processar_eventos(ev)
        ghost.aceitar_x()
        ghost.aceitar_y()
