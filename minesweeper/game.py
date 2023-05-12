import numpy
import numpy as np
import random

from cell import Cell
import itertools

class Game:
    def __init__(self, n_mines=10):
        self.board = np.empty((5, 5), dtype=Cell)
        self.mines = random.sample(range(0, 25), n_mines)
        self.create_game()

    def create_game(self):
        #Place mines
        for i in range(self.board.shape[0]):
            for j in range(self.board.shape[1]):
                self.board[i,j] = Cell(i,j, self.get_value(i,j))

    def get_value(self, i, j):
        if i*self.board.shape[1]+j in self.mines:
            return -1
        cells = list(itertools.product([i, i-1, i+1], [j, j-1, j+1]))
        count = 0
        for x, y in cells:
            if x >=0 and y>=0 and x<self.board.shape[0] and y<self.board.shape[1]:
                idx = x*self.board.shape[1]+y
                if idx in self.mines:
                    count += 1
        return count





        # for row in self.board:
        #     for cell in row:
        #         print(cell.value)


if __name__ == "__main__":
    game = Game()
    game.create_game()
    game.get_value(1,1)


