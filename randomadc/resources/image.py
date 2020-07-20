import pygame
pygame.init()
# test = pygame.image.load("images\Draven.jpeg")
# mainSurface = pygame.display.set_mode((500,500), 0, 32)
# mainSurface.blit(test, (0,0))
# pygame.display.update()
class Image:
    def __init__(self, mainSurface):
        self.mainSurface = mainSurface
        pygame.init()

    def drawImage(self, champ):
        img = pygame.image.load("resources\images\{}.jpeg".format(champ))
        self.mainSurface.blit(img, (0,0))
        pygame.display.update()

    def printName(self, name):
        nameFont = pygame.font.SysFont("Comic Sans MS", 32)
        nameLabel = nameFont.render("{}".format(name), 1, (0,255,255))
        self.mainSurface.blit(nameLabel, (10,450))
        pygame.display.update()
