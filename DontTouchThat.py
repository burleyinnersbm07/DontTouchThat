# A simple program that resembles the falling of stars or snow on a screen
# Coded in Python 2.7.10 with PyGame
# by Brett Burley-Inners :: 11/7/2015

import pygame, time, random, sys




pygame.init()




# Default dimensions of the game window (px)
display_width = 1280
display_height = 720




# Create a canvas to display the game on
gameScreen = pygame.display.set_mode((display_width, display_height))
# Title of the game Window
pygame.display.set_caption('Falling Stars')



# This is the player. He is a square. #sadlife
class Player:
    def __init__(self, playerSize, xPosition, xChange, yPosition, playerColor):
        self.xPosition = xPosition
        self.xChange = xChange
        self.yPosition = yPosition
        self.playerSize = playerSize
        self.playerColor = playerColor
        pygame.draw.rect(gameScreen, self.playerColor, [self.xPosition, self.yPosition, self.playerSize, self.playerSize])

    def moveLeft(self):
        self.xPosition -= playerSize

    def moveRight(self):
        self.xPosition += playerSize

    def movePlayer(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.K_LEFT:
                    xChange = -playerSize
                elif event.type == pygame.K_RIGHT:
                    xChange = playerSize

                    if self.xPosition < 0 or self.xPosition > display_width:
                        self.xPosition += 0
                    else:
                        self.xPosition += self.xChange



# Class that creates a star object
class Star:
    def __init__(self, starSize, xCoordinate, yCoordinate, starColor, fallSpeed, fallDirection):
        self.starSize = starSize
        self.xCoordinate = xCoordinate
        self.yCoordinate = yCoordinate
        self.starColor = starColor
        self.fallSpeed = fallSpeed
        self.fallDirection = fallDirection

    def fall(self):
        self.yCoordinate += self.fallSpeed
        self.xCoordinate += self.fallDirection
        pygame.draw.rect(gameScreen, self.starColor, [self.xCoordinate, self.yCoordinate, self.starSize, self.starSize])
        if self.yCoordinate > display_height:
            fallingStars.remove(self)

    def collideWithPlayer(self):

            return true


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





# variables for the while loop... 1's and 0's work too
starFall = True
makeStars = True


xPosition = 300
xChange = 0
size = 20


# Main loop for the falling star effect
while starFall:




    # refresh rate of gameScreen (times per second)
    clock.tick(60)




    # make the 'close'/'x' button work
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            starFall = False
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                xChange = -10
            if event.key == pygame.K_RIGHT:
                xChange = 10


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                xChange = 0


    # background color, drawn before the stars each time
    gameScreen.fill(darkGray)





    xPosition += xChange




    # keep making the stars...
    if makeStars:
        # stars going down
        fallingStars.append(Star(random.randrange(1, 20), random.randrange(1, display_width), -5, colorList[random.randrange(0, 6)], random.randrange(1, 10), random.randrange(-3, 3)))

        pygame.draw.rect(gameScreen, pink, [xPosition, 600, 40, 40])




    # for every star object in the list, run the fall function (make 'em "move")
    for i in fallingStars:
        i.fall()
        #print(len(fallingStars))
        # if the list is too big, remove the first item
        # for the computer's sake
        if len(fallingStars) > 10000:
            del fallingStars[0]





    # draw the screen
    pygame.display.update()

# That's all, folks!
