import pygame
from utils import get_cell

class Graph:
    def __init__(self, grid, window):
        self.grid = grid
        self.window = window
        self.draw()
    
    def draw(self):
        for row in range(len(self.grid.board)):
            for column in range(len(self.grid.board[row])):
                cell, cell_sqr = get_cell(self.grid, row, column)
                
                self.window.blit(cell.cell_sprite, cell_sqr)