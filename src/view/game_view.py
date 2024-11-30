# src/view/game_view.py

class GameView:
    def display_board(self, board):
        """Muestra el tablero actual en la consola."""
        for row in board.grid:
            print(" | ".join(str(cell.value) if not cell.is_empty() else '.' for cell in row))
            print("-" * (board.size * 4 - 1))  # Línea separadora

    def display_score(self, score):
        """Muestra la puntuación actual en la consola."""
        print(f"Score: {score}")

    def display_message(self, message):
        """Muestra un mensaje en la consola."""
        print(message)
        
    def display_end_message(self, game_status):
        if game_status == "won":
            print("¡Has ganado!")
        elif game_status == "lost":
            print("Juego terminado")
