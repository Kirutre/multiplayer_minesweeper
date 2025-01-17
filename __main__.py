from game import Game
from board import Board


def main():
    board_size = (5, 5)
    window_size = (500, 500)
    grid = Board(board_size)
    game = Game(grid, window_size)
    
if __name__ == '__main__':main()