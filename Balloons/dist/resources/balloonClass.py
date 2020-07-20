import pygame, random, time

class Balloon(pygame.sprite.Sprite):
    def __init__(self, speed):
        pygame.sprite.Sprite.__init__(self)
        listimage = [pygame.image.load('resources\\blueBalloon.png'),pygame.image.load('resources\\redBalloon.png'),pygame.image.load('resources\\greenBalloon.png')]
        self.image = random.choice(listimage)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(100,700)
        self.rect.y = random.randint(800,1000)
        self.speed = speed

    def up(self):
        self.rect.y -= self.speed

    def update(self):
        self.up()

    def balloonPop(self): #To be implemented
        self.image = (pygame.image.load("resources\pop.png"))
        self.update()
        self.kill()
