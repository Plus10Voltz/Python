import pygame, sys
pygame.init()

BLACK = (0,0,0)
GREY = (135,135,135)
WHITE = (255,255,255)
PURPLE = (126, 47, 237)

# Grid Block Size
WIDTH = 56
HEIGHT = 55
MARGIN = 5

class Game:
    def __init__(self):
        self.font = pygame.font.SysFont("Comic Sans MS", 20)
        self.FPS = 60
        self.clock = pygame.time.Clock()
        self.over = False
        self.display = pygame.display.set_mode((620,660))
        self.score = 0
        self.timer = 0
        self.grid = [[0 for x in range(10)] for y in range(10)]

    def drawGrid(self):
        row = 0
        col = 0
        for i in range(10):
            for j in range(10):
                colour = WHITE
                if self.grid[row][col] == 1:
                    colour = PURPLE
                pygame.draw.rect(self.display, colour, (i * (WIDTH + MARGIN) + MARGIN + 2,
                j * (HEIGHT + MARGIN) + MARGIN + 50, WIDTH, HEIGHT))

    def update(self):
        self.clock.tick(self.FPS)
        self.display.fill(GREY)
        textScore = self.font.render('Score: {}'.format(str(self.score)), 1, BLACK)
        textTimer = self.font.render(str(self.timer), 1, BLACK)
        x = textTimer.get_rect(center=(620/2, 25))
        self.display.blit(textScore, (20,10))
        self.display.blit(textTimer, x)
        self.drawGrid()
        pygame.display.update()

    def onClick(self):
        pos = pygame.mouse.get_pos()
        col = pos[0] // (WIDTH + MARGIN)
        row = pos[1] // (HEIGHT + MARGIN)
        print('{},{}'.format(col, row))
        self.grid[row][col] = 1
