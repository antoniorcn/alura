import pygame

from abc import ABCMeta, abstractmethod


AZUL = (0, 0, 255)
PRETO = (0, 0, 0)
AMARELO = (255, 255, 0)


class ElementoJogo(metaclass=ABCMeta):
    @abstractmethod
    def pintar(self, tela, ppc):
        pass

    @abstractmethod
    def calcular_regras(self):
        pass

    @abstractmethod
    def processar_eventos(self, eventos):
        pass


class Cenario(ElementoJogo):
    def __init__(self):
        self.cenario = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1],
            [1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1],
            [1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1],
            [1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1],
            [1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1],
            [1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1],
            [1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        ]

    def pintar_linha(self, linha_id, linha, tela, ppc):
        for coluna_id, coluna in enumerate(linha):
            cor = AZUL
            if self.cenario[linha_id][coluna_id] == 0:
                cor = PRETO
            x_initial = coluna_id * ppc
            y_initial = linha_id * ppc
            bloco = pygame.Rect((x_initial, y_initial), (ppc, ppc))
            pygame.draw.rect(tela, cor, bloco, 0)

    def pintar(self, tela, ppc):
        for linha_id, linha in enumerate(self.cenario):
            self.pintar_linha(linha_id, linha, tela, ppc)

    def calcular_regras(self):
        pass

    def processar_eventos(self, eventos):
        for evento in eventos:
            if evento.type == pygame.QUIT:
                exit()


class Pacman(ElementoJogo):
    def __init__(self):
        self.x = 1.0
        self.y = 1.0
        self.velx = 0.0
        self.vely = 0.0

    def pintar(self, tela, ppc):
        # Desenha o pacman
        px = int(self.x * ppc)   # X do canto superior esquerdo
        py = int(self.y * ppc)   # Y do canto superior esquerdo
        corpo_x = px + (ppc // 2)
        corpo_y = py + (ppc // 2)
        corpo_raio = ppc // 2
        pygame.draw.circle(tela, AMARELO, (corpo_x, corpo_y), corpo_raio, 0)

        # Desenha o recorte da boca
        boca_labio_inferior = (px + ppc, corpo_y)
        boca_fundo = (corpo_x, corpo_y)
        boca_labio_superior = (px + ppc, py)

        polygon = [boca_fundo, boca_labio_inferior, boca_labio_superior]
        pygame.draw.polygon(tela, PRETO, polygon, 0)

        # Desenha o olho
        olho_x = px + int(ppc // 1.7)
        olho_y = py + int(ppc / 5)
        olho_raio = ppc // 10
        pygame.draw.circle(tela, PRETO, (olho_x, olho_y), olho_raio, 0)

    def calcular_regras(self):
        self.x += self.velx
        self.y += self.vely

    def processar_eventos(self, eventos):
        for e in eventos:
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_DOWN:
                    self.vely = 0.01
                elif e.key == pygame.K_UP:
                    self.vely = -0.01
                elif e.key == pygame.K_LEFT:
                    self.velx = -0.01
                elif e.key == pygame.K_RIGHT:
                    self.velx = 0.01


class Jogo:
    def __init__(self):
        pygame.init()
        self.elementos = []
        self.tela = pygame.display.set_mode((800, 640), 0)
        self.PPC = (640 // 16) - 2

    def adicionar_elemento(self, elemento):
        self.elementos.append(elemento)

    def remover_elemento(self, elemento):
        self.elementos.remove(elemento)

    def calcular_regras(self):
        for elemento in self.elementos:
            elemento.calcular_regras()

    def pintar(self):
        self.tela.fill(PRETO)
        for elemento in self.elementos:
            elemento.pintar(self.tela, self.PPC)
        pygame.display.update()

    def processar_eventos(self):
        eventos = pygame.event.get()
        for elemento in self.elementos:
            elemento.processar_eventos(eventos)

    def loop_jogo(self):
        while True:
            self.calcular_regras()
            self.pintar()
            self.processar_eventos()


if __name__ == "__main__":
    jogo = Jogo()
    cenario = Cenario()
    bol1 = Pacman()

    jogo.adicionar_elemento(cenario)
    jogo.adicionar_elemento(bol1)
    jogo.loop_jogo()
