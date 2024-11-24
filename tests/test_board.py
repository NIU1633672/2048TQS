import pytest
from src.model.board import Board

def test_initialize_empty_board():
    board = Board(4)  # Creamos un tablero de 4x4
    expected_board = [[0, 0, 0, 0] for _ in range(4)]
    assert board.grid == expected_board

def test_board_is_empty():
    board = Board(4)  # Creamos un tablero 4x4
    assert board.is_empty()  # Al inicio, todas las celdas deberían estar vacías