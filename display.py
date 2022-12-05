import pygame as pg
import sys
import math
import time

#set constant vars
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (200, 200, 200)
RED = (230, 20, 20)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BOARD_SIZE = 3
(SCREEN_WIDTH, SCREEN_HEIGHT) = (600, 650)

#sets dynamic vars
running = True
player_1_turn = True
previous_turns = list()

#temp vars
win_start_cell = (BOARD_SIZE-1, 0)
win_end_cell = (0, BOARD_SIZE-1)

#initialise display
pg.init()
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill(WHITE)
pg.display.set_caption("Tic-tac-tonk")

#initialise messages
font = pg.font.SysFont('bahnschrift', 32)
player_1_turn_msg = 'Player 1s turn'
player_2_turn_msg = 'Player 2s turn'
player_1_win_msg = 'Player 1 Wins!!!'
player_2_win_msg = 'Player 2 Wins!!!'
non_empty_cell = 'Select empty cell'

def draw_board(board_size, screen: pg.SurfaceType):
    for i in range(board_size -1):
        pg.draw.line(screen, BLACK, ((i+1)*screen.get_width()/board_size-1, 0), ((i+1)*screen.get_width()/board_size-1, 600), 2)
    for i in range(board_size -1):
        pg.draw.line(screen, BLACK, (0, (i+1)*(screen.get_height()-50)/board_size-1), (600, (i+1)*(screen.get_height()-50)/board_size-1), 2)
    pg.draw.rect(screen, GREY, pg.Rect(0, screen.get_height()-50, screen.get_width(), 50))

def draw_turn(player_1_turn, board_size, cell_x_pos, cell_y_pos, screen: pg.SurfaceType):
    cell_width = screen.get_width()/board_size
    cell_height = (screen.get_height()-50)/board_size
    if player_1_turn:
        pg.draw.circle(screen, BLACK, (cell_x_pos * cell_width + cell_width / 2, cell_y_pos * cell_height + cell_height / 2), 0.8 * min(screen.get_width()/(board_size * 2), screen.get_height()/(board_size * 2)), 2)
    else:
        for i in range(2):
            pg.draw.line(screen, BLACK, (cell_x_pos * cell_width + cell_width / 5, cell_y_pos * cell_height + cell_height / 5), (cell_x_pos * cell_width + cell_width * 4 / 5, cell_y_pos * cell_height + cell_height * 4 / 5), 2)
            pg.draw.line(screen, BLACK, (cell_x_pos * cell_width + cell_width * 4 / 5, cell_y_pos * cell_height + cell_height / 5), (cell_x_pos * cell_width + cell_width / 5, cell_y_pos * cell_height + cell_height * 4 / 5), 2)

def draw_win_line(win_start_cell, win_end_cell, board_size, screen):
    cell_width = screen.get_width()/board_size
    cell_height = (screen.get_height()-50)/board_size
    pg.draw.line(screen, RED, (win_start_cell[0] * cell_width + cell_width / 2, win_start_cell[1] * cell_height + cell_height / 2), (win_end_cell[0] * cell_width + cell_width / 2, win_end_cell[1] * cell_height + cell_height / 2), 6)  

def draw_msg(message, surface, location, colour, background_colour):
    message = font.render(message, True, colour, background_colour)
    surface = message.get_rect()
    surface.center = (location)
    screen.blit(message, surface)
#win_msg_rect = player_1_win_msg.get_rect()
#win_msg_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

#draws board
draw_board(BOARD_SIZE, screen)
draw_msg(player_1_turn_msg, screen, (110, 625), BLACK, GREY)

#draws win -- needs to be in game loop on win detection
draw_win_line(win_start_cell, win_end_cell, BOARD_SIZE, screen)
draw_msg(player_1_win_msg, screen, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2), GREEN, BLUE)

#game loop
while running:
    pg.display.flip()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.MOUSEBUTTONUP:
            player_turn_pos = pg.mouse.get_pos()
            x_cell_clicked = math.ceil(player_turn_pos[0] * BOARD_SIZE / screen.get_width() ) - 1
            y_cell_clicked = math.ceil(player_turn_pos[1] * BOARD_SIZE / (screen.get_height() - 50) ) - 1
            if [x_cell_clicked, y_cell_clicked] in previous_turns:
                draw_msg(player_2_turn_msg, screen, (110, 625), GREY, GREY)
                draw_msg(non_empty_cell, screen, (130, 625), BLACK, GREY)
                pg.display.flip()
                time.sleep(1)
                if player_1_turn == True:
                    draw_msg(non_empty_cell, screen, (130, 625), GREY, GREY)
                    draw_msg(player_1_turn_msg, screen, (110, 625), BLACK, GREY)
                else:
                    draw_msg(non_empty_cell, screen, (130, 625), GREY, GREY)
                    draw_msg(player_2_turn_msg, screen, (110, 625), BLACK, GREY)
            else:
                previous_turns.append([x_cell_clicked, y_cell_clicked])
                draw_turn(player_1_turn, BOARD_SIZE, x_cell_clicked, y_cell_clicked, screen)
                if player_1_turn == True:
                    player_1_turn = False
                    draw_msg(non_empty_cell, screen, (130, 625), GREY, GREY)
                    draw_msg(player_2_turn_msg, screen, (110, 625), BLACK, GREY)                    
                else:
                    player_1_turn = True
                    draw_msg(non_empty_cell, screen, (130, 625), GREY, GREY)
                    draw_msg(player_1_turn_msg, screen, (110, 625), BLACK, GREY)            
