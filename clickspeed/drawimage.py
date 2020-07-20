import pygame, sys
from pygame.locals import *
import image

pygame.init()
mainSurface = pygame.display.set_mode((600,600),0,32)
pygame.display.set_caption("Click Speed Test")
myImage = image.Image(mainSurface)
myImage.drawImage()
clicks = 0

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            start_ticks = pygame.time.get_ticks()
            clicks += 1
            myImage.printMouseCoordinates(pygame.mouse.get_pos())
            while True:
                seconds = (pygame.time.get_ticks()-start_ticks)/1000
                if seconds > 5:
                    break
                elif pygame.event.get() == MOUSEBUTTONDOWN:
                    clicks += 1
                print("Clicks: {} -- {}".format(clicks, seconds))
