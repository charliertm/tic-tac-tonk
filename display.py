import numpy as np
import pygame as pg
import sys

#set display vars
(SCREEN_WIDTH, SCREEN_HEIGHT) = (600, 600)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
CELLS_WIDTH = 3
CELLS_HEIGHT = 3

player_1_turn = True 
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

def draw_turn(player_1_turn, cells_width, cells_height, cell_x_pos, cell_y_pos, screen: pg.SurfaceType):
    cell_width = screen.get_width() / cells_width
    cell_height = screen.get_height() / cells_height
    if player_1_turn:
        pg.draw.circle(screen, BLACK, (cell_x_pos * cell_width + cell_width / 2, cell_y_pos * cell_height + cell_height / 2), 0.8 * screen.get_width()/(cells_width * 2), 2)
    else:
        for i in range(2):
            pg.draw.line(screen, BLACK, (cell_x_pos * cell_width + cell_width / 5, cell_y_pos * cell_height + cell_height / 5), (cell_x_pos * cell_width + cell_width * 4 / 5, cell_y_pos * cell_height + cell_height * 4 / 5), 2)
            pg.draw.line(screen, BLACK, (cell_x_pos * cell_width + cell_width * 4 / 5, cell_y_pos * cell_height + cell_height / 5), (cell_x_pos * cell_width + cell_width / 5, cell_y_pos * cell_height + cell_height * 4 / 5), 2)

draw_line(CELLS_WIDTH, CELLS_HEIGHT, screen)

draw_turn(False, CELLS_WIDTH, CELLS_HEIGHT, 1, 2, screen)

draw_turn(True, CELLS_WIDTH, CELLS_HEIGHT, 0, 1, screen)

#game loop
while running:
    pg.display.flip()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

