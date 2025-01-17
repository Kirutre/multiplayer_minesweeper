import pygame
from utils import cell_size, CellStatus ,get_cell
from graphic import Graph


class Game:
    def __init__(self, grid, window_size):
        self.grid = grid
        self.window_size = window_size
        self.run()
        
    def run(self):
        pygame.init()
        
        window = pygame.display.set_mode(self.window_size)
        pygame.display.set_caption('Buscaminas')
        
        is_running = False
        graphics = Graph(self.grid, window)
        
        while True:
            window.fill((51, 28, 33))
            events = pygame.event.get()
            
            if self.is_window_closed(events):
                close = input('Are You Sure? Y/N ')
                
                if close == 'Y':
                    break
                else:
                    continue
            
            if self.is_clicked(events):
                x, y = self.get_mouse_pos(events)
                row, column = x // cell_size, y // cell_size
                
                if not is_running:
                    first_cell_pos = (row, column)
                    
                    self.grid.get_mines(first_cell_pos)
                    self.grid.set_mines_around()
                    
                    is_running = True
                
                cell = self.grid.board[row][column]
                
                cell.cell_status = CellStatus.REVEALED
                cell.set_cell_sprite()
                
                if cell.has_mine:
                    keep = input('Continue? Y/N ')
                    
                    if keep == 'N':
                        break
                
            graphics.draw()
            
            pygame.display.flip()
        pygame.quit()
    
    def is_window_closed(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                return True
            
    def is_clicked(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                return True
    
    def get_mouse_pos(self, events):
        for event in events:
            for row in range(len(self.grid.board)):
                for column in range(len(self.grid.board[row])):
                    cell, cell_sqr = get_cell(self.grid, row, column)
                            
                    if cell_sqr.collidepoint(event.pos):
                        return event.pos