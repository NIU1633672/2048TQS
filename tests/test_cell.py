# tests/test_cell.py
import pytest
from src.model.cell import Cell
from unittest import TestCase
from unittest.mock import MagicMock

def test_initialize_empty_cell():
    cell = Cell()
    assert cell.value == 0  # La celda debe estar vacía al inicio
    assert cell.is_empty()  # Método para verificar que está vacía

# Tests de particiones equivalentes (Valores válidos / no válidos)

def test_cell_boundary_values():
    # Valor inicial (límite inferior)
    cell = Cell()
    assert cell.value == 0  # Límite inferior esperado
    assert cell.is_empty() == True  # Una celda recién creada debe estar vacía

    # Modificar a un valor válido (límite interior)
    cell.value = 2  # Un valor típico del juego 2048
    assert cell.is_empty() == False  # Ya no está vacía

    # Modificar de vuelta a 0 (límite inferior)
    cell.value = 0
    assert cell.is_empty() == True  # Vuelve a estar vacía

    # Caso borde con un valor límite negativo (aunque en este caso, fuera de los valores válidos del juego)
    cell.value = -1
    assert cell.is_empty() == False  # Una celda con valor negativo no debería considerarse vacía

def test_cell_equivalence_partitions():
    # Partición: celda vacía (valor 0)
    cell_empty = Cell()
    assert cell_empty.is_empty() == True  # Una celda recién creada debe estar vacía

    # Partición: celda con valores válidos del juego (2, 4, 8, ...)
    cell_valid = Cell()
    cell_valid.value = 2
    assert cell_valid.is_empty() == False  # Una celda con valor 2 no está vacía

    cell_valid.value = 4
    assert cell_valid.is_empty() == False  # Una celda con valor 4 no está vacía

    # Partición: celda con valores inválidos (negativos o no usados en el juego)
    cell_invalid = Cell()
    cell_invalid.value = -1
    assert cell_invalid.is_empty() == False  # Una celda con valor negativo no debe considerarse vacía

    cell_invalid.value = 3  # Un valor no estándar en el juego
    assert cell_invalid.is_empty() == False  # Tampoco debería considerarse vacía
    
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

def test_is_empty_boundary_values():
    # Límite inferior: valor 0 (vacío)
    cell = Cell()
    cell.value = 0
    assert cell.is_empty() == True  # Una celda con valor 0 debe estar vacía

    # Límite cercano al inferior: valor 1 (no vacío)
    cell.value = 1
    assert cell.is_empty() == False  # Una celda con valor 1 no está vacía

    # Límite negativo: valor -1 (fuera del dominio normal del juego)
    cell.value = -1
    assert cell.is_empty() == False  # Una celda con valor negativo no está vacía

    # Límite superior (aunque no suele aplicarse en el juego): valor grande positivo
    cell.value = 2048
    assert cell.is_empty() == False  # Una celda con un valor válido del juego no está vacía
    
def test_is_empty_equivalence_partitions():
    # Partición: celdas vacías (valor 0)
    cell = Cell()
    cell.value = 0
    assert cell.is_empty() == True  # Celda vacía

    # Partición: celdas con valores válidos del juego (2, 4, 8, ...)
    cell.value = 2
    assert cell.is_empty() == False  # Celda con valor 2 no está vacía
    cell.value = 4
    assert cell.is_empty() == False  # Celda con valor 4 no está vacía

    # Partición: celdas con valores fuera del rango válido (negativos)
    cell.value = -1
    assert cell.is_empty() == False  # Celda con valor -1 no está vacía

    # Partición: celdas con valores no utilizados en el juego (no múltiplos de 2)
    cell.value = 3
    assert cell.is_empty() == False  # Celda con valor 3 no está vacía
    
def test_reset_boundary_values():
    # Caso límite inferior: valor inicial 0
    cell = Cell()
    cell.value = 0
    cell.reset()
    assert cell.value == 0  # La celda debe estar vacía después del reset

    # Caso límite cercano al inferior: valor inicial 1
    cell.value = 1
    cell.reset()
    assert cell.value == 0  # La celda debe estar vacía después del reset

    # Caso límite alto: valor inicial 2048 (valor máximo en el juego)
    cell.value = 2048
    cell.reset()
    assert cell.value == 0  # La celda debe estar vacía después del reset

    # Caso límite negativo: valor inicial -1 (fuera del dominio normal)
    cell.value = -1
    cell.reset()
    assert cell.value == 0  # La celda debe estar vacía después del reset
    
def test_reset_equivalence_partitions():
    # Partición: celdas vacías (valor 0)
    cell = Cell()
    cell.value = 0
    cell.reset()
    assert cell.is_empty() == True  # Debe mantenerse vacía

    # Partición: celdas con valores válidos del juego (2, 4, 8, ...)
    cell.value = 2
    cell.reset()
    assert cell.is_empty() == True  # Debe estar vacía después del reset
    cell.value = 4
    cell.reset()
    assert cell.is_empty() == True  # Debe estar vacía después del reset

    # Partición: celdas con valores fuera del rango válido (negativos o no múltiplos de 2)
    cell.value = -1
    cell.reset()
    assert cell.is_empty() == True  # Debe estar vacía después del reset
    cell.value = 3
    cell.reset()
    assert cell.is_empty() == True  # Debe estar vacía después del reset