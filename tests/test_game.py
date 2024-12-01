import pytest
from src.model.game import Game
from src.model.board import Board
from src.model.cell import Cell
from unittest.mock import patch

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
    assert non_empty_cells == 2

    # Verificamos la puntuación
    assert game.score == initial_score + 4

    # Verificamos el estado del tablero
    assert game.board.grid[0][0].value == 4
    assert game.board.grid[0][1].is_empty()



    
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

def test_play_turn_valid_move():
    board = Board(size=4)
    game = Game(size=4, board=board)
    board.grid[0][0].set_value(2)
    board.grid[0][1].set_value(2)
    assert game.play_turn("left")  # Camino 3: movimiento válido
    non_empty_cells = sum(
        not cell.is_empty() for row in game.board.grid for cell in row
    )
    assert non_empty_cells == 2  # Se añade una nueva ficha