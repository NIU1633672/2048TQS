from mocks.mock_cell import MockCellGenerator


class MockController:
    def __init__(self, board, view):
        self.board = board
        self.view = view
        self.cell_generator = MockCellGenerator() 

    def play_turn(self):
        self.board.move_left()  # Lógica para mover el tablero
        self.view.display_board(self.board)  # Mostrar el tablero

    def add_cell(self):
        # Llama a la lógica de agregar celda en el tablero
        cell = self.cell_generator.generate()
        self.board.add_cell()  
