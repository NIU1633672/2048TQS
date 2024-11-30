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
    """
    Verifica que agregar una ficha aleatoria cambia una celda vacía
    a tener un valor válido (2 o 4).
    """
    # Creamos el controlador, que tiene el tablero
    controller = GameController(4)
    
    # Guardamos el estado inicial del tablero
    initial_board = controller.get_board()
    
    # Contamos las celdas vacías antes de agregar la ficha
    empty_cells_before = sum(
        1 for row in initial_board.grid for cell in row if cell.is_empty()
    )
    
    # Añadimos una ficha aleatoria
    controller.add_random_tile()
    
    # Contamos las celdas vacías después de agregar la ficha
    empty_cells_after = sum(
        1 for row in initial_board.grid for cell in row if cell.is_empty()
    )
    
    # Verificamos que el número de celdas vacías disminuyó en 1
    assert empty_cells_after == empty_cells_before - 1

    # Verificamos que la celda no vacía tiene un valor válido
    for row in initial_board.grid:
        for cell in row:
            if not cell.is_empty():
                assert cell.value in [2, 4]

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
