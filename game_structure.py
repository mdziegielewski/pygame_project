import pygame
from sys import exit

pygame.init()   #game setup

width = 900     #game screen dimension
height = 700
rescale = 3
rescaleBall = 2
screenDim = (width, height)


screen = pygame.display.set_mode(screenDim)     #screen display

pygame.display.set_caption("First game")


def grass_method():
    grassImage = pygame.image.load("grass.png").convert()
    grassImage = pygame.transform.scale(grassImage,
                                        (screenDim))
    screen.blit(grassImage, (0, 0))


def player_method():
    player = pygame.image.load("characterBody.png").convert_alpha()
    playerWidth = player.get_rect().width
    playerHeight = player.get_rect().height
    player = pygame.transform.scale(player,
                                    (playerWidth * rescale,
                                     playerHeight * rescale))
    player = pygame.transform.rotate(player, 90)
    screen.blit(player, (0, 0))


def foot_method():
    foot = pygame.image.load("characterFoot.png").convert_alpha()
    footWidth = foot.get_rect().width
    footHeight = foot.get_rect().height
    foot = pygame.transform.scale(foot,
                                  (footWidth * rescale,
                                   footHeight * rescale))
    foot = pygame.transform.rotate(foot, 90)
    screen.blit(foot, (0, 0))


def ball_method():
    ball = pygame.image.load("ball.png").convert_alpha()
    ballWidth = ball.get_rect().width
    ballHeight = ball.get_rect().height
    ball = pygame.transform.scale(ball,
                                  (ballWidth * rescaleBall,
                                   ballHeight * rescaleBall))
    screen.blit(ball, (0, 0))



grass_method()
player_method()
foot_method()
ball_method()


finished = False
while finished == False:
    for event in pygame.event.get():    #processing all the events
        if event.type == pygame.QUIT:
            finished = True
            pygame.quit()   #close the screen
            exit()

    pygame.display.flip()   #screen/frame update