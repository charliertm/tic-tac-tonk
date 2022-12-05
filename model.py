import numpy as np

class Board:
    def __init__(self):
        self.board = [[0, 0, 0] for i in range(3)]
        self.num_moves = 0

    @property
    def player_to_move(self):
        return -1 if (self.num_moves % 2) else 1

    def move(self, x: int, y: int):
        if self.board[y][x] != 0:
            raise Exception('This cell is already filled.')
        self.board[y][x] = self.player_to_move
        self.num_moves += 1
    
    def check_winner(self):
        for row in self.board:
            if sum(row) == 3:
                return 1
            elif sum(row) == -3:
                return -1
        for col in np.array(self.board).transpose().tolist():
            if sum(col) == 3:
                return 1
            elif sum(col) == -3:
                return -1
        # forward diagonal
        if sum(np.diag(np.array(self.board))) == 3:
            return 1
        elif sum(np.diag(np.array(self.board))) == -3:
            return -1
        # backwards diagonal
        if np.diag(np.fliplr(np.array(self.board))) == 3:
            return 1
        elif np.diag(np.fliplr(np.array(self.board))) == -3:
            return -1
        return False

