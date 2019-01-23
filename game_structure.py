import pygame
from sys import exit
import math

pygame.init()   #game setup


def cropSurface(newWidth, newHeight, cropWidth, cropHeight, image):

    newSurf = pygame.Surface((newWidth, newHeight),
                             pygame.SRCALPHA, 32)   #32 bytes
    newSurf.blit(image, (0, 0), (cropWidth, cropHeight,
                                 newWidth, newHeight))
    return newSurf

def movePlayer(direction, radius, absRot):
    yChange = 5
    deltaTheta = int(90/(radius/yChange))
    if direction == "left":
        deltaTheta *= -1

    finalRot = (absRot + deltaTheta)*math.pi/180

    hypotenuse = radius * math.sin(finalRot) / (math.sin((math.pi-finalRot) / 2))

    newX = hypotenuse * math.cos(math.pi/2-(math.pi-finalRot)/2)
    newY = hypotenuse * math.sin(math.pi/2-(math.pi-finalRot)/2)

    return newX, newY, absRot + deltaTheta



width = 900     #game screen dimension
height = 700
rescale = 3
rescaleBall = 2
screenDim = (width, height)


screen = pygame.display.set_mode(screenDim)     #screen display

pygame.display.set_caption("First game")


grassImage = pygame.image.load("images/grass.png").convert()
grassImage = pygame.transform.scale(grassImage,
                                (screenDim))
screen.blit(grassImage, (0, 0))



player = pygame.image.load("images/characterBody.png").convert_alpha()
playerWidth = player.get_rect().width
playerHeight = player.get_rect().height
player = pygame.transform.scale(player,
                                (playerWidth * rescale,
                                 playerHeight * rescale))
player = pygame.transform.rotate(player, 90)
currentRotation = 0
playerStart = player

# screen.blit(player, (0, 0))



foot = pygame.image.load("images/characterFoot.png").convert_alpha()
footWidth = foot.get_rect().width
footHeight = foot.get_rect().height
foot = pygame.transform.scale(foot,
                              (footWidth * rescale,
                               footHeight * rescale))
foot = pygame.transform.rotate(foot, 90)
footStart = foot
# screen.blit(foot, (0, 0))



ball = pygame.image.load("images/ball.png").convert_alpha()
ballWidth = ball.get_rect().width
ballHeight = ball.get_rect().height
ball = pygame.transform.scale(ball,
                              (ballWidth * rescaleBall,
                               ballHeight * rescaleBall))
# screen.blit(ball, (0, 0))


goalLeft = pygame.image.load("images/goalLeft.png").convert_alpha()
goalLeft = pygame.transform.scale(goalLeft, (250, 270))
goalLeftWidth = goalLeft.get_rect().width
goalLeftHeight = goalLeft.get_rect().height
goalLeft = cropSurface(goalLeftWidth/2+12,
                       goalLeftHeight/2+12,
                       goalLeftWidth/2-12,
                       goalLeftHeight/2-12,
                       goalLeft)
# screen.blit(goalLeft, (0, 0))




goalMid = pygame.image.load("images/goalMiddle.png").convert_alpha()
goalMid = pygame.transform.scale(goalMid, (250, 270))
goalMidWidth = goalMid.get_rect().width
goalMidHeight = goalMid.get_rect().height
goalMid = cropSurface(goalMidWidth,
                      goalMidHeight/2+12,
                      0,
                      goalMidHeight/2-12,
                      goalMid)
# screen.blit(goalMid, (137, 0))


goalRight = pygame.image.load("images/goalRight.png").convert_alpha()
goalRight = pygame.transform.scale(goalRight, (250, 270))
goalRightWidth = goalRight.get_rect().width
goalRightHeight = goalRight.get_rect().height
goalRight = cropSurface(goalRightWidth/2+12,
                        goalRightHeight/2+12,
                        0,
                        goalRightHeight/2-12,
                        goalRight)
# screen.blit(goalRight, (387, 0))






goalStart = (width - goalLeft.get_rect().width - goalMid.get_rect().width - goalRight.get_rect().width)/2
screen.blit(goalLeft, (goalStart, 0))
screen.blit(goalMid, (goalStart+goalLeft.get_rect().width, 0))
screen.blit(goalRight, (goalStart+goalLeft.get_rect().width+goalMid.get_rect().width, 0))

playerX = width/2
playerY = 530
playerXOriginal = playerX
playerYOriginal = playerY

screen.blit(player, (playerX-player.get_rect().width/2, playerY-player.get_rect().height))

ballX = width/2
ballY = 450
radius = playerY - ballY

screen.blit(ball, (ballX-ball.get_rect().width/2, ballY-ball.get_rect().height))







frame = pygame.time.Clock() #max frame rate
finished = False

while finished == False:
    for event in pygame.event.get():    #processing all the events
        if event.type == pygame.QUIT:
            finished = True
            pygame.quit()   #close the screen
            exit()

    pressedKeys = pygame.key.get_pressed() #"event listener"

    if pressedKeys[pygame.K_LEFT] == True:
        changeX, changeY, currentRotation = movePlayer("left", radius, currentRotation)
        player = pygame.transform.rotate(playerStart, currentRotation)
        playerX = playerXOriginal + changeX
        playerY = playerYOriginal - changeY

    elif pressedKeys[pygame.K_RIGHT] == True:
        changeX, changeY, currentRotation = movePlayer("right", radius, currentRotation)
        player = pygame.transform.rotate(playerStart, currentRotation)
        playerX = playerXOriginal + changeX
        playerY = playerYOriginal - changeY

    elif pressedKeys[pygame.K_SPACE] == True:
        pass


    screen.blit(grassImage, (0, 0))
    screen.blit(goalLeft, (goalStart, 0))
    screen.blit(goalMid, (goalStart + goalLeft.get_rect().width, 0))
    screen.blit(goalRight, (goalStart + goalLeft.get_rect().width + goalMid.get_rect().width, 0))
    screen.blit(ball, (ballX - ball.get_rect().width / 2, ballY - ball.get_rect().height))
    screen.blit(player, (playerX - player.get_rect().width / 2, playerY - player.get_rect().height))
    pygame.display.flip()   #screen/frame update
    frame.tick(30)    #max frame rate
