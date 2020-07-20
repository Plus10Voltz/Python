import pygame, sys, time, random
from pygame.locals import *
from resources.image import Image
f = open("resources\ADCS.txt", "r")
champs = []
sounds = []
for i in f:
    champs.append(i[0:-1])
pygame.init()
spin = pygame.mixer.Sound("resources\\audio\Spin.ogg")
for champion in champs:
    sounds.append(pygame.mixer.Sound("resources\\audio\{}.ogg".format(champion)))
mainSurface = pygame.display.set_mode((500,500), 0, 32)
pygame.display.set_caption("Random Champion Selector V2")
_nameFont = pygame.font.SysFont("Comic Sans MS", 32)
_nameLabel = _nameFont.render("Click for a random ADC",1,(255,255,255))
mainSurface.blit(_nameLabel, (75,250))
pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            pygame.mixer.stop()
            pygame.mixer.Sound.play(spin)
            select = Image(mainSurface)
            for i in range(50):
                champ = random.choice(champs)
                select.drawImage(champ)
                select.printName(champ)
                time.sleep(0.01)
            champ = random.choice(champs)
            select.drawImage(champ)
            select.printName(champ)
            x = champs.index(champ)
            pygame.mixer.stop()
            pygame.mixer.Sound.play(sounds[x])
