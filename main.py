import pygame
import os
import grid

os.environ["SDL_VIDEO_CEMTERED"]='1'

# Set game screen size
width = 1250
height = 720
dimensions = (width,height)

# Init game
pygame.init()
pygame.display.set_caption(" Game Of Life") # Tittle
screen = pygame.display.set_mode(dimensions)
clock = pygame.time.Clock()

# Set FPS rate
fps = 60

# Set colors
black = (0,0,0)
red = (255,0,0)
white = (255,255,255)

# Set scaler and offset
scaler = 15
offset = 1

# Set Grid dimensions
Grid = grid.Grid(width,height,scaler,offset)
Grid.random_array()

run = True
while run:
    clock.tick(fps)
    screen.fill(black)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    Grid.game(off_color=white,on_color=red,surface=screen)

    pygame.display.update()

pygame.quit()
