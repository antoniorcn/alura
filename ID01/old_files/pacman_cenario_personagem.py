import pygame

from abc import ABCMeta, abstractmethod


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

    def pintar(self, tela, ppc):
        tela.fill((0, 0, 0))
        for linha_id, linha in enumerate(self.cenario):
            for coluna_id, coluna in enumerate(linha):
                cor = (0, 0, 255)
                if self.cenario[linha_id][coluna_id] == 0:
                    cor = (0, 0, 0)
                bloco = pygame.Rect((coluna_id * ppc, linha_id * ppc), (ppc, ppc))
                pygame.draw.rect(tela, cor, bloco, 0)

    def calcular_regras(self):
        pass

    def processar_eventos(self, eventos):
        for evento in eventos:
            if evento.type == pygame.QUIT:
                exit()


class Pacman(ElementoJogo):
    def __init__(self):
        self.x = 1
        self.y = 1

    def pintar(self, tela, ppc):
        # Desenha o pacman
        px = self.x * ppc
        py = self.y * ppc
        pygame.draw.circle(tela, (255, 255, 0), (px + (ppc // 2), py + (ppc // 2)), ppc // 2, 0)

        # Desenha o recorte da boca
        polygon = [(px + (ppc // 2), py + (ppc // 2)),
                   (px + ppc, py + (ppc // 2)),
                   (px + ppc, py)]
        pygame.draw.polygon(tela, (0, 0, 0), polygon, 0)

        # Desenha o olho
        pygame.draw.circle(tela, (0, 0, 0), (px + int(ppc // 1.7), py + int(ppc / 5)), ppc // 10, 0)

    def calcular_regras(self):
        pass

    def processar_eventos(self, eventos):
        pass


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

    def loop_jogo(self):
        while True:
            eventos = pygame.event.get()
            for elemento in self.elementos:
                elemento.calcular_regras()
                elemento.pintar(self.tela, self.PPC)
                elemento.processar_eventos(eventos)
            pygame.display.update()


if __name__ == "__main__":
    jogo = Jogo()
    cenario = Cenario()
    bol1 = Pacman()

    jogo.adicionar_elemento(cenario)
    jogo.adicionar_elemento(bol1)
    jogo.loop_jogo()
