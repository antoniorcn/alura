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

    jogo.adicionar_elemento(cenario)
    jogo.loop_jogo()
