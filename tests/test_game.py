import pytest
from src.model.game import Game
from src.model.board import Board
from src.model.cell import Cell
from unittest.mock import patch

def test_init_boundary_values():
    # Caso límite: tamaño correcto (4)
    game = Game(4)
    assert game.board.size == 4  # Debe crear un tablero de tamaño 4
    assert isinstance(game.board, Board)  # Debe ser una instancia de Board
    assert game.score == 0  # Puntuación inicial debe ser 0

    # Caso límite incorrecto: tamaño incorrecto
    try:
        Game(3)  # Debe lanzar una excepción
        assert False, "Expected an AssertionError for size 3"
    except AssertionError:
        pass  # Se espera que falle, así que esto es correcto

    try:
        Game(5)  # Debe lanzar una excepción
        assert False, "Expected an AssertionError for size 5"
    except AssertionError:
        pass  # Se espera que falle, así que esto es correcto

def test_init_equivalence_partitions():
    # Partición: Tamaño correcto (4)
    game = Game(4)
    assert game.board.size == 4  # Debe crear un tablero de tamaño 4
    assert isinstance(game.board, Board)  # Debe ser una instancia de Board
    assert game.score == 0  # Puntuación inicial debe ser 0

    # Partición: Otro tablero (board no es None)
    custom_board = Board(4)
    game_with_custom_board = Game(4, custom_board)
    assert game_with_custom_board.board == custom_board  # Debe usar el otro tablero
    assert game_with_custom_board.score == 0  # Puntuación inicial debe seguir siendo 0

    # Partición: Tamaño incorrecto (3 o 5, que deben causar una excepción)
    for invalid_size in [3, 5]:
        try:
            Game(invalid_size)  # Debe lanzar una excepción
            assert False, f"Expected an AssertionError for size {invalid_size}"
        except AssertionError:
            pass  # Se espera que falle, así que esto es correcto


def test_play_turn():
    """
    Verifica que un turno completo funcione correctamente en el modelo de juego.
    """
    game = Game(4)

    # Estado inicial
    game.board.grid[0][0].set_value(2)
    game.board.grid[0][1].set_value(2)
    initial_score = game.score

    # Realizamos un turno
    move_successful = game.play_turn("left")

    # Verificamos que el movimiento fue válido
    assert move_successful

    # Verificamos que se generó una nueva ficha
    non_empty_cells = sum(
        not cell.is_empty() for row in game.board.grid for cell in row
    )
    assert non_empty_cells == 1

    # Verificamos la puntuación
    assert game.score == initial_score + 4

    # Verificamos el estado del tablero
    assert game.board.grid[0][0].value == 4    



    
# Valors límit i frontera

# Valor limit / frontera: tauler ple amb una cel·la buida

def test_board_full_moves():
    board = Board(size=4)
    game = Game(size=4, board=board)
    values = [
        [2, 4, 2, 4],
        [4, 2, 4, 2],
        [2, 4, 2, 4],
        [4, 2, 0, 2],
    ]
    for i in range(4):
        for j in range(4):
            board.grid[i][j].set_value(values[i][j])
    assert not game.is_game_over()  # Hay movimientos posibles

# Valor limit / frontera: tauler inicial amb només una cel·la

def test_is_game_over_with_empty_cells():
    board = Board(size=4)
    game = Game(size=4, board=board)
    board.grid[0][0].set_value(2)  # Una celda con valor, las demás vacías
    assert not game.is_game_over()  # El juego no termina con celdas vacías

# Valor limit / frontera: tauler completament ple pero hi ha almenys un moviment possible

def test_is_game_over_with_moves_available():
    board = Board(size=4)
    game = Game(size=4, board=board)
    values = [
        [2, 2, 4, 8],
        [16, 32, 64, 128],
        [256, 512, 1024, 2048],
        [2, 4, 8, 16],
    ]
    for i in range(4):
        for j in range(4):
            board.grid[i][j].set_value(values[i][j])
    assert not game.is_game_over()  # Hay movimientos posibles (dos 2 en la primera fila)

# Cas limit on hi ha cel·la amb valor 2048

def test_game_over_victory():
    """
    Prova el cas límit on hi ha una cel·la amb valor 2048.
    """
    board = Board(4)
    board.grid[0][0].set_value(2048)  # Simula una victòria
    game = Game(4, board)
    assert game.is_victory()

# Valor limit i frontera: Tauler completament ple sense moviments possibles
def test_is_game_over_with_full_board_no_moves():
    board = Board(size=4)
    game = Game(size=4, board=board)
    values = [
        [2, 4, 2, 4],
        [4, 2, 4, 2],
        [2, 4, 2, 4],
        [4, 2, 4, 2],
    ]
    for i in range(4):
        for j in range(4):
            board.grid[i][j].set_value(values[i][j])
    assert game.is_game_over()  # Tablero lleno y sin movimientos posibles


