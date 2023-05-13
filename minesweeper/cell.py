
class Cell:
    def __init__(self, row, col, value=0):
        self.row = row
        self.col = col
        self.value = value
        self.visible = False
        self.flag = False

    def __repr__(self):
        return str(self.value)

