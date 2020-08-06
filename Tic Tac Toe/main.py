import pygame, sys
from math import inf as infinity
from random import choice
import time
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
        self.HUMAN = -1
        self.COMP = +1

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
                elif j == -1:
                    w = self.font.render("X", 1, (0,0,0))
                elif j == +1:
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

    def onClick(self, x, y, player):
        if player == "player":
            pos = pygame.mouse.get_pos()
            col = pos[0] // (WIDTH + MARGIN)
            row = pos[1] // (HEIGHT + MARGIN)
            if self.playerTurn == 0:
                if self.board[row][col] == 0:
                    self.board[row][col] = -1
        else:
            self.board[x][y] = +1

    def update(self):
        self.clock.tick(self.FPS)
        self.display.fill((135,135,135))
        self.drawGrid()
        self.displayBoard()
        self.checkWin()
        pygame.display.update()

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
        if self.tied() == True:
            self.over = True

    def showEndScreen(self):
        s = pygame.Surface((620,620), pygame.SRCALPHA)
        s.fill((255,255,255, 10))
        self.display.blit(s, (0,0))
        if self.tied() == True:
            endText = self.endFont.render("Tied!", 1, (0,0,0))
        else:
            endText = self.endFont.render("Player {} Wins!".format(game.playerTurn+1), 1, (0,0,0))
        text = endText.get_rect(center=(310,310))
        self.display.blit(endText, text)
        pygame.display.update()

    def tied(self):
        x = []
        for i in self.board:
            for item in i:
                x.append(item)
        if 0 in x:
            pass
        else:
            return True

    def evaluate(self, state):
        if self.wins(state, self.COMP):
            score = +1
        elif self.wins(state, self.HUMAN):
            score = -1
        else:
            score = 0
        return score

    def wins(self, state, player):
        winState = [
            [state[0][0], state[0][1], state[0][2]],
            [state[1][0], state[1][1], state[1][2]],
            [state[2][0], state[2][1], state[2][2]],
            [state[0][0], state[1][0], state[2][0]],
            [state[0][1], state[1][1], state[2][1]],
            [state[0][2], state[1][2], state[2][2]],
            [state[0][0], state[1][1], state[2][2]],
            [state[2][0], state[1][1], state[0][2]],
        ]
        if [player, player, player] in winState:
            return True
        else:
            return False

    def gameOver(self, state):
        return self.wins(state, self.HUMAN) or self.wins(state, self.COMP)

    def emptyCells(self, state):
        cells = []
        for x, row in enumerate(state):
            for y, cell in enumerate(row):
                if cell == 0:
                    cells.append([x, y])
        return cells

    def minimax(self, state, depth, player):
        if player == self.COMP:
            best = [-1, -1, -infinity]
        else:
            best = [-1, -1, +infinity]
        if depth == 0 or self.gameOver(state):
            score = self.evaluate(state)
            return [-1, -1, score]

        for cell in self.emptyCells(state):
            x, y = cell[0], cell[1]
            state[x][y] = player
            score = self.minimax(state, depth - 1, -player)
            state[x][y] = 0
            score[0], score[1] = x, y
            if player == self.COMP:
                if score[2] > best[2]:
                    best = score  # max value
            else:
                if score[2] < best[2]:
                    best = score  # min value
        return best

    def aiTurn(self):
        depth = len(self.emptyCells(self.board))
        if depth == 0:
            return
        move = self.minimax(self.board, depth, self.COMP)
        x,y = move[0], move[1]
        self.onClick(x,y,"bot")
        # time.sleep(1)
