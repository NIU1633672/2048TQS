from src.model.board import Board

class Game:
    def __init__(self, size):
        self.board = Board(size)
        self.score = 0

    def play_turn(self, direction):
        """
        Realiza un turno completo en el juego: movimiento, puntuación y nueva ficha.
        """
        # Realizamos el movimiento
        if direction == "left":
            move_successful = self.board.move_left()
        elif direction == "right":
            move_successful = self.board.move_right()
        elif direction == "up":
            move_successful = self.board.move_up()
        elif direction == "down":
            move_successful = self.board.move_down()
        else:
            raise ValueError("Dirección inválida")

        if not move_successful:
            return False

        # Actualizamos la puntuación
        self.score += self.board.last_move_score

        # Añadimos una nueva ficha
        self.board.add_random_tile()

        return True
