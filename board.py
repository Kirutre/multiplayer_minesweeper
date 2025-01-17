import random
from cell import Cell


class Board:
    def __init__(self, board_size):
        self.board_size = board_size
        self.set_board()
    
    def set_board(self):
        self.board = []
        self.mine_percentage = 0.25
        
        for board_row in range(self.board_size[0]):
            row = []
            
            for board_column in range(self.board_size[1]):
                
                cell = Cell()
            
                row.append(cell)
            
            self.board.append(row)

    def get_mines(self, first_cell_pos):
        x, y = first_cell_pos
        first_cell = self.board[x][y]
        
        for row in range(len(self.board)):
            for column in range(len(self.board[row])):
                cell = self.board[row][column]
                last_cell = self.board[row][column-1]
                
                if column == 0:
                    last_cell = self.board[row-1][column-1]
                
                mine = self.generate_mine(last_cell)
                
                if cell != first_cell:
                    cell.has_mine = mine
                
    def generate_mine(self, last_cell):
        get_number = random.random()
        
        self.calculated_mine_percentage(last_cell)
        
        if get_number < self.mine_percentage:
            return True
        
        return False
    
    def calculated_mine_percentage(self, last_cell):
        if self.mine_percentage < 0.5 and self.mine_percentage > 0:
            if last_cell.has_mine:
                self.mine_percentage -= self.mine_percentage ** 2
            else:
                self.mine_percentage = (abs(1 - (self.mine_percentage)) ** 0.5)/3
    
    def set_mines_around(self):
        for row in range(len(self.board)):
            for column in range(len(self.board[0])):
                cell = self.board[row][column]
                
                mines_around = self.get_mines_around(row, column)
                
                cell.nearby_mines = mines_around
                
                cell.set_cell_sprite()
    
    def get_mines_around(self, row, column):
        mines_around = 0
        
        for r in range(max(0, row - 1), min(self.board_size[0], row + 2)):
            for c in range(max(0, column - 1), min(self.board_size[1], column + 2)):
                if r == row and c == column:
                    continue
                
                if self.board[r][c].has_mine:
                    mines_around += 1
        
        return mines_around