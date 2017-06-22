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

## players
class Player:
    x = None
    y = None
    left = False
    right = False
    direction = None
    length = 2
    tail = []

    def turn(self):
        if self.right:
            if self.direction == UP:
                self.direction = LEFT
            elif self.direction == RIGHT:
                self.direction = UP
            elif self.direction == DOWN:
                self.direction = RIGHT
            elif self.direction == LEFT:
                self.direction = DOWN
        elif self.left:
            if self.direction == UP:
                self.direction = RIGHT
            elif self.direction == RIGHT:
                self.direction = DOWN
            elif self.direction == DOWN:
                self.direction = LEFT
            elif self.direction == LEFT:
                self.direction = UP

p1 = Player()
p1.x = 4
p1.y = TILES_Y / 2 + 5
p1.direction = UP
p1.tail = [(p1.x, p1.y - 1), (p1.x, p1.y - 2)]

p2 = Player()
p2.x = TILES_X - 5
p2.y = TILES_Y / 2 + 5
p2.direction = UP
p2.tail = [(p2.x, p2.y - 1), (p2.x, p2.y - 2)]

## main loop
while not game_over:
    ## event queue
    for event in pygame.event.get():
        ## QUIT event
        if event.type == QUIT:
            print("## Quit ##")
            pygame.quit()
            sys.exit()
        ## keyboard mode
        elif event.type == KEYDOWN:
            if event.key == K_a:
                p1.left = True
                p1.right = False
                p1.turn()
            elif event.key == K_d:
                p1.right = True
                p1.left = False
                p1.turn()
            elif event.key == K_LEFT:
                p2.left = True
                p2.right = False
                p2.turn()
            elif event.key == K_RIGHT:
                p2.right = True
                p2.left = False
                p2.turn()

    p1.left = False
    p1.right = False
    p2.left = False
    p2.right = False

    ## clear
    DISPLAY_SURFACE.fill(COLOR_BG)

    ## draw head
    pygame.draw.rect(DISPLAY_SURFACE, COLOR_P1, get_dimension(p1.x, p1.y, 1, 1))
    pygame.draw.rect(DISPLAY_SURFACE, COLOR_P2, get_dimension(p2.x, p2.y, 1, 1))

    ## move head
    p1.x += p1.direction[0]
    p1.y += p1.direction[1]
    p2.x += p2.direction[0]
    p2.y += p2.direction[1]

    ## update
    pygame.display.update()
    
pygame.time.wait(4000)
