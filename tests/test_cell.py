# tests/test_cell.py
import pytest
from src.model.cell import Cell

def test_initialize_empty_cell():
    cell = Cell()
    assert cell.value == 0  # La celda debe estar vacía al inicio
    assert cell.is_empty()  # Método para verificar que está vacía

# Tests de particiones equivalentes (Valores válidos / no válidos)

def test_set_value():
    """
    Verifica que los valores válidos se asignan correctamente a la celda.
    """
    cell = Cell()
    valid_values = [2, 4, 8]  # Valores válidos definidos por el juego
    for value in valid_values:
        cell.set_value(value)
        assert cell.value == value  # El valor de la celda debe coincidir con el asignado
        assert not cell.is_empty()  # La celda no debe estar vacía después de asignar un valor

def test_set_invalid_value():
    """
    Verifica que los valores no válidos lancen una excepción al intentar asignarlos.
    """
    cell = Cell()
    invalid_values = [-1, 3, 5, 6, 7, 9, 10, 12]  # Valores no válidos
    for value in invalid_values:
        with pytest.raises(ValueError):
            cell.set_value(value)  # Debe lanzar una excepción si el valor no es válido

# Test de valores límite y frontera

def test_set_value_with_limits_and_boundaries():
    """
    Verifica el comportamiento del método set_value en valores frontera y límite.
    """
    cell = Cell()

    # Valores frontera (válidos)
    cell.set_value(2)  # Frontera inferior
    assert cell.value == 2

    cell.set_value(2048)  # Frontera superior
    assert cell.value == 2048
    
    cell.set_value(16) # Valor interior
    assert cell.value == 16

    invalid_values = [1, 3, 2047, 2049]  # Valores no válidos
    for value in invalid_values:
        with pytest.raises(ValueError):
            cell.set_value(value)  # Debe lanzar una excepción si el valor no es válido
           
    

def test_reset_cell():
    """
    Verifica que una celda pueda ser reseteada a su estado inicial.
    """
    cell = Cell()
    cell.set_value(2)  # Cambiar el valor de la celda
    assert cell.value == 2  # Verificar que el valor ha cambiado
    cell.reset()  # Resetear la celda
    assert cell.value == 0  # Debe estar en el estado inicial
    assert cell.is_empty()  # Debe estar vacía

