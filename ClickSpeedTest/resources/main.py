import pygame, sys
pygame.init()

class Game:
    def __init__(self):
        self.font = pygame.font.SysFont("Comic Sans MS", 30)
        self.FPS = 60
        self.clock = pygame.time.Clock()
        self.over = False
        self.display = pygame.display.set_mode((500,500))
        self.background = pygame.image.load('resources\\background.png')
        self.score = 0
        self.counter = 5
        self.text = self.counter

    def update(self):
        self.clock.tick(self.FPS)
        self.display.blit(self.background, (0,0))
        textScore = self.font.render('score: {}'.format(str(self.score)), 1, (0,0,0))
        textTimer = self.font.render(str(self.counter), 1, (0,0,0))
        if self.counter >= 0:
            self.display.blit(textTimer, (10,40))
        self.display.blit(textScore, (10,10))
        pygame.display.update()

    def gameOver(self):
        self.display.fill((0,0,0))
        cps = self.font.render('Clicks Per Second: {}'.format(str(self.score)), 1, (255,255,255))
        x = cps.get_rect(center=(250,250))
        finalScore = self.font.render('Score: {}'.format(str(self.score * 5)), 1, (255,255,255))
        y = finalScore.get_rect(center=(250, 300))
        self.display.blit(finalScore, x)
        self.display.blit(finalScore, y)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.quit()
                sys.exit()
