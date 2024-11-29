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
