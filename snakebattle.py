import pygame, sys
from pygame.locals import *

## window dimensions
TILE_SIZE = 12
TILES_X = 70
TILES_Y = 50

## colors
COLOR_BG = (30, 30, 30) # background
COLOR_FG = (255, 255, 255) # foreground
COLOR_P1 = (255, 30, 30) # player 1
COLOR_P2 = (30, 255, 30) # player 2
COLOR_FD = (255, 200, 30) # food
COLOR_DB = (50, 150, 250) # debug

## settings
TPS = 12 # ticks lock
DEBUG = True # debugging

## tiles to pixels
def get_dimension(x, y, width = 0, height = 0):
    return (x * TILE_SIZE, y * TILE_SIZE, width * TILE_SIZE, height * TILE_SIZE)
  
## init
pygame.init()
pygame.display.set_caption('Snake Battle by Scriptim')
CLOCK = pygame.time.Clock()
DISPLAY_SURFACE = pygame.display.set_mode((TILE_SIZE * TILES_X, TILE_SIZE * TILES_Y))
DISPLAY_SURFACE.fill(COLOR_BG)

## fonts (change font files here)
FONT_DB = pygame.font.Font(None, 20) # debug font
FONT_SC = pygame.font.Font(None, 60) # score

## directions
UP = (0, -1)
RIGHT = (-1, 0)
DOWN = (0, 1)
LEFT = (1, 0)

## game over
game_over = False

## main loop
while not game_over:
    ## event queue
    for event in pygame.event.get():
        ## QUIT event
        if event.type == QUIT:
            print("## Quit ##")
            pygame.quit()
            sys.exit()

    ## update
    pygame.display.update()
    
pygame.time.wait(4000)
