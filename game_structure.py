import pygame
from sys import exit

pygame.init()   #game setup

width = 900     #game screen dimension
height = 700
screenDim = (width, height)

screen = pygame.display.set_mode(screenDim)     #screen display

pygame.display.set_caption("First game")


finished = False
while finished == False:
    for event in pygame.event.get():    #processing all the events
        if event.type == pygame.QUIT:
            finished = True
            pygame.quit()   #close the screen
            exit()

    pygame.display.flip()   #screen/frame update