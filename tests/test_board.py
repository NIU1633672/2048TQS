import pytest
from src.controller.game_controller import GameController
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


def test_add_random_tile():
    controller = GameController(4)
    initial_board = controller.game.board  # Cambiar aquí
    controller.add_random_tile()
    # Verifica que una celda vacía ahora tiene un valor válido
    has_valid_value = any(cell.get_value() in (2, 4) for row in initial_board.grid for cell in row if cell.get_value() is not None)
    assert has_valid_value

def test_move_left():
    """
    Verifica que el movimiento hacia la izquierda funcione correctamente.
    """
    controller = GameController(4)  # Tablero 4x4

    # Configuramos un estado inicial del tablero
    controller.board.grid[0][0].set_value(2)
    controller.board.grid[0][1].set_value(2)

    # Realizamos el movimiento hacia la izquierda
    controller.move_left()

    # Verificamos el resultado esperado
    assert controller.board.grid[0][0].value == 4  # Se combinan
    assert controller.board.grid[0][1].is_empty()  # La celda se vacía

def test_move_right():
    """
    Verifica que el movimiento hacia la derecha funcione correctamente.
    """
    controller = GameController(4)  # Tablero 4x4

    # Configuramos un estado inicial del tablero
    controller.board.grid[0][2].set_value(2)
    controller.board.grid[0][3].set_value(2)

    # Realizamos el movimiento hacia la derecha
    controller.move_right()

    # Verificamos el resultado esperado
    assert controller.board.grid[0][3].value == 4  # Se combinan
    assert controller.board.grid[0][2].is_empty()  # La celda se vacía
    assert controller.board.grid[0][1].is_empty()  # Se espera que estas celdas estén vacías
    assert controller.board.grid[0][0].is_empty()

def test_move_up():
    """
    Verifica que el movimiento hacia arriba funcione correctamente.
    """
    controller = GameController(4)  # Tablero 4x4

    # Configuramos un estado inicial del tablero
    controller.board.grid[2][0].set_value(2)
    controller.board.grid[3][0].set_value(2)

    # Realizamos el movimiento hacia arriba
    controller.move_up()

    # Verificamos el resultado esperado
    assert controller.board.grid[0][0].value == 4  # Se combinan
    assert controller.board.grid[2][0].is_empty()  # La celda se vacía
    assert controller.board.grid[1][0].is_empty()  # La celda entre se vacía

def test_move_down():
    """
    Verifica que el movimiento hacia abajo funcione correctamente.
    """
    controller = GameController(4)  # Tablero 4x4

    # Configuramos un estado inicial del tablero
    controller.board.grid[2][0].set_value(2)  # Colocamos un 2 en la fila 2, columna 0
    controller.board.grid[3][0].set_value(2)  # Colocamos otro 2 en la fila 3, columna 0
    controller.move_down()  # Hacemos el movimiento hacia abajo

    # Verificamos que el valor en la fila 3, columna 0 sea 4
    assert controller.board.grid[3][0].value == 4
    # Verificamos que el valor en la fila 2, columna 0 sea 0 (ya que se combinó)
    assert controller.board.grid[2][0].value == 0

def test_is_full_with_empty_cells():
    board = Board(size=4)
    board.grid[0][0].set_value(2)  # Una celda con valor, las demás vacías
    assert not board.is_full()  # El tablero no está lleno

def test_is_full_with_all_cells_filled():
    board = Board(size=4)
    for row in board.grid:
        for cell in row:
            cell.set_value(2)  # Llenamos todas las celdas
    assert board.is_full()  # El tablero está lleno

def test_has_no_moves_possible_full_no_combinations():
    board = Board(size=4)
    values = [
        [2, 4, 8, 16],
        [32, 64, 128, 256],
        [512, 1024, 2048, 4096],
        [8192, 16384, 32768, 65536],
    ]
    for i in range(4):
        for j in range(4):
            board.grid[i][j].set_value(values[i][j])
    assert not board.has_moves()  # El tablero lleno y sin combinaciones posibles

def test_has_moves_possible_with_combinations():
    board = Board(size=4)
    values = [
        [2, 2, 4, 8],
        [16, 32, 64, 128],
        [256, 512, 1024, 2048],
        [2, 4, 8, 16],
    ]
    for i in range(4):
        for j in range(4):
            board.grid[i][j].set_value(values[i][j])
    assert board.has_moves()  # Hay combinaciones posibles (dos 2 en la primera fila)