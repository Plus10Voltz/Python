import pygame

class Image:
    def __init__(self, mainSurface):
        self.mainSurface = mainSurface
        pygame.init()

    def drawImage(self):
        GREY = (69,69,69)
        pygame.draw.rect(self.mainSurface, GREY, (0,0,600,600), 0)
        pygame.display.update()

    def printMouseCoordinates(self, position):
        GREY = (69,69,69)
        self.mainSurface.fill((GREY))
        mouseFont = pygame.font.SysFont("Comic Sans MS", 32)
        mouseLabel = mouseFont.render(str(position), 1, (0,255,255))
        self.mainSurface.blit(mouseLabel, (30,30))
        pygame.display.update()
