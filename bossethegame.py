import os, sys
import pygame
from pygame.locals import *

# exit program
def events():
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()

# display settings
W, H = 800, 800
HW, HH = W/2, H/2
AREA = W * H

# init display
pygame.init()
CLOCK = pygame.time.Clock()
DS = pygame.display.set_mode((W, H))
pygame.display.set_caption("Bosse the Game")
FPS = 120

# Colors
BLACK = (0, 0, 0, 255)
WHITE = (255, 255, 255, 255)
RED = (255, 0, 0, 255)
GREEN = (124, 252, 0, 255)

# Bosse
def bosse(x_pos, y_pos):
    pygame.draw.rect(DS, GREEN, [x_pos, y_pos, W/8, H/8])

# game loop
while True:
    events()

    bosse(0, 0)

    pygame.display.update()
    CLOCK.tick(FPS)
    DS.fill(WHITE)
