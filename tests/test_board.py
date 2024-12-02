import pytest
from src.controller.game_controller import GameController
from src.model.board import Board
from src.model.cell import Cell
from src.model.game import Game

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
    controller = GameController(4)
    controller.game.board.grid[0][0].set_value(2)  # Cambiar aquí
    # Asegúrate de que el movimiento a la izquierda funciona como se espera
    controller.play_turn('left')
    # Añade aserciones para verificar el estado del tablero después del movimiento

def test_move_right():
    controller = GameController(4)
    controller.game.board.grid[0][2].set_value(2)  # Establece un valor en la celda (0, 2)
    controller.game.board.grid[0][3].set_value(2)  # Establece otro valor en la celda (0, 3)
    
    # Realiza el movimiento a la derecha
    controller.play_turn('right')
    
    # Verifica que las celdas se hayan combinado correctamente
    assert controller.game.board.grid[0][3].get_value() == 4  # La celda (0, 3) debe contener el resultado de la combinación
    assert controller.game.board.grid[0][2].get_value() == 0  # La celda (0, 2) debe estar vacía


def test_move_up():
    controller = GameController(4)
    controller.game.board.grid[2][0].set_value(2)  # Establece un valor en la celda (2, 0)
    controller.game.board.grid[1][0].set_value(2)  # Establece otro valor en la celda (1, 0)
    
    # Realiza el movimiento hacia arriba
    controller.play_turn('up')
    
    # Verifica que las celdas se hayan combinado correctamente
    assert controller.game.board.grid[0][0].get_value() == 4  # La celda (0, 0) debe contener el resultado de la combinación
  

def test_move_down():
    controller = GameController(4)
    controller.game.board.grid[0][0].set_value(2)  # Establece un valor en la celda (0, 0)
    controller.game.board.grid[1][0].set_value(2)  # Establece otro valor en la celda (1, 0)
    
    # Realiza el movimiento hacia abajo
    controller.play_turn('down')
    
    # Verifica que las celdas se hayan combinado correctamente
    assert controller.game.board.grid[3][0].get_value() == 4  # La celda (3, 0) debe contener el resultado de la combinación
    

      
# Test valores frontera y valores límite
    
def test_board_size_values():
    """
    Verifica el comportamiento del tamaño del tablero en valores frontera y límites.
    """
    
    # Valor frontera o único valor permitido (4)   

    board_max = Board(4)  # Frontera superior válida
    assert len(board_max.grid) == 4     

    # Valores límite inferiores (no válidos)
    with pytest.raises(ValueError):  
        Board(3)  # Menor que el mínimo válido

    # Valores límite superiores (no válidos)
    with pytest.raises(ValueError):  
        Board(5)  # Mayor que el máximo válido
        
# Proves de caixa blanca, decision coverage.

def test_move_left_combination():
    board = Board()
    board.grid[0][0].set_value(2)
    board.grid[0][1].set_value(2)
    board.move_left()
    assert board.grid[0][0].get_value() == 4  # Se combinan las celdas

def test_move_left_no_combination():
    board = Board()
    board.grid[0][0].set_value(2)
    board.grid[0][1].set_value(4)
    board.move_left()
    assert board.grid[0][0].get_value() == 2  # No se combinan
    
def test_move_up_combination():
    board = Board()
    board.grid[0][0].set_value(2)
    board.grid[1][0].set_value(2)
    assert board.move_up()  # Debería devolver True
    assert board.grid[0][0].get_value() == 4  # Las celdas deben combinarse

def test_move_up_no_combination():
    board = Board()
    board.grid[0][0].set_value(2)
    board.grid[1][0].set_value(4)
    assert not board.move_up()  # Debería devolver False, sin cambios
    assert board.grid[0][0].get_value() == 2  # Sin cambios


# Estas dos también son condition coverage 

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

# Esta también es loop testing con 0 iteraciones

def test_has_no_moves_possible_full_no_combinations():
    board = Board(size=4)
    values = [
        [2, 4, 8, 16],
        [32, 64, 128, 256],
        [512, 1024, 2048, 2],
        [2, 4, 8, 16],
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

# Loop testing

def test_has_moves_one_iteration():
    board = Board(size=4)
    board.grid[0][0].set_value(2)
    board.grid[0][1].set_value(2)  # Un movimiento posible
    game = Game(size=4, board=board)
    assert board.has_moves()  # Iteraciones: 1

def test_has_moves_multiple_iterations():
    board = Board(size=4)
    board.grid[0][0].set_value(2)
    board.grid[0][1].set_value(2)  # Un movimiento posible
    board.grid[1][0].set_value(4)
    board.grid[1][1].set_value(4)  # Otro movimiento posible
    game = Game(size=4, board=board)
    assert board.has_moves()  # Iteraciones: 3 filas x 3 comparaciones