import unittest
from mocks.mock_board import MockBoard
from mocks.mock_view import MockView
from mocks.mock_controller import MockController
from mocks.mock_cell import MockCellGenerator
from mocks.mock_cell import MockCell
from unittest.mock import Mock
from unittest import TestCase
from unittest.mock import patch
from random import choice
from mockito import mock, when

class TestGame(unittest.TestCase):
    def test_play_turn(self):
        mock_board = MockBoard(4)
        mock_view = MockView()
        mock_controller = MockController(mock_board, mock_view)

        # Aquí puedes realizar la prueba del flujo completo.
        mock_controller.play_turn()

        # Agrega aquí tus aserciones para verificar el comportamiento esperado
        # Por ejemplo, puedes verificar el estado del tablero o el puntaje.

    def test_with_mockito(self):
        # Nuevo test usando mockito
        mock_board = Mock()
        mock_board.move_left.return_value = True  # Simula siempre un éxito

        mock_view = Mock()
        mock_view.display_board.return_value = None

        controller = MockController(mock_board, mock_view)
        controller.play_turn()

        # Verificar que el método move_left fue llamado
        mock_board.move_left.assert_called_once()

        # Verificar que la vista actualizó el tablero
        mock_view.display_board.assert_called_once()
        
    def test_generate_method(self):
        generator = MockCellGenerator()
        cell = generator.generate()

        # Verifica que el método se llamó
        self.assertTrue(generator.called)

        # Verifica que la celda generada tiene el valor esperado
        self.assertIsInstance(cell, MockCell)
        self.assertEqual(cell.get_value(), 2)
        
    def test_cell_addition_with_mockito(self):
        mock_board = MockBoard(4)
        mock_view = MockView()
        mock_controller = MockController(mock_board, mock_view)

        # Crear un mock para el generador de celdas
        mock_cell_generator = mock(MockCellGenerator)
        
        # Configurar el mock para que genere un valor de 2 o 4
        when(mock_cell_generator).generate().thenReturn(MockCell(2))  # Simula que siempre genera una celda con valor 2

        # Reemplazar el generador de celdas en el controlador
        mock_controller.cell_generator = mock_cell_generator

        # Añadir celdas al tablero
        mock_controller.add_cell()
        mock_controller.add_cell()

        # Verificar que al menos dos celdas no estén vacías
        filled_cells = sum(1 for i in range(4) for j in range(4) if mock_board.get_cell_value(i, j) != 0)
        self.assertGreaterEqual(filled_cells, 2)  # Deben haber al menos dos celdas llenas

        # Verificar que las celdas generadas tienen valores válidos (2 o 4)
        for i in range(4):
            for j in range(4):
                value = mock_board.get_cell_value(i, j)
                if value != 0:
                    self.assertIn(value, [2, 4])  # Las celdas deben ser 2 o 4

        
        
    def test_mock_cell(self):
        mock_cell = MockCell()
        assert mock_cell.is_empty()

        mock_cell.set_value(2)
        assert mock_cell.get_value() == 2

        mock_cell.reset()
        assert mock_cell.is_empty() 

if __name__ == '__main__':
    unittest.main()
