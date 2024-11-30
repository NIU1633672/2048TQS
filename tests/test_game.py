import pytest
from src.model.game import Game

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

def test_is_game_over_with_full_board_no_moves():
    board = Board(size=4)
    game = Game(board=board)
    values = [
        [2, 4, 8, 16],
        [32, 64, 128, 256],
        [512, 1024, 2048, 4096],
        [8192, 16384, 32768, 65536],
    ]
    for i in range(4):
        for j in range(4):
            board.grid[i][j].set_value(values[i][j])
    assert game.is_game_over()  # Tablero lleno y sin movimientos posibles

def test_is_game_over_with_empty_cells():
    board = Board(size=4)
    game = Game(board=board)
    board.grid[0][0].set_value(2)  # Una celda con valor, las demás vacías
    assert not game.is_game_over()  # El juego no termina con celdas vacías

def test_is_game_over_with_moves_available():
    board = Board(size=4)
    game = Game(board=board)
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