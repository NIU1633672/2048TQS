# mock_board.py
from mocks.mock_cell import MockCell

class MockBoard:
    def __init__(self, size):
        self.size = size
        self.board = [[MockCell(0) for _ in range(size)] for _ in range(size)]
        self.score = 0  # Inicializa un valor de puntuación

    def get_score(self):
        return self.score  # Devuelve la puntuación actual

    def get_board(self):
        return self.board  # Devuelve el estado actual del tablero

    def move_left(self):
        print("Moving left")
        # Aquí podrías simular el movimiento en el tablero

    def display(self):
        print(f"Board displayed: {self.board}")
