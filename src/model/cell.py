# src/model/cell.py

class Cell:
    def __init__(self):
        self.value = 0

    def is_empty(self):
        return self.value == 0

    def set_value(self, value):
        """Método para asignar un valor a la celda, solo 0, 2 o 4 son válidos."""
        if value < 0 or (value != 0 and (value & (value - 1)) != 0):
            raise ValueError("El valor debe ser 0 o una potencia de 2")
        self.value = value

    def reset(self):
        """
        Resetea la celda a su valor inicial (vacía).
        """
        self.value = 0
        
    
    def get_value(self):  # Método que devuelve el valor de la celda
        return self.value