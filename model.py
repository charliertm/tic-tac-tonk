import numpy as np

class Board:
    def __init__(self, size: int):
        self.board = [[0 for x in range(size)] for y in range(size)]
        self.size = size
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
            if sum(row) == self.size:
                return 1
            elif sum(row) == -self.size:
                return -1
        for col in np.array(self.board).transpose().tolist():
            if sum(col) == self.size:
                return 1
            elif sum(col) == -self.size:
                return -1
        # forward diagonal
        if sum(np.diag(np.array(self.board))) == self.size:
            return 1
        elif sum(np.diag(np.array(self.board))) == -self.size:
            return -1
        # backwards diagonal
        if sum(np.diag(np.fliplr(np.array(self.board)))) == self.size:
            return 1
        elif sum(np.diag(np.fliplr(np.array(self.board)))) == -self.size:
            return -1
        return False
    
    def get_winning_cells(self):
        winner = self.check_winner()
        if not winner:
            raise Exception('Cannot get winning cells because there is no winner!')
        for r, row in enumerate(self.board):
            if sum(row) == self.size * winner:
                return [(0, r), (self.size - 1 , r)]
        for c, col in enumerate(np.array(self.board).transpose().tolist()):
            if sum(col) == self.size * winner:
                return [(c, 0), (c, self.size - 1)]
        # forward diagonal
        if sum(np.diag(np.array(self.board))) == self.size * winner:
            return [(0, 0), (self.size - 1, self.size - 1)]
        # backwards diagonal
        if sum(np.diag(np.fliplr(np.array(self.board)))) == self.size * winner:
            return [(self.size - 1, 0), (0, self.size - 1)]

