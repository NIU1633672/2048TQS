from src.model.board import Board
from src.view.game_view import GameView
from src.model.game import Game

class GameController:
    def __init__(self, size):
        self.game = Game(size)  # Crear el juego
        self.view = GameView()  # Inicializar vista
        self.board = Board(size)

    def add_random_tile(self):
        """Usa el método de Board para agregar una ficha aleatoria."""
        self.game.board.add_random_tile()

    def get_board(self):
        """Devuelve el tablero actual."""
        return self.game.board

    def display(self):
        """Pide a la vista que muestre el tablero actual."""
        self.view.display_board(self.game.board)
        
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
        """Realiza un movimiento en la dirección especificada."""
        return self.game.play_turn(direction)

    def start_game(self):
        """Inicia el juego y gestiona el bucle principal."""
        self.add_random_tile()  # Agrega una ficha al iniciar el juego
        while True:
            self.display()
            direction = input("Enter move (left, right, up, down or 'exit' to quit): ")
            if direction.lower() == 'exit':
                print("Thanks for playing!")
                break
            if direction in ["left", "right", "up", "down"]:
                move_successful = self.play_turn(direction)
                if not move_successful:
                    print("No valid moves available!")
                else:
                    self.add_random_tile()  # Agregar una ficha después de un movimiento exitoso
            
                # Verificar el estado del juego después del movimiento
                game_status = self.game.check_game_status()
                if game_status in ["won", "lost"]:
                    self.view.display_end_message(game_status)
                    break  # Salir del bucle si el juego ha terminado
                
            else:
                print("Invalid direction! Please use left, right, up, down.")
