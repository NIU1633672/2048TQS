# mock_board.py
from random import choice  
from mocks.mock_cell import MockCell

class MockBoard:
    def __init__(self, size):
        self.size = size
        self.board = [[MockCell(0) for _ in range(size)] for _ in range(size)]
        self.score = 0  # Inicializa un valor de puntuación
        self.cells = [[MockCell() for _ in range(size)] for _ in range(size)]

    def get_score(self):
        return self.score  # Devuelve la puntuación actual

    def get_board(self):
        return self.board  # Devuelve el estado actual del tablero

    def move_left(self):
        print("Moving left")        

    def display(self):
        print(f"Board displayed: {self.board}")
        
    def add_cell(self):
        # Simular la lógica de adición de una celda
        empty_cells = [(i, j) for i in range(self.size) for j in range(self.size) if self.cells[i][j].is_empty()]
        if empty_cells:
            i, j = choice(empty_cells)  # Selecciona una celda vacía al azar
            self.cells[i][j].set_value(choice([2, 4]))  # Asigna 2 o 4 aleatoriamente

    def get_cell_value(self, x, y):
        return self.cells[x][y].get_value()
