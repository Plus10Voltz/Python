import pygame, sys
import resources.main
from pygame.locals import *

pygame.display.set_caption("Minesweeper")
game = resources.main.Game()
pygame.time.set_timer(pygame.USEREVENT, 1000)
game.drawGrid()

while not game.over:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            game.onClick()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            print("Right Click")
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    game.update()
