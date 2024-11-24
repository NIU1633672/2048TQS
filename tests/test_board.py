import pytest
from src.model.board import Board
from src.model.cell import Cell

def test_initialize_board_with_cells():
    """
    Verifica que el tablero se inicializa correctamente con objetos de tipo Cell.
    """
    board = Board(4)  # Creamos un tablero de 4x4
    for row in board.grid:
        for cell in row:
            assert isinstance(cell, Cell), "Cada posición del tablero debe ser un objeto Cell"

def test_initialize_board_with_empty_cells():
    """
    Verifica que todas las celdas del tablero están vacías al inicializarse.
    """
    board = Board(4)  # Creamos un tablero de 4x4
    for row in board.grid:
        for cell in row:
            assert cell.is_empty(), "Todas las celdas deben estar vacías al inicio"
