import pygame, sys
from resources.balloonClass import Balloon
from resources.main import Game

game = Game()
pygame.time.set_timer(pygame.USEREVENT, 400)
TIMESPEED = pygame.USEREVENT + 1
pygame.time.set_timer(TIMESPEED, 7000)
largeFont = pygame.font.SysFont('Comic Sans MS', 40)
gameOverFont = pygame.font.SysFont('Comic Sans MS', 60)
while not game.over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.over = True
        if event.type == pygame.USEREVENT:
            game.spawnBalloon()
            if game.score > 100 and game.score < 250:
                game.spawnBalloon()
            elif game.score > 250 and game.score < 500:
                game.spawnBalloon()
                game.spawnBalloon()
            elif game.score > 500 and game.score < 1000:
                for i in range(0,3):
                    game.spawnBalloon()
            elif game.score == 1000:
                game.over = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            game.checkclick(event.pos)
        if event.type == TIMESPEED:
            game.speedup()
    game.update()
while game.over:
    game.display.fill((0,0,0))
    finalScore = largeFont.render('Score: {}'.format(str(game.score)), 1, (255,255,255))
    textRect = finalScore.get_rect(center=(450,450))
    if game.score == 1000:
        gameOver = gameOverFont.render('Fuck you cheater!',1,(255,255,255))
    else:
        gameOver = gameOverFont.render('Game Over',1,(255,255,255))
    textGameOver = gameOver.get_rect(center=(450,350))
    game.display.blit(finalScore, textRect)
    game.display.blit(gameOver, textGameOver)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.quit()
            sys.exit()
# helloo
