class MockController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def play_turn(self):
        # Simula una jugada, llama a los métodos del modelo y de la vista.
        self.model.move_left()  # Por ejemplo, simula un movimiento a la izquierda.
        self.view.display_board(self.model.get_board())
        self.view.update_score(self.model.get_score())
