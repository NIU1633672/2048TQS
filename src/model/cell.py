# src/model/cell.py

class Cell:
    def __init__(self):
        self.value = 0

    def is_empty(self):
        return self.value == 0

    def set_value(self, value):
        """Método para asignar un valor a la celda, solo 0, 2 o 4 son válidos."""
        if value not in [0, 2, 4]:
            raise ValueError("El valor debe ser 0, 2 o 4")
        self.value = value

    def reset(self):
        """
        Resetea la celda a su valor inicial (vacía).
        """
        self.value = 0