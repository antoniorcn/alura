import pygame
from alura_steps.aula5.utils import *
from alura_steps.aula5.nave import Nave
from alura_steps.aula5.tiro import Tiro
from alura_steps.aula5.enemy import Enemy

pygame.init()
pygame.mixer.init()

tela = pygame.display.set_mode((WIDTH, HEIGHT), 0)
spritesheet = pygame.image.load("./images/naves.png").convert_alpha()
sounds = dict()
sounds['musica_inicial'] = pygame.mixer.Sound(file="./sounds/theme_song.ogg")
sounds['tiro'] = pygame.mixer.Sound(file="./sounds/firing.ogg")
sounds['kill_enemy'] = pygame.mixer.Sound(file="./sounds/kill_enemy.ogg")

nave1 = Nave(spritesheet, sounds)
aliadas = pygame.sprite.Group()
aliadas.add(nave1)

tiros = pygame.sprite.Group()

inimigo1 = Enemy(spritesheet, sounds)
inimigos = pygame.sprite.Group(inimigo1)


def game_loop():
    while True:
        # calcular regras
        aliadas.update()
        inimigos.update()
        tiros.update()
        for inimigo in inimigos:
            if pygame.sprite.spritecollide(inimigo, tiros, True):
                inimigo.matou()

        # testar se a nave colidiu com o chão

        if len(inimigos) <= 0:
            inimigos.add(Enemy(spritesheet, sounds))

        # pintar
        tela.fill(PRETO)
        aliadas.draw(tela)
        inimigos.draw(tela)
        tiros.draw(tela)
        pygame.display.update()

        # capturar eventos
        for e in pygame.event.get():
            nave1.processar_eventos(e)
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_SPACE:
                    tiros.add(Tiro(spritesheet, sounds, nave1.rect.midtop))
            if e.type == pygame.QUIT:
                exit()


if __name__ == "__main__":
    aliadas.draw(tela)
    pygame.display.update()
    sounds['musica_inicial'].play()

    # Aguarda a musica a encerrar
    while pygame.mixer.get_busy():
        pass

    game_loop()
