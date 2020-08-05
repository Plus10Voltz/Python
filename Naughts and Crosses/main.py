import pygame, sys
pygame.init()

WIDTH, HEIGHT = 200, 200
MARGIN = 5

class Game:
    def __init__(self):
        self.playerTurn = 0
        self.font = pygame.font.SysFont("Comic Sans MS", 180)
        self.endFont = pygame.font.SysFont("Comic Sans MS", 50)
        self.board = [[0 for x in range(3)] for y in range(3)]
        self.FPS = 60
        self.clock = pygame.time.Clock()
        self.over = False
        self.display = pygame.display.set_mode((620,620))
        self.winner = 0

    def debugBoard(self):
        for i in self.board:
            for j in i:
                print(j,end=' ')
            print()
        print()

    def displayBoard(self):
        w = self.font.render(" ", 1, (0,0,0))
        xpos = 0
        ypos = 0
        for i in self.board:
            for j in i:
                if j == 0:
                    w = self.font.render(" ", 1, (0,0,0))
                elif j == "x":
                    w = self.font.render("X", 1, (0,0,0))
                elif j == "o":
                    w = self.font.render("O", 1, (0,0,0))
                else:
                    w = self.font.render(" ", 1, (0,0,0))
                row = 205 * xpos + 35
                col = 205 * ypos - 35
                self.display.blit(w, (row, col))
                if xpos == 2:
                    xpos = 0
                    ypos += 1
                else:
                    xpos += 1
                pass

    def drawGrid(self):
        colour = (255,255,255)
        for i in range(3):
            for j in range(3):
                pygame.draw.rect(self.display, colour, (i * (WIDTH + MARGIN) + MARGIN,
                j * (HEIGHT + MARGIN) + MARGIN, WIDTH, HEIGHT))

    def onClick(self):
        pos = pygame.mouse.get_pos()
        col = pos[0] // (WIDTH + MARGIN)
        row = pos[1] // (HEIGHT + MARGIN)
        if self.playerTurn == 0:
            if self.board[row][col] == 0:
                self.board[row][col] = "x"
        else:
            if self.board[row][col] == 0:
                self.board[row][col] = "o"

    def update(self):
        self.clock.tick(self.FPS)
        self.display.fill((135,135,135))
        self.drawGrid()
        self.displayBoard()
        self.checkWin()
        pygame.display.update()

    def changeElement(self):
        pos = pygame.mouse.get_pos()
        col = pos[0] // (WIDTH + MARGIN)
        row = pos[1] // (HEIGHT + MARGIN)
        self.board[row][col] = 1

    def checkWin(self):
        for row in range (0, 3):
            if ((self.board [row][0] == self.board[row][1] == self.board[row][2]) and (self.board [row][0] is not 0)):
                self.winner = self.board[row][0]
                pygame.draw.line(self.display, (250,0,0), (75, 100 + (200*row) + 5*(row+1)),(545, 100 + (200*row) + 5*(row+1)), 20)
                break
        for col in range (0, 3):
            if ((self.board [0][col] == self.board[1][col] == self.board[2][col]) and (self.board [0][col] is not 0)):
                self.winner = self.board[0][col]
                pygame.draw.line(self.display, (250,0,0), (100 + (200*col) + 5*(col+1), 75),(100 + (200*col) + 5*(col+1), 545), 20)
                break
        if ((self.board [0][0] == self.board[1][1] == self.board[2][2]) and (self.board [0][0] is not 0)):
            self.winner = self.board[0][0]
            pygame.draw.line(self.display, (255,0,0), (105,105),(545,545), 30)
        if ((self.board [0][2] == self.board[1][1] == self.board[2][0]) and (self.board [0][2] is not 0)):
            self.winner = self.board[0][2]
            pygame.draw.line(self.display, (255,0,0), (545,105-50),(105,545-50), 30)

    def showEndScreen(self):
        s = pygame.Surface((620,620), pygame.SRCALPHA)
        s.fill((255,255,255, 10))
        self.display.blit(s, (0,0))
        endText = self.endFont.render("Player {} Wins!".format(game.playerTurn+1), 1, (0,0,0))
        text = endText.get_rect(center=(310,310))
        game.display.blit(endText, text)
        pygame.display.update()

#-----------[ Main Game ]-----------#

debug = False

pygame.display.set_caption("Tic Tac Toe")
game = Game()
pygame.time.set_timer(pygame.USEREVENT, 1000)
game.drawGrid()

while __name__ == '__main__':
    while not game.over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if game.winner == 0 or game.winner == "0":
                    game.onClick()
                    game.checkWin()
                    if debug == True:
                        print(game.winner)
                        game.debugBoard()
                else:
                    game.over = True
                if game.playerTurn == 0:
                    game.playerTurn += 1
                else:
                    game.playerTurn -= 1
        game.update()

    #-----------[ Game Over Screen ]-----------#

    while game.over:
        game.showEndScreen()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pygame.quit()
                sys.exit()
