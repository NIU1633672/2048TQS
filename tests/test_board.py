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

# Particions equivalents i valors límit reset

def test_reset_empty_board():
    board = Board(4)  # Tablero vacío
    board.reset()
    assert board.is_empty()   # Debe seguir vacío

def test_reset_partial_filled_board():
    board = Board(4)
    board.grid[0][0].set_value(2)  # Una celda ocupada
    board.reset()
    assert board.is_empty()  # Debe estar vacío después de reset

def test_reset_fully_filled_board():
    board = Board(4)
    for row in board.grid:
        for cell in row:
            cell.set_value(2)  # Llenamos todas las celdas
    board.reset()
    assert board.is_empty()  # Debe estar vacío después de reset

# Particio equivalent add_random_tile (vàlid / no vàlid)

def test_add_random_tile():
    controller = GameController(4)
    initial_board = controller.game.board  # Cambiar aquí
    controller.add_random_tile()
    # Verifica que una celda vacía ahora tiene un valor válido
    has_valid_value = any(cell.get_value() in (2, 4) for row in initial_board.grid for cell in row if cell.get_value() is not None)
    assert has_valid_value
    
def test_add_random_tile_invalid_value():
    board = Board(4)  # Crea un tablero de 4x4
    board.reset()  # Asegúrate de que el tablero esté vacío al inicio

    # Asegúrate de que no hay celdas llenas antes de agregar una
    assert all(cell.is_empty() for row in board.grid for cell in row), "El tablero debe estar vacío"

    # Llama a add_random_tile y verifica que se añade un valor válido (2 o 4)
    board.add_random_tile()
    
    # Comprueba que no hay valores inválidos (3) en el tablero
    for row in board.grid:
        for cell in row:
            assert cell.get_value() != 3, "No debe haber un valor inválido en el tablero"

# Valors limit i frontera add random tile

def test_add_random_tile_invalid_values():
    board = Board(4)  # Crea un tablero de 4x4
    board.reset()  # Asegúrate de que el tablero esté vacío al inicio

    # Asegúrate de que no hay celdas llenas antes de agregar una
    assert all(cell.is_empty() for row in board.grid for cell in row), "El tablero debe estar vacío"

    # Llama a add_random_tile y verifica que se añade un valor válido (2 o 4)
    board.add_random_tile()
    
    # Comprueba que no hay valores inválidos (1, 3 y 5) en el tablero
    for row in board.grid:
        for cell in row:
            assert cell.get_value() != 1, "No debe haber un valor inválido 1 en el tablero"
            assert cell.get_value() != 3, "No debe haber un valor inválido 3 en el tablero"
            assert cell.get_value() != 5, "No debe haber un valor inválido 5 en el tablero"



def test_move_left():
    controller = GameController(4)
    controller.game.board.grid[0][0].set_value(2)  
    controller.game.board.grid[0][1].set_value(2)
    
    # Asegúrate de que el movimiento a la izquierda funciona como se espera
    controller.play_turn('left')
    # Añade aserciones para verificar el estado del tablero después del movimiento
    assert controller.game.board.grid[0][0].get_value() == 4
    
def test_move_left1():
    controller = GameController(4)
    controller.game.board.grid[0][0].set_value(2048)  
    controller.game.board.grid[0][1].set_value(2048)
    
    with pytest.raises(ValueError):
        controller.play_turn('left')
    
def test_move_left_with_1():
    controller = GameController(4)
    with pytest.raises(ValueError):
        controller.game.board.grid[0][0].set_value(1)  # Debería fallar al establecer el valor

def test_move_left_with_3():
    controller = GameController(4)
    with pytest.raises(ValueError):
        controller.game.board.grid[0][0].set_value(3)  # Debería fallar al establecer el valor
        
def test_move_left_with_2047():
    controller = GameController(4)
    with pytest.raises(ValueError):
        controller.game.board.grid[0][0].set_value(2047)  # Debería fallar al establecer el valor

def test_move_left_with_2049():
    controller = GameController(4)
    with pytest.raises(ValueError):
        controller.game.board.grid[0][0].set_value(2049)  # Debería fallar al establecer el valor

