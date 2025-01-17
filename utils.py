import pygame
import enum

cell_size = 100

class CellStatus(enum.Enum):
    HIDDEN = enum.auto()
    MARKED = enum.auto()
    REVEALED = enum.auto()

ASSETS = {"hidden": pygame.image.load("assets/cell.png"),
          "0_mine": pygame.image.load("assets/revealed-cell.png"),
          "1_mine": pygame.image.load("assets/1.png"),
          "2_mine": pygame.image.load("assets/2.png"),
          "3_mine": pygame.image.load("assets/3.png"),
          "4_mine": pygame.image.load("assets/4.png"),
          "5_mine": pygame.image.load("assets/5.png"),
          "6_mine": pygame.image.load("assets/6.png"),
          "7_mine": pygame.image.load("assets/7.png"),
          "8_mine": pygame.image.load("assets/8.png"),
          "bomb": pygame.image.load("assets/bomb.png"),
          "flag": pygame.image.load("assets/flag.png")}

def get_cell(grid, row, column):
    x = row * cell_size
    y = column * cell_size
    position = (x, y)
                
    cell = grid.board[row][column]
    cell_sqr = cell.cell_sprite.get_rect()
    cell_sqr.topleft = position
    
    return (cell, cell_sqr)           