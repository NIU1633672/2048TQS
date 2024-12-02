class MockView:
    def display_board(self, board):
        # Aquí podrías simplemente imprimir o almacenar el estado del tablero.
        print("Board displayed:", board)

    def get_user_input(self):
        # Simula la entrada del usuario. Devuelve un movimiento simulado.
        return "left"  # Por ejemplo, puede ser "left", "right", "up", "down".

    def show_message(self, message):
        print("Message:", message)

    def update_score(self, score):
        print("Score updated:", score)