def test_move_right():
    controller = GameController(4)
    controller.game.board.grid[0][2].set_value(2)  
    controller.game.board.grid[0][3].set_value(2)
    
    # Asegúrate de que el movimiento a la derecha funciona como se espera
    controller.play_turn('right')
    # Añade aserciones para verificar el estado del tablero después del movimiento
    assert controller.game.board.grid[0][3].get_value() == 4

def test_move_right_with_2048():
    controller = GameController(4)
    controller.game.board.grid[0][2].set_value(2048)  
    controller.game.board.grid[0][3].set_value(2048)
    
    with pytest.raises(ValueError):
        controller.play_turn('right')

def test_move_right_with_1():
    controller = GameController(4)
    with pytest.raises(ValueError):
        controller.game.board.grid[0][0].set_value(1)  # Debería fallar al establecer el valor

def test_move_right_with_3():
    controller = GameController(4)
    with pytest.raises(ValueError):
        controller.game.board.grid[0][0].set_value(3)  # Debería fallar al establecer el valor

def test_move_right_with_2047():
    controller = GameController(4)
    with pytest.raises(ValueError):
        controller.game.board.grid[0][0].set_value(2047)  # Debería fallar al establecer el valor

def test_move_right_with_2049():
    controller = GameController(4)
    with pytest.raises(ValueError):
        controller.game.board.grid[0][0].set_value(2049)  # Debería fallar al establecer el valor


def test_move_up():
    controller = GameController(4)
    controller.game.board.grid[2][0].set_value(2)  
    controller.game.board.grid[3][0].set_value(2)
    
    # movimiento hacia arriba funciona como se espera
    controller.play_turn('up')
    # Añade aserciones para verificar el estado del tablero después del movimiento
    assert controller.game.board.grid[0][0].get_value() == 4

def test_move_up_with_2048():
    controller = GameController(4)
    controller.game.board.grid[2][0].set_value(2048)  
    controller.game.board.grid[3][0].set_value(2048)
    
    with pytest.raises(ValueError):
        controller.play_turn('up')

def test_move_up_with_1():
    controller = GameController(4)
    with pytest.raises(ValueError):
        controller.game.board.grid[0][0].set_value(1)  # Debería fallar al establecer el valor

def test_move_up_with_3():
    controller = GameController(4)
    with pytest.raises(ValueError):
        controller.game.board.grid[0][0].set_value(3)  # Debería fallar al establecer el valor

def test_move_up_with_2047():
    controller = GameController(4)
    with pytest.raises(ValueError):
        controller.game.board.grid[0][0].set_value(2047)  # Debería fallar al establecer el valor

def test_move_up_with_2049():
    controller = GameController(4)
    with pytest.raises(ValueError):
        controller.game.board.grid[0][0].set_value(2049)  # Debería fallar al establecer el valor
  

def test_move_down():
    controller = GameController(4)
    controller.game.board.grid[2][0].set_value(2)  
    controller.game.board.grid[3][0].set_value(2)
    
    # Asegúrate de que el movimiento hacia abajo funciona como se espera
    controller.play_turn('down')
    # Añade aserciones para verificar el estado del tablero después del movimiento
    assert controller.game.board.grid[3][0].get_value() == 4

def test_move_down_with_2048():
    controller = GameController(4)
    controller.game.board.grid[2][0].set_value(2048)  
    controller.game.board.grid[3][0].set_value(2048)
    
    with pytest.raises(ValueError):
        controller.play_turn('down')

def test_move_down_with_1():
    controller = GameController(4)
    with pytest.raises(ValueError):
        controller.game.board.grid[0][0].set_value(1)  # Debería fallar al establecer el valor

def test_move_down_with_3():
    controller = GameController(4)
    with pytest.raises(ValueError):
        controller.game.board.grid[0][0].set_value(3)  # Debería fallar al establecer el valor

def test_move_down_with_2047():
    controller = GameController(4)
    with pytest.raises(ValueError):
        controller.game.board.grid[0][0].set_value(2047)  # Debería fallar al establecer el valor

def test_move_down_with_2049():
    controller = GameController(4)
    with pytest.raises(ValueError):
        controller.game.board.grid[0][0].set_value(2049)  # Debería fallar al establecer el valor

