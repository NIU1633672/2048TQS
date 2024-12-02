import unittest
from mocks.mock_board import MockBoard
from mocks.mock_view import MockView
from mocks.mock_controller import MockController

class TestGame(unittest.TestCase):
    def test_play_turn(self):
        mock_board = MockBoard(4)
        mock_view = MockView()
        mock_controller = MockController(mock_board, mock_view)

        # Aquí puedes realizar la prueba del flujo completo.
        mock_controller.play_turn()

        # Agrega aquí tus aserciones para verificar el comportamiento esperado
        # Por ejemplo, puedes verificar el estado del tablero o el puntaje.

if __name__ == '__main__':
    unittest.main()