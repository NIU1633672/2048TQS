# tests/test_cell.py
import pytest
from src.model.cell import Cell

def test_initialize_empty_cell():
    cell = Cell()
    assert cell.value == 0  # La celda debe estar vacía al inicio
    assert cell.is_empty()  # Método para verificar que está vacía

def test_set_value():
    cell = Cell()
    cell.set_value(2)
    assert cell.value == 2
    assert not cell.is_empty()

def test_set_invalid_value():
    cell = Cell()
    with pytest.raises(ValueError):
        cell.set_value(8)  # Debe lanzar una excepción si el valor no es válido