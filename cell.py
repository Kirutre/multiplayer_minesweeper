from utils import ASSETS, CellStatus


class Cell:
    def __init__(self):
        self._has_mine = False
        self._cell_status = CellStatus.HIDDEN
        self._nearby_mines = 0
        self.cell_sprite = ASSETS['hidden']
        
    def set_cell_sprite(self):
        if self._cell_status == CellStatus.HIDDEN:
            self.cell_sprite = ASSETS['hidden']
        elif self._cell_status == CellStatus.MARKED:
            self.cell_sprite = ASSETS['flag']
        elif self._has_mine:
            self.cell_sprite = ASSETS['bomb']
        elif self._nearby_mines >= 0:
            self.cell_sprite = ASSETS[f'{self._nearby_mines}_mine']
    
    @property
    def has_mine(self):
        return self._has_mine
    
    @has_mine.setter
    def has_mine(self, mine):
        self._has_mine = mine
    
    @property
    def nearby_mines(self):
        return self._nearby_mines
    
    @nearby_mines.setter
    def nearby_mines(self, mines_amount):
        self._nearby_mines = mines_amount
    
    @property
    def cell_status(self):
        return self._cell_status
    
    @cell_status.setter
    def cell_status(self, status):
        self._cell_status = status