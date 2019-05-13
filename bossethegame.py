import os
import sys
import time
import pygame
from pygame.locals import *

# settings
W, H = 800, 800
AREA = W * H
W_STEP = W/8
H_STEP = H/8
SPEED = 1

# init display
pygame.init()
DS = pygame.display.set_mode((W, H))
pygame.display.set_caption("Bosse the Game")
FPS = 30

# init settings
CLOCK = pygame.time.Clock()
START_TIME = 0

# Colors
BLACK = (0, 0, 0, 255)
WHITE = (255, 255, 255, 255)
RED = (255, 0, 0, 255)
GREEN = (124, 252, 0, 255)

# Classes
class Body:

    def __init__(self, color, width, height, x_pos, y_pos):
        self.color = color
        self.width = width
        self.height = height
        self.x_pos = x_pos
        self.y_pos = y_pos

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def moveY(self, y_pos):
        self.y_pos = y_pos

    def moveX(self, x_pos):
        self.x_pos = x_pos

    def getY(self):
        return self.y_pos
    
    def getX(self):
        return self.x_pos
    
    def draw(self):
        drawRect(self.color, self.width, self.height, self.x_pos, self.y_pos)

class Bosse(Body):
    
    color = GREEN
    width = W_STEP
    height = H_STEP

    def __init__(self, x_pos):
        return super().__init__(self.color, self.width, self.height, x_pos, (H - H_STEP))

    def moveRight(self, step):
        if self.x_pos + step < W:
            self.moveX(self.x_pos + step)
    
    def moveLeft(self, step):
        if self.x_pos - step >= 0:
            self.moveX(self.x_pos - step)

class Baddie(Body):

    color = RED
    width = W_STEP
    height = H_STEP
    init_y = 0

    def __init__(self, x_pos):
        return super().__init__(self.color, self.width, self.height, x_pos, self.init_y)

    def move(self):
        self.y_pos += self.y_pos + 1

# various help methods
def drawRect(color, width, height, x_pos, y_pos):
    pygame.draw.rect(DS, color, [x_pos, y_pos, width, height])

# game variables
bosse = Bosse(0)
baddies = []
score = 0
move_ticks = 0
last_tick = 0


# runtime methods
def events():
    global bosse


    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                print("Right pressed")
                bosse.moveRight(W_STEP)
            if event.key == K_LEFT:
                print("Left pressed")
                bosse.moveLeft(W_STEP)
    
def drawBaddies():
    global baddies

    for baddie in baddies:
        baddie.draw()

def moveBaddies():
    global baddies

    for baddie in baddies:
        baddie.move()

def checkCollision():
    global bosse
    global baddies

    for baddie in baddies:
        if (baddie.getY() + baddie.getHeight()) >= bosse.getY():
            if (baddie.getX() + baddie.getWidth()) >= bosse.getX():
                print("Collision")
            

# game loop
while True:
    events()
    
    move_ticks = round(pygame.time.get_ticks() / 1000)

    if move_ticks != last_tick:
        print("Seconds elapsed: ", move_ticks)
        print("Score: ", score)
        last_tick = move_ticks

    bosse.draw()
    drawBaddies()


    pygame.display.update()
    CLOCK.tick(FPS)
    DS.fill(WHITE)