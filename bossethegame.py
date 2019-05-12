import os, sys
import pygame
from pygame.locals import *

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

# gamestate
w_step = W/8
h_step = H/8
bosse_xpos = 0

# Body
def body(x_pos, y_pos, color):
    body_w = w_step
    body_h = h_step
    pygame.draw.rect(DS, color, [x_pos, y_pos, w_step, h_step])

# Bosse
def bosse(x_pos, y_pos):
    body(x_pos, y_pos, GREEN)

# Baddie
def baddie(x_pos, y_pos):
    body(x_pos, y_pos, RED)


def events():
    global bosse_xpos

    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()
        if event.type == KEYUP:
            if event.key == K_RIGHT:
                print("Right pressed")
                if bosse_xpos + w_step < W:
                    bosse_xpos += w_step
            if event.key == K_LEFT:
                print("Left pressed")
                if bosse_xpos - w_step >= 0:
                    bosse_xpos -= w_step

# game loop
while True:
    events()

    bosse(bosse_xpos, (H - w_step))

    pygame.display.update()
    CLOCK.tick(FPS)
    DS.fill(WHITE)
