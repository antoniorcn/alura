import pygame
import operator

pygame.init()
pygame.mixer.init()

WIDTH = 800
HEIGHT = 400
PRETO = (0, 0, 0)
CENTRO_X_TELA = WIDTH // 2
CENTRO_Y_TELA = HEIGHT // 2
tela = pygame.display.set_mode((WIDTH, HEIGHT), 0)
naves = pygame.image.load("./images/naves.png").convert_alpha()
musica_inicial = pygame.mixer.Sound(file="./sounds/theme_song.ogg")
snd_tiro = pygame.mixer.Sound(file="./sounds/firing.ogg")
snd_kill_enemy = pygame.mixer.Sound(file="./sounds/kill_enemy.ogg")


def circular(iterable):
    while iterable:
        for element in iterable:
            yield element


class Tiro(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.frames = circular([
            pygame.Rect((365, 195), (3, 8))])
        self.velocity = [0, -1]
        self.image = naves.subsurface(next(self.frames))
        self.rect = pygame.Rect(pos,
                                self.image.get_size())

    def update(self):
        self.image = naves.subsurface(next(self.frames))
        self.rect.center = list(map(operator.add, self.rect.center, self.velocity))
        if self.rect.left < 0:
            self.kill()


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.frames_normal = circular([
            pygame.Rect((160, 104), (16, 16)),
            pygame.Rect((184, 104), (16, 16))
        ])
        self.frames_explosao = circular([
            pygame.Rect((198, 190), (32, 32)),
            pygame.Rect((224, 190), (32, 32)),
            pygame.Rect((248, 190), (32, 32)),
            pygame.Rect((280, 190), (32, 32)),
            pygame.Rect((320, 190), (32, 32)),
            pygame.Rect((280, 190), (32, 32)),
            pygame.Rect((248, 190), (32, 32)),
            pygame.Rect((224, 190), (32, 32)),
            pygame.Rect((196, 190), (32, 32))
        ])
        self.estado = 0
        self.velocity = [1, 1]
        self.update()
        self.rect = pygame.Rect((CENTRO_X_TELA, 200),
                                self.image.get_size())

    def update(self):
        if self.estado == 0:
            self.image = naves.subsurface(next(self.frames_normal))
        else:
            self.image = naves.subsurface(next(self.frames_explosao))

    def kill(self):
        self.estado = 1

class Nave(pygame.sprite.Sprite):
    def __init__(self):
        r = pygame.Rect((160, 55), (16, 16))
        pygame.sprite.Sprite.__init__(self)
        self.velocity = [1, 0]
        self.image = naves.subsurface(r)
        self.rect = pygame.Rect((CENTRO_X_TELA, 300),
                                self.image.get_size())

    def update(self):
        self.rect.center = list(map(operator.add, self.rect.center, self.velocity))
        if self.rect.right > WIDTH:
            self.velocity[0] = -1
        if self.rect.left < 0:
            self.velocity[0] = 1


nave1 = Nave()
aliadas = pygame.sprite.Group()
aliadas.add(nave1)

tiros = pygame.sprite.Group()

inimigo1 = Enemy()
inimigos = pygame.sprite.Group()
inimigos.add(inimigo1)

aliadas.draw(tela)
pygame.display.update()
# musica_inicial.play()

# Aguarda a musica a encerrar
# while pygame.mixer.get_busy():
#    pass

while True:
    # calcular regras
    aliadas.update()
    inimigos.update()
    tiros.update()
    if pygame.sprite.spritecollide(inimigo1, tiros, True):
        inimigo1.kill()
        snd_tiro.stop()
        snd_kill_enemy.stop()
        snd_kill_enemy.play()

    # pintar
    tela.fill(PRETO)
    aliadas.draw(tela)
    inimigos.draw(tela)
    tiros.draw(tela)
    pygame.display.update()

    # capturar eventos
    for e in pygame.event.get():
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_SPACE:
                tiros.add(Tiro(nave1.rect.midtop))
                snd_tiro.stop()
                snd_tiro.play()
        if e.type == pygame.QUIT:
            exit()
