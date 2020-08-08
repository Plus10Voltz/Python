debug = False
import pygame, sys
from math import inf as infinity
from random import choice
import time
import main

pygame.init()

pygame.display.set_caption("Tic Tac Toe")
game = main.Game()
pygame.time.set_timer(pygame.USEREVENT, 1000)
game.drawGrid()

while not game.over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if game.winner == 0 or game.winner == "0":
                if debug == True:
                    # print(game.winner)
                    print(game.playerTurn)
                    # game.debugBoard()
                if game.playerTurn == 0:
                    if game.onClick(None, None, "player") == True:
                        game.checkWin()
                        game.update()
                        game.aiTurn()
                        game.checkWin()
                        game.update()
            else:
                game.over = True
    game.update()

while game.over:
    game.showEndScreen()
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pygame.quit()
            sys.exit()
