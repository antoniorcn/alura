import pygame

from abc import ABCMeta, abstractmethod

AZUL = (0, 0, 255)
PRETO = (0, 0, 0)
AMARELO = (255, 255, 0)

ACERELERACAO = 0.05


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


class Validador(metaclass=ABCMeta):
    @abstractmethod
    def validar(self, elemento):
        return True


class Validavel(metaclass=ABCMeta):
    @abstractmethod
    def get_linha(self):
        pass

    @abstractmethod
    def get_coluna(self):
        pass

    @abstractmethod
    def aceitar(self):
        pass


class Pontuavel(metaclass=ABCMeta):
    @abstractmethod
    def get_pontos(self):
        pass

    @abstractmethod
    def adicionar_pontos(self, pontos):
        pass

    @abstractmethod
    def remover_pontos(self, pontos):
        pass


class Cenario(ElementoJogo, Validador):
    def __init__(self):
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

    def pintar(self, tela, ppc):
        for linha_id, linha in enumerate(self.cenario):
            self.pintar_linha(linha_id, linha, tela, ppc)

    def calcular_regras(self):
        pass

    def processar_eventos(self, eventos):
        for evento in eventos:
            if evento.type == pygame.QUIT:
                exit()

    def validar(self, elemento):
        coluna = elemento.get_coluna()
        linha = elemento.get_linha()
        celula = self.cenario[linha][coluna]
        if celula != 2:
            elemento.aceitar()
        if isinstance(elemento, Pontuavel) and celula == 1:
            elemento.adicionar_pontos(1)
            self.cenario[linha][coluna] = 0


class Pacman(ElementoJogo, Validavel, Pontuavel):
    def __init__(self):
        self.x = 1.0
        self.y = 1.0
        self.velx = 0.0
        self.vely = 0.0
        self.x_temp = self.x
        self.y_temp = self.y
        self.pontos = 0

    def pintar(self, tela, ppc):
        # Desenha o pacman
        px = round(self.x) * ppc  # X do canto superior esquerdo
        py = round(self.y) * ppc  # Y do canto superior esquerdo
        # print("X({})  Y({})   TEMP_X({})   TEMP_Y({})  pX({})  pY({})"
        #      .format(round(self.x), round(self.y), self.x_temp, self.y_temp, px, py))
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
        olho_x = px + round(ppc // 1.7)
        olho_y = py + round(ppc / 5)
        olho_raio = ppc // 10
        pygame.draw.circle(tela, PRETO, (olho_x, olho_y), olho_raio, 0)

    def calcular_regras(self):
        self.x_temp = self.x + self.velx
        self.y_temp = self.y + self.vely

    def processar_eventos(self, eventos):
        for e in eventos:
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

    def aceitar(self):
        self.x = self.x_temp
        self.y = self.y_temp

    def get_coluna(self):
        return round(self.x_temp)

    def get_linha(self):
        return round(self.y_temp)

    def get_pontos(self):
        return self.pontos

    def adicionar_pontos(self, pontos):
        self.pontos += pontos
        print(self.pontos)

    def remover_pontos(self, pontos):
        self.pontos -= pontos


class Jogo:
    def __init__(self):
        pygame.init()
        self.fonte = pygame.font.SysFont("arial", 20, True, False)
        self.elementos = []
        self.validador = None
        self.pontuavel = None
        self.tela = pygame.display.set_mode((800, 640), 0)
        self.PPC = (640 // 16) - 2
        self.info_x = 640 + self.PPC

    def set_validador(self, validador):
        self.validador = validador

    def set_pontuavel(self, pontuavel):
        self.pontuavel = pontuavel

    def adicionar_elemento(self, elemento):
        self.elementos.append(elemento)

    def remover_elemento(self, elemento):
        self.elementos.remove(elemento)

    def calcular_regras(self):
        for elemento in self.elementos:
            elemento.calcular_regras()
            if self.validador is not None and isinstance(elemento, Validavel):
                self.validador.validar(elemento)

    def pintar_pontos(self):
        pontos = 0
        if isinstance(self.pontuavel, Pontuavel):
            pontos = self.pontuavel.get_pontos()
        score = self.fonte.render("Score: {}".format(pontos), True, AMARELO)
        self.tela.blit(score, (self.info_x, 50))

    def pintar(self):
        self.tela.fill(PRETO)
        for elemento in self.elementos:
            elemento.pintar(self.tela, self.PPC)
        self.pintar_pontos()
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
    pacman = Pacman()

    jogo.adicionar_elemento(cenario)
    jogo.adicionar_elemento(pacman)
    jogo.set_validador(cenario)
    jogo.set_pontuavel(pacman)
    jogo.loop_jogo()
