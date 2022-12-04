import numpy as np
import pygame as pg
import sys
import math

#set constant vars
(SCREEN_WIDTH, SCREEN_HEIGHT) = (600, 600)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (230, 20, 20)
CELLS_WIDTH = 3
CELLS_HEIGHT = 3


screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
running = True
player_1_turn = True 

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

def draw_win(win_start_cell, win_end_cell, cells_width, cells_height, screen):
    cell_width = screen.get_width() / cells_width
    cell_height = screen.get_height() / cells_height
    pg.draw.line(screen, RED, (win_start_cell[0] * cell_width + cell_width / 2, win_start_cell[1] * cell_height + cell_height / 2), (win_end_cell[0] * cell_width + cell_width / 2, win_end_cell[1] * cell_height + cell_height / 2), 2)

#initialises board
draw_line(CELLS_WIDTH, CELLS_HEIGHT, screen)



draw_win((0, 2), (2, 0), CELLS_WIDTH, CELLS_HEIGHT, screen)

#game loop
while running:
    pg.display.flip()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.MOUSEBUTTONUP:
            player_turn_pos = pg.mouse.get_pos()
            x_cell_clicked = math.ceil(player_turn_pos[0] * CELLS_WIDTH / screen.get_width() ) - 1
            y_cell_clicked = math.ceil(player_turn_pos[1] * CELLS_HEIGHT / screen.get_height() ) - 1
            print(player_turn_pos)
            print(x_cell_clicked, y_cell_clicked)
            if player_1_turn == False:
                player_1_turn = True
            else:
                player_1_turn = False
            draw_turn(player_1_turn, CELLS_WIDTH, CELLS_HEIGHT, x_cell_clicked, y_cell_clicked, screen)
            pg.display.flip()


