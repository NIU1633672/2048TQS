import pytest
from src.model.board import Board

def test_initialize_empty_board():
    board = Board(4)  # Creamos un tablero de 4x4
    expected_board = [[0, 0, 0, 0] for _ in range(4)]
    assert board.grid == expected_board
