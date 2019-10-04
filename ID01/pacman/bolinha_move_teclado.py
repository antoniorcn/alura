import pygame

from abc import ABCMeta, abstractmethod


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


class Cenario(ElementoJogo):
    def pintar(self, tela):
        tela.fill((0, 0, 0))

    def calcular_regras(self):
        pass

    def processar_eventos(self, eventos):
        for evento in eventos:
            if evento.type == pygame.QUIT:
                exit()


class Bolinha(ElementoJogo):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.velX = 0
        self.velY = 0

    def pintar(self, tela):
        pygame.draw.circle(tela, (255, 255, 0), (self.x, self.y), 20, 0)

    def calcular_regras(self):
        if self.x < 0 or self.x > 800:
            self.velX = self.velX * -1
        if self.y < 0 or self.y > 640:
            self.velY = self.velY * -1
        self.x += self.velX
        self.y += self.velY

    def processar_eventos(self, eventos):
        for evento in eventos:
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_DOWN:
                    self.velY = 1
                elif evento.key == pygame.K_UP:
                    self.velY = -1
                elif evento.key == pygame.K_LEFT:
                    self.velX = -1
                elif evento.key == pygame.K_RIGHT:
                    self.velX = 1


class Jogo:
    def __init__(self):
        pygame.init()
        self.elementos = []
        self.tela = pygame.display.set_mode((800, 640), 0)

    def adicionar_elemento(self, elemento):
        self.elementos.append(elemento)

    def remover_elemento(self, elemento):
        self.elementos.remove(elemento)

    def loop_jogo(self):
        while True:
            eventos = pygame.event.get()
            for elemento in self.elementos:
                elemento.calcular_regras()
                elemento.pintar(self.tela)
                elemento.processar_eventos(eventos)
            pygame.display.update()


if __name__ == "__main__":
    jogo = Jogo()
    cenario = Cenario()
    bol1 = Bolinha()

    jogo.adicionar_elemento(cenario)
    jogo.adicionar_elemento(bol1)
    jogo.loop_jogo()
