# A simple program that resembles the falling of stars or snow on a screen
# Coded in Python 2.7.10 with PyGame
# by Brett Burley-Inners :: 11/7/2015

import pygame, time, random, sys

pygame.init()

# Default dimensions of the game window (px) test
display_width = 320
display_height = 240

# Create a canvas to display the game on
gameScreen = pygame.display.set_mode((display_width, display_height))
# Title of the game Window
pygame.display.set_caption('Falling Stars')

# This is the player. He is a square. #sadlife
class Player:
    def __init__(self, playerSize, xPosition, yPosition, playerColor, display_width):
        self.xPosition = xPosition
        self.yPosition = yPosition
        self.playerSize = playerSize
        self.playerColor = playerColor
        self.display_width = display_width
        pygame.draw.rect(gameScreen, self.playerColor, [self.xPosition, self.yPosition, self.playerSize, self.playerSize])

    def getPlayerSize(self):
        return self.playerSize

    def getPlayerX(self):
        return self.xPosition

    def getPlayerY(self):
        return self.yPosition

    def redrawPlayer(self, newXPosition):
        self.xPosition = newXPosition
        pygame.draw.rect(gameScreen, self.playerColor, [self.xPosition, self.yPosition, self.playerSize, self.playerSize])

    def isOverLeftBound(self):
        if self.xPosition <= 0:
            return True
        else:
            return False

    def isOverRightBound(self):
        if self.xPosition >= self.display_width - self.playerSize:
            return True
        else:
            return False

# Class that creates a star object
class Star:
    def __init__(self, starSize, xCoordinate, yCoordinate, starColor, fallSpeed, fallDirection, score):
        self.starSize = starSize
        self.xCoordinate = xCoordinate
        self.yCoordinate = yCoordinate
        self.starColor = starColor
        self.fallSpeed = fallSpeed
        self.fallDirection = fallDirection
        self.score = 0

    def fall(self):
        self.yCoordinate += self.fallSpeed
        self.xCoordinate += self.fallDirection
        pygame.draw.rect(gameScreen, self.starColor, [self.xCoordinate, self.yCoordinate, self.starSize, self.starSize])
        if self.yCoordinate > display_height:
            fallingStars.remove(self)
            self.score += 1

    def returnScore(self):
        return self.score

    def collideWithPlayer(self, objectX, objectY, objectSize):
        if self.yCoordinate + self.starSize >= objectY and self.yCoordinate <= objectY + objectSize:
            if self.xCoordinate >= objectX and self.xCoordinate + self.starSize <= objectX + objectSize:
                return True
        if self.yCoordinate + self.starSize >= objectY and self.yCoordinate <= objectY + objectSize:
            if self.xCoordinate <= objectX + objectSize and self.xCoordinate + self.starSize >= objectX:
                return True
        else:
            return False

font = pygame.font.SysFont(None, 25)

# Colors
white = (255, 255, 255)
darkGray = (50, 50, 50)
darkerGray = (25, 25, 25)
darkestGray = (10, 10, 10)
lightGray = (150, 150, 150)
rLightGray = (200, 200, 200)
rrLightGray = (220, 220, 220)
black = (0, 0, 0)
red = (245, 0, 0)
darkRed = (150, 0, 0)
green = (0, 235, 0)
darkGreen = (0, 150, 0)
lightBlue = (55, 210, 225)
blue = (0, 0, 215)
darkBlue = (0, 0, 115)
pink = (225, 55, 135)

# List of colors
colorList = []
colorList.append(darkerGray)
colorList.append(darkestGray)
colorList.append(lightGray)
colorList.append(rLightGray)
colorList.append(rrLightGray)
colorList.append(lightBlue)

# Clock and FPS stuff
clock = pygame.time.Clock()

# List to maintain star objects
fallingStars = []

clockTickTimer = 0

# variables for the while loop... 1's and 0's work too
RUNNING = True
makeStars = True

score = 0
xChange = 0
xPosition = display_width / 2
size = 20
pygame.key.set_repeat(1, 5)

player = Player(30, xPosition, display_height - 50, pink, display_width)


# Main loop for the falling star effect
while RUNNING:

    # refresh rate of gameScreen (times per second)
    clock.tick(30)



    # make the 'close'/'x' button work
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            starFall = False
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and not isOverLeftBound:
                xChange -= 10
                #print("left")
            if event.key == pygame.K_RIGHT and not isOverRightBound:
                xChange += 10
                #print("right")

        #if pygame.key.get_pressed()[pygame.K_LEFT]:
        #    xChange = -10
        #    print("left pressed")
        #elif pygame.key.get_pressed()[pygame.K_RIGHT]:
        #    xChange += 10
        #    print("right pressed")

    # background color, drawn before the stars each time
    gameScreen.fill(darkGray)

    #print(clock.tick())

    font = pygame.font.SysFont("monospace", 25)
    message = font.render(str(score), True, lightGray)
    gameScreen.blit(message, (15, 15))

    clockTickTimer += 1
    #print (clock.get_fps())

    xPosition += xChange
    #print(xPosition)

    player.redrawPlayer(xPosition)
    isOverLeftBound = player.isOverLeftBound()
    isOverRightBound = player.isOverRightBound()
    #print(isOverLeftBound)
    #print(isOverRightBound)
    xChange = 0
    #print(xPosition)
    #print(display_width)

    # keep making the stars...
    if makeStars and clockTickTimer > 20:

        # stars going down
        fallingStars.append(Star(random.randrange(1, 20), random.randrange(1, display_width), -5, colorList[random.randrange(0, 6)], random.randrange(1, 2), random.randrange(-1, 2)/2, score))

        clockTickTimer = 0

    # for every star object in the list, run the fall function (make 'em "move")
    for i in fallingStars:
        i.fall()
        score += i.returnScore()
        #print(score)
        #print(len(fallingStars))
        # if the list is too big, remove the first item
        # for the computer's sake
        if len(fallingStars) > 10000:
            del fallingStars[0]
        if i.collideWithPlayer(player.getPlayerX(), player.getPlayerY(), player.getPlayerSize()):
            makeStars = False
            del fallingStars[:]


    # draw the screen
    pygame.display.update()

#game over code
# That's all, folks!
