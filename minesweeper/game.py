import numpy
import numpy as np
import random

from cell import Cell
import itertools

class Game:
    def __init__(self, n_mines=2):
        self.board = np.empty((5, 5), dtype=Cell)
        self.mines = random.sample(range(0, 25), n_mines)
        self.create_game()
        self.playing = True
        self.stack = []
        # self.first_click = False

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

    def game_complete(self):
        for row in self.board:
            for cell in row:
                if not cell.visible:
                    return False
        return True

    def check_selection(self, i, j):
        self.set_visibility(i, j)
        cell = self.board[i, j]
        if self.game_complete() or cell.value == -1:
            self.playing = False

    def set_visibility(self, i, j):
        self.stack.append((i,j))
        cell = self.board[i, j]
        cell.visible = True
        if cell.value == 0:
            cells = list(itertools.product([i, i - 1, i + 1], [j, j - 1, j + 1]))
            for x, y in cells:
                if 0 <= x < self.board.shape[0] and 0 <= y < self.board.shape[1] and ((x,y) not in self.stack):
                    self.set_visibility(x, y)







        # for row in self.board:
        #     for cell in row:
        #         print(cell.value)


if __name__ == "__main__":
    game = Game()
    game.create_game()
    game.get_value(1,1)


