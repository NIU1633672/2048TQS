# tests/test_cell.py

from src.model.cell import Cell

def test_initialize_empty_cell():
    cell = Cell()
    assert cell.value == 0  # La celda debe estar vacía al inicio
    assert cell.is_empty()  # Método para verificar que está vacía
