import pygame, sys
import resources.main

game = resources.main.Game()
pygame.display.set_caption("Click Speed Test")
clock = pygame.time.Clock()
pygame.time.set_timer(pygame.USEREVENT, 1000)
counter, text = 5, '5'.rjust(3)

gameFont = pygame.font.SysFont("Comic Sans MS", 30)

while not game.over:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if game.counter > 0:
                game.score += 1
        if event.type == pygame.USEREVENT:
            if game.counter > 0:
                if game.score >= 1:
                    game.counter -= 1
            elif game.counter == 0:
                game.score = game.score / 5
                game.counter -= 1
            elif game.counter < 0:
                game.over = True
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        else:
            clock.tick(60)
            continue
    game.update()
while game.over:
    game.gameOver()
