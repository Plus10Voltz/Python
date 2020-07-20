import pygame, sys
from resources.balloonClass import Balloon
pygame.init()

pop = pygame.mixer.Sound('resources\pop.wav')
class Game:
    def __init__(self):
        self.font = pygame.font.SysFont('Comic Sans MS', 40)
        self.FPS = 60
        self.clock = pygame.time.Clock()
        self.over = False
        self.display = pygame.display.set_mode((900, 900))
        self.background = pygame.image.load('resources\\background.png')
        self.group = pygame.sprite.LayeredUpdates()
        self.speed = 5
        self.score = 0
        self.lives = 100

    def update(self):
        self.clock.tick(self.FPS)
        self.display.blit(self.background, (0,0))
        self.group.draw(self.display)
        self.group.update()
        for e in self.group:
            if e.rect.y < -250:
                e.kill()
                self.lives -= 1
                if self.lives < 1:
                    self.over = True
        largeFont = pygame.font.SysFont('Comic Sans MS',30)
        textScore = largeFont.render('score: {}'.format(str(self.score)), 1, (0,0,0))
        textLives = largeFont.render('lives: {}'.format(str(self.lives)), 1, (0,0,0))
        self.display.blit(textScore, (10,10))
        self.display.blit(textLives, (10,50))
        pygame.display.update()

    def spawnBalloon(self):
        self.balloon = Balloon(self.speed)
        self.group.add(self.balloon)

    def checkclick(self, pos):
        sprtlist = self.group.get_sprites_at(pos)
        for i in sprtlist:
            i.balloonPop()
            pygame.mixer.Sound.play(pop)
            # i.kill()
            if self.score < 1000:
                self.score += 1

    def speedup(self):
        self.speed += 2
