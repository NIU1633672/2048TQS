class MockView:
    def display_board(self, board):
        # imprimir o almacenar el estado del tablero.
        print("Board displayed:", board)

    def get_user_input(self):
        # Simula la entrada del usuario. Devuelve un movimiento simulado.
        return "left"  

    def show_message(self, message):
        print("Message:", message)

    def update_score(self, score):
        print("Score updated:", score)
