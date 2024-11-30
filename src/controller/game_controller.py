# src/controller/game_controller.py
from src.model.board import Board
from src.view.game_view import GameView

class GameController:
    def __init__(self, size):
        self.board = Board(size)  # Crear tablero
        self.view = GameView()    # Inicializar vista

    def add_random_tile(self):
        """Usa el método de Board para agregar una ficha aleatoria."""
        self.board.add_random_tile()

    def get_board(self):
        """Devuelve el tablero actual."""
        return self.board

    def display(self):
        """Pide a la vista que muestre el tablero actual."""
        self.view.display_board(self.board)

    def move_left(self):
        """
        Realiza un movimiento hacia la izquierda en el tablero.
        """
        self.board.move_left()

    def move_right(self):
        self.board.move_right()

    def move_up(self):
        self.board.move_up()
        
    def move_down(self):
        self.board.move_down()

    def play_turn(self, direction):
        move_successful = self.game.play_turn(direction)
