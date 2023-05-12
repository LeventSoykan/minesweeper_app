
class Cell:
    def __init__(self, row, col, value=0):
        self.row = row
        self.col = col
        self.value = value

    def __repr__(self):
        return str(self.value)

