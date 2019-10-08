import pygame
pygame.init()
screen = pygame.display.set_mode((800, 600), 0)
AMARELO = (255, 255, 0)
PRETO = (0, 0, 0)


class Pacman:
    def __init__(self):
        self.px = 400   # X do canto superior esquerdo onde será desenhado
        self.py = 300   # Y do canto superior esquerdo onde será desenhado

    def pintar(self, tela):
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
        pygame.display.update()

    @staticmethod
    def processar_eventos(eventos):
        for e in eventos:
            if e.type == pygame.QUIT:
                exit()


pacman = Pacman()
# Loop do Jogo
while True:
    # Pintar a tela
    pacman.pintar(screen)

    # Capturar eventos
    ev = pygame.event.get()
    pacman.processar_eventos(ev)