# Particions equivalents, valors valids / no valids

def test_play_turn_valid_directions():
    """
    Prova que les direccions vàlides executen moviments correctament.
    """
    game = Game(4)
    for direction in ["left", "right", "up", "down"]:
        assert game.play_turn(direction) in [True, False]  # Retorna True si hi ha canvi
        
def test_play_turn_invalid_directions():
    """
    Prova que les direccions no vàlides llencen una excepció.
    """
    game = Game(4)
    invalid_directions = ["diagonal", "", 123, None]
    for direction in invalid_directions:
        with pytest.raises(ValueError):
            game.play_turn(direction)
            
@pytest.mark.parametrize("initial_grid, expected_grid, direction", [
    ([[0, 2, 2, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], 
      [[4, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], "left"),
    
    ([[0, 2, 2, 0], [0, 0, 0, 0], [0, 0, 0, 0], [2, 0, 0, 0]], 
      [[4, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [2, 0, 0, 0]], "left"),
    
    ([[0, 0, 2, 2], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], 
      [[0, 0, 0, 4], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], "right"),
    
    ([[2, 0, 0, 0], [2, 0, 0, 0], [4, 0, 0, 0], [0, 0, 0, 0]], 
      [[4, 0, 0, 0], [4, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], "up"),
    
    ([[0, 0, 0, 0], [0, 2, 0, 0], [0, 2, 0, 0], [0, 0, 0, 0]], 
      [[0, 4, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], "up"),
    
    ([[2, 0, 0, 0], [2, 0, 0, 0], [0, 0, 0, 0], [4, 0, 0, 0]], 
      [[0, 0, 0, 0], [0, 0, 0, 0], [4, 0, 0, 0], [4, 0, 0, 0]], "down"),
    
     ([[0, 0, 0, 0], [2, 0, 0, 0], [2, 0, 0, 0], [4, 0, 0, 0]], 
      [[0, 0, 0, 0], [0, 0, 0, 0], [4, 0, 0, 0], [4, 0, 0, 0]], "down"),
])
@patch.object(Board, 'add_random_tile')  # Mock para evitar generación aleatoria
def test_play_turn_pairwise(mock_add_random_tile, initial_grid, expected_grid, direction):
    board = Board()
    for i in range(board.size):
        for j in range(board.size):
            board.grid[i][j].set_value(initial_grid[i][j])
    game = Game(size=4, board=board)

    # Llamar a la función de juego
    game.play_turn(direction)
    
    # Comprobar el estado del tablero después del movimiento
    assert [[cell.value for cell in row] for row in game.board.grid] == expected_grid

# Condition coverage and path coverage

def test_is_game_over_moves_available():
    board = Board(size=4)
    board.grid[0][0].set_value(2)  # Hay movimientos disponibles
    game = Game(size=4, board=board)
    assert not game.is_game_over()  # has_moves devuelve True -> Juego no terminado

def test_is_game_over_no_moves():
    board = Board(size=4)
    values = [
        [2, 4, 8, 16],
        [32, 64, 128, 256],
        [512, 1024, 2048, 2],
        [4, 8, 16, 32]
    ]
    for i in range(4):
        for j in range(4):
            board.grid[i][j].set_value(values[i][j])  # Sin movimientos disponibles
    game = Game(size=4, board=board)
    assert game.is_game_over()  # has_moves devuelve False -> Juego terminado
    
def test_is_victory_with_victory():
    board = Board(size=4)
    board.grid[0][0].set_value(2048)  # Una celda con 2048
    game = Game(size=4, board=board)
    assert game.is_victory()  # cell.value == 2048 sale True -> Victoria

def test_is_victory_no_victory():
    board = Board(size=4)
    board.grid[0][0].set_value(2)  # Ninguna celda con 2048
    game = Game(size=4, board=board)
    assert not game.is_victory()  # cell.value == 2048 sale False -> No hay victoria
    
# Path coverage

def test_play_turn_invalid_direction():
    game = Game(size=4)
    with pytest.raises(ValueError):
        game.play_turn("diagonal")  # Camino 1: dirección no válida


def test_play_turn_no_valid_move():
    board = Board(size=4)
    game = Game(size=4, board=board)
    values = [
        [2, 4, 2, 4],
        [4, 2, 4, 2],
        [2, 4, 2, 4],
        [4, 2, 4, 2],
    ]
    for i in range(4):
        for j in range(4):
            board.grid[i][j].set_value(values[i][j])  # Tablero sin movimientos
    assert not game.play_turn("left")  # Camino 2: movimiento inválido
    assert not game.play_turn("right")  # Camino 2: movimiento inválido
    assert not game.play_turn("up")  # Camino 2: movimiento inválido
    assert not game.play_turn("down")  # Camino 2: movimiento inválido


def test_play_turn_valid_move_left():
    board = Board(size=4)
    game = Game(size=4, board=board)
    board.grid[0][0].set_value(2)
    board.grid[0][1].set_value(2)
    assert game.play_turn("left")  # Camino 3: movimiento válido
    non_empty_cells = sum(
        not cell.is_empty() for row in game.board.grid for cell in row
    )
    assert non_empty_cells == 1  # Se añade una nueva ficha


def test_play_turn_valid_move_right():
    board = Board(size=4)
    game = Game(size=4, board=board)
    board.grid[0][2].set_value(2)
    board.grid[0][3].set_value(2)
    assert game.play_turn("right")  # Camino 4: movimiento válido
    non_empty_cells = sum(
        not cell.is_empty() for row in game.board.grid for cell in row
    )
    assert non_empty_cells == 1  # Se añade una nueva ficha


def test_play_turn_valid_move_up():
    board = Board(size=4)
    game = Game(size=4, board=board)
    board.grid[2][0].set_value(2)
    board.grid[3][0].set_value(2)
    assert game.play_turn("up")  # Camino 5: movimiento válido
    non_empty_cells = sum(
        not cell.is_empty() for row in game.board.grid for cell in row
    )
    assert non_empty_cells == 1  # Se añade una nueva ficha


def test_play_turn_valid_move_down():
    board = Board(size=4)
    game = Game(size=4, board=board)
    board.grid[0][0].set_value(2)
    board.grid[1][0].set_value(2)
    assert game.play_turn("down")  # Camino 6: movimiento válido
    non_empty_cells = sum(
        not cell.is_empty() for row in game.board.grid for cell in row
    )
    assert non_empty_cells == 1  # Se añade una nueva ficha
    
# Loop testing 

def test_is_victory_no_iterations():
    board = Board(size=4)  # Tablero 4x4 vacío
    game = Game(size=4, board=board)
    assert not game.is_victory()  # Iteraciones: 0 (sin 2048)

def test_is_victory_one_iteration():
    board = Board(size=4)
    board.grid[0][0].set_value(2048)  # Victoria en la primera celda
    game = Game(size=4, board=board)
    assert game.is_victory()  # Iteraciones: 1

def test_is_victory_multiple_iterations():
    board = Board(size=4)
    board.grid[1][1].set_value(2048)  # Victoria en otra celda
    game = Game(size=4, board=board)
    assert game.is_victory()  # Iteraciones: multiples, pero se detiene en la primera coincidencia

def test_is_victory_no_victory():
    board = Board(size=4)
    game = Game(size=4, board=board)  # Ninguna celda tiene 2048
    assert not game.is_victory()  # Iteraciones: 16 (4x4)
    
# Loop testing 

def test_is_game_over_no_iterations():
    board = Board(size=4)  # Tablero 4x4 lleno
    for i in range(4):
        for j in range(4):
            board.grid[i][j].set_value(2)  # Ninguna celda vacía
    game = Game(size=4, board=board)
    assert not game.is_game_over()  # Iteraciones: 16 (sin ceros)

def test_is_game_over_one_iteration():
    board = Board(size=4)
    for i in range(4):
        for j in range(4):
            board.grid[i][j].set_value(2)  # Rellenar todo menos una celda
    board.grid[0][0].set_value(0)  # Una celda vacía
    game = Game(size=4, board=board)
    assert not game.is_game_over()  # Iteraciones: 1

def test_is_game_over_multiple_iterations():
    board = Board(size=4)
    for i in range(4):
        for j in range(4):
            board.grid[i][j].set_value(2)  # Rellenar todo
    game = Game(size=4, board=board)
    assert not game.is_game_over()  # Iteraciones: 16 (sin ceros)
    
# loop testing

def test_play_turn_no_iterations():
    board = Board(size=4)  # Tablero 4x4 vacío
    game = Game(size=4, board=board)
    assert not game.play_turn("left")  # Sin iteraciones

def test_play_turn_one_iteration():
    board = Board(size=4)
    board.grid[0][0].set_value(2)
    board.grid[0][1].set_value(2)  # Solo una fila con movimiento válido
    game = Game(size=4, board=board)
    assert game.play_turn("left")  # Iteraciones: 1 fila

def test_play_turn_multiple_iterations():
    board = Board(size=4)
    board.grid[0][0].set_value(2)
    board.grid[0][1].set_value(4)  # Varias iteraciones posibles
    game = Game(size=4, board=board)
    assert not game.play_turn("up")  # Iteraciones: varias filas y columnas
    
# valors limit i frontera

def test_play_turn_boundary_values():
    """
    Verifica el comportamiento de play_turn en valores límite y frontera.
    """
    # Caso límite: tablero completamente lleno
    board_full = Board(size=4)
    values_full = [
        [2, 4, 2, 4],
        [4, 2, 4, 2],
        [2, 4, 2, 4],
        [4, 2, 4, 2],
    ]
    for i in range(4):
        for j in range(4):
            board_full.grid[i][j].set_value(values_full[i][j])
    game_full = Game(size=4, board=board_full)
    
    # Intentar mover en una dirección (debería retornar False porque no hay movimientos posibles)
    assert not game_full.play_turn("left")
    assert not game_full.play_turn("right")
    assert not game_full.play_turn("up")
    assert not game_full.play_turn("down")

    # Caso límite: un solo movimiento posible
    board_single_move = Board(size=4)
    values_single_move = [
        [2, 2, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ]
    for i in range(4):
        for j in range(4):
            board_single_move.grid[i][j].set_value(values_single_move[i][j])
    game_single_move = Game(size=4, board=board_single_move)

    # Intentar mover en una dirección (debería retornar True porque hay un movimiento válido)
    assert game_single_move.play_turn("left")
    assert game_single_move.score == 4  # La puntuación debe haber aumentado por el movimiento

    # Verificar el estado del tablero después del movimiento
    assert game_single_move.board.grid[0][0].value == 4  # Los dos 2 deben haberse combinado en 4
    assert game_single_move.board.grid[0][1].is_empty()  # La segunda celda debe estar vacía

    # Caso límite: tablero inicial vacío
    board_empty = Board(size=4)
    game_empty = Game(size=4, board=board_empty)

    # Intentar mover en una dirección (debería retornar False porque no hay movimientos posibles)
    assert not game_empty.play_turn("left")
    assert not game_empty.play_turn("right")
    assert not game_empty.play_turn("up")
    assert not game_empty.play_turn("down")


def test_is_game_over_equivalence_partitions():
        """
        Verifica el comportamiento de is_game_over en particiones equivalentes.
        """
        # Partición 1: El juego NO ha terminado (hay movimientos disponibles)
        board_with_moves = Board(size=4)
        values_with_moves = [
            [2, 2, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ]
        for i in range(4):
            for j in range(4):
                board_with_moves.grid[i][j].set_value(values_with_moves[i][j])
        
        game_with_moves = Game(size=4, board=board_with_moves)
        
        # Asegurarse de que el juego NO ha terminado
        assert not game_with_moves.is_game_over()

        # Partición 2: El juego ha terminado (no hay movimientos disponibles)
        board_no_moves = Board(size=4)
        values_no_moves = [
            [2, 4, 2, 4],
            [4, 2, 4, 2],
            [2, 4, 2, 4],
            [4, 2, 4, 2],
        ]
        for i in range(4):
            for j in range(4):
                board_no_moves.grid[i][j].set_value(values_no_moves[i][j])
        
        game_no_moves = Game(size=4, board=board_no_moves)
        
        # Asegurarse de que el juego ha terminado
        assert game_no_moves.is_game_over()
        
def test_is_victory_equivalence_partitions():
    """
    Verifica el comportamiento de is_victory en particiones equivalentes.
    """
    # Partición 1: El juego ha ganado (hay al menos una celda con valor 2048)
    board_with_victory = Board(size=4)
    values_with_victory = [
        [2, 4, 2, 4],
        [4, 2048, 4, 2],
        [2, 4, 2, 4],
        [4, 2, 4, 2],
    ]
    for i in range(4):
        for j in range(4):
            board_with_victory.grid[i][j].set_value(values_with_victory[i][j])
    
    game_with_victory = Game(size=4, board=board_with_victory)
    
    # Asegurarse de que el juego ha ganado
    assert game_with_victory.is_victory()

    # Partición 2: El juego NO ha ganado (no hay celdas con valor 2048)
    board_no_victory = Board(size=4)
    values_no_victory = [
        [2, 4, 2, 4],
        [4, 8, 4, 2],
        [2, 4, 2, 4],
        [4, 2, 4, 2],
    ]
    for i in range(4):
        for j in range(4):
            board_no_victory.grid[i][j].set_value(values_no_victory[i][j])
    
    game_no_victory = Game(size=4, board=board_no_victory)
    
    # Asegurarse de que el juego NO ha ganado
    assert not game_no_victory.is_victory()
