from src.model.board import Board

class Game:
    def __init__(self, size, board=None):
        if board is None:
            self.board = Board(size)
        else:
            self.board = board
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

        

        return True

    def is_game_over(self):    
        
        # Si hay movimientos disponibles, el juego no ha terminado
        if self.board.has_moves():
            return False
        
        # Si no hay movimientos disponibles, el juego ha terminado
        return True

    def is_victory(self):
        # Comprobar si hay alguna celda con valor 2048 (victoria)
        for row in self.board.grid:
            for cell in row:
                if cell.value == 2048:
                    return True  # El juego se ha ganado
                
    