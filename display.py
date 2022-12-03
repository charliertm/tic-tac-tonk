import numpy as np
import pygame as pg
import sys

#set display vars
(SCREEN_WIDTH, SCREEN_HEIGHT) = (600, 600)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
CELLS_WIDTH = 3
CELLS_HEIGHT = 3

screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
running = True

#initialise display
screen.fill(WHITE)
pg.display.set_caption("Tic-tac-tonk")

def draw_line(cells_width, cells_height, screen: pg.SurfaceType):
    for i in range(cells_width -1):
        pg.draw.line(screen, BLACK, ((i+1)*screen.get_width()/cells_width-1, 0), ((i+1)*screen.get_width()/cells_width-1, 600), 2)
    for i in range(cells_height -1):
        pg.draw.line(screen, BLACK, (0, (i+1)*screen.get_width()/cells_height-1), (600, (i+1)*screen.get_width()/cells_height-1), 2)

draw_line(CELLS_WIDTH, CELLS_HEIGHT, screen)

#game loop
while running:
    pg.display.flip()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