def test_move_down_equivalence_partitions():
    controller = GameController(4)

    # Caso válido: movimientos que deben combinarse
    controller.game.board.grid[2][0].set_value(2)
    controller.game.board.grid[3][0].set_value(2)
    
    # Realizar movimiento hacia abajo
    move_successful = controller.play_turn('down')
    
    # Comprobar que el movimiento fue exitoso
    assert move_successful
    assert controller.game.board.grid[3][0].get_value() == 4  # Combinación debe dar 4
    assert controller.game.board.grid[2][0].get_value() == 0  # La celda debe estar vacía

    # Caso no válido: intentar mover un 2 y un 4 (no se deben combinar)
    controller.game.board.grid[2][0].set_value(2)  # Establecer 2 en la celda
    controller.game.board.grid[3][0].set_value(4)  # Establecer 4 en la celda inferior

    # Intentar mover hacia abajo, se espera que el movimiento no sea exitoso
    move_successful = controller.play_turn('down')
    
    # Verificar que no hubo movimiento
    assert not move_successful
    assert controller.game.board.grid[3][0].get_value() == 4  # La celda inferior debe seguir siendo 4
    assert controller.game.board.grid[2][0].get_value() == 2  # La celda superior debe seguir siendo 2   

      
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
    
def test_move_left_empty_cells():
    board = Board()
    board.grid[0][0].set_value(2)
    board.grid[0][1].set_value(0)  # Celda vacía
    board.move_left()
    assert board.grid[0][0].get_value() == 2  # Debe permanecer igual
    assert board.grid[0][1].get_value() == 0  # Debe permanecer vacío

def test_move_left_multiple_combinations():
    board = Board()
    board.grid[0][0].set_value(2)
    board.grid[0][1].set_value(2)
    board.grid[0][2].set_value(4)
    board.grid[0][3].set_value(4)  # Se pueden combinar
    assert board.move_left() == True  # Se espera que haya movimiento
    assert board.grid[0][0].get_value() == 4  # Combinación 2 + 2
    assert board.grid[0][1].get_value() == 8  # Combinación 4 + 4
    assert board.grid[0][2].get_value() == 0  # Relleno con 0

def test_move_left_no_change():
    board = Board()
    board.grid[0][0].set_value(2)
    board.grid[0][1].set_value(4)  # No se pueden combinar
    assert board.move_left() == False  # No hubo movimiento
    assert board.grid[0][0].get_value() == 2  # Sin cambios
    assert board.grid[0][1].get_value() == 4  # Sin cambios
    
def test_move_right_combination():
    board = Board()
    board.grid[0][0].set_value(2)
    board.grid[0][1].set_value(2)  # Deben combinarse
    assert board.move_right() == True  # Se espera que haya movimiento
    assert board.grid[0][3].get_value() == 4  # La combinación debe estar a la derecha

def test_move_right_no_combination():
    board = Board()
    board.grid[0][0].set_value(2)
    board.grid[0][1].set_value(4)  # No se pueden combinar    
    assert board.grid[0][0].get_value() == 2  # Sin cambios
    assert board.grid[0][1].get_value() == 4  # Sin cambios

def test_move_right_with_empty_cells():
    board = Board()
    board.grid[0][0].set_value(2)
    board.grid[0][1].set_value(0)  # Celda vacía
    assert board.move_right() == True  # Debe mover 2 a la derecha
    assert board.grid[0][3].get_value() == 2  # Debe moverse a la derecha
    

def test_move_right_multiple_combinations():
    board = Board()
    board.grid[0][0].set_value(2)
    board.grid[0][1].set_value(2)
    board.grid[0][2].set_value(4)
    board.grid[0][3].set_value(4)  # Deben combinarse
    assert board.move_right() == True  # Se espera que haya movimiento
    assert board.grid[0][2].get_value() == 4  
    assert board.grid[0][3].get_value() == 8  

def test_move_right_no_change():
    board = Board()
    board.grid[0][0].set_value(2)
    board.grid[0][1].set_value(4)
    board.grid[0][2].set_value(2)
    board.grid[0][3].set_value(4)  # Sin cambios
    assert board.move_right() == False  # No hubo movimiento
    assert board.grid[0][0].get_value() == 2  # Sin cambios
    assert board.grid[0][1].get_value() == 4  # Sin cambios
    



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
    


