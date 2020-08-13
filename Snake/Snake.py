import pygame, sys
import time, os, random
pygame.init()

WIDTH, HEIGHT = 20, 20
arrowKeys = [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]


class Board:
    def __init__(self):
        self.board = [[0 for x in range(25)] for y in range(30)]
        self.FPS = 144
        self.clock = pygame.time.Clock()
        self.over = False
        self.display = pygame.display.set_mode((500, 600)) # 25h x 30v
        self.snake = Snake()
        self.colour = [255,0,0]

    def update(self):
        self.rainbow()
        self.updateBoard()
        self.clock.tick(self.FPS)
        self.display.fill((30,30,30))
        self.drawGrid()
        pygame.display.update()

    def drawGrid(self):
        for i in range(30):
            for j in range(25):
                if self.board[i][j] == 0:
                    pygame.draw.rect(self.display, (180,180,180),
                    (j * WIDTH, i * HEIGHT, WIDTH, HEIGHT), 1)
                elif self.board[i][j] == 1:
                    pygame.draw.rect(self.display, self.colour,
                    (j * WIDTH, i * HEIGHT, WIDTH, HEIGHT))
                else:
                    pygame.draw.rect(self.display, (0,220,0),
                    (j * WIDTH, i * HEIGHT, WIDTH, HEIGHT))

    def updateBoard(self):
        for b in range(25):
            for d in range(30):
                if [b,d] in self.snake.body:
                    self.board[d][b] = 1

    def placeApple(self):
        x = random.randint(0,29)
        y = random.randint(0,24)
        if self.board[x][y] != 1:
            self.board[x][y] = 2
        else:
            self.placeApple()

    def rainbow(self):
        rgbColour = self.colour
        if rgbColour[0] in range(1,256) and rgbColour[2] == 0:
            rgbColour[0] -= 1
            rgbColour[1] += 1
        elif rgbColour[1] in range(1,256):
            rgbColour[1] -= 1
            rgbColour[2] += 1
        elif rgbColour[2] in range(1,256):
            rgbColour[2] -=1
            rgbColour[0] += 1
        else:
            pass
        self.colour = rgbColour

class Snake:
    def __init__(self):
        self.length = 3
        self.speed = 5
        self.direction = 'up'
        self.headX = 12
        self.headY = 15
        self.body = [[self.headX,self.headY]]
        self.moving = 0

    def move(self, board):
        flag = self.length
        if self.headX in range(0,25) and self.headY in range(0,30):
            board[self.body[-1][1]][self.body[-1][0]] = 0
            if len(self.body) >= self.length:
                self.body.pop()
            if self.direction == 'up':
                if board[self.headY - 1][self.headX] == 2:
                    self.length += 1
                elif board[self.headY - 1][self.headX] == 1:
                    return "over"
                self.headY -= 1
            elif self.direction == 'down':
                if board[self.headY + 1][self.headX] == 2:
                    self.length += 1
                elif board[self.headY + 1][self.headX] == 1:
                    return "over"
                self.headY += 1
            elif self.direction == 'left':
                if board[self.headY][self.headX - 1] == 2:
                    self.length += 1
                elif board[self.headY][self.headX - 1] == 1:
                    return "over"
                self.headX -= 1
            else:
                if board[self.headY][self.headX + 1] == 2:
                    self.length += 1
                elif board[self.headY][self.headX + 1] == 1:
                    return "over"
                self.headX += 1
            self.body.insert(0, [self.headX,self.headY])
            if flag != self.length:
                return True
        else:
            return False

    def changeDirection(self, key):
        if key == pygame.K_UP and self.direction != 'down':
            self.direction = 'up'
        elif key == pygame.K_DOWN and self.direction != 'up':
            self.direction = 'down'
        elif key == pygame.K_LEFT and self.direction != 'right':
            self.direction = 'left'
        elif key == pygame.K_RIGHT and self.direction != 'left':
            self.direction = 'right'
        else:
            pass

pygame.time.set_timer(pygame.USEREVENT, 120)
game = Board()
while game.over == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.USEREVENT:
            if game.snake.moving == 1:
                snake = game.snake.move(game.board)
                if snake == False:
                    game.over == True
                elif snake == True:
                    game.placeApple()
                elif snake == "over":
                    game.over = True
        elif event.type == pygame.KEYDOWN and event.key in arrowKeys:
            game.snake.changeDirection(event.key)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if game.snake.moving == 0:
                game.snake.moving = 1
                game.placeApple()
    game.update()
