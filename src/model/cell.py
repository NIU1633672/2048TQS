# src/model/cell.py

class Cell:
    def __init__(self): 
        # Inicializa celda con valor 0
        self.value = 0
        assert self.is_empty() #Invariante: celda debe estar vacía

    def is_empty(self):
        # Devuelve true si celda esta vacía 
        return self.value == 0

    def set_value(self, value):
        
        #Precondición: valor debe ser 0 o potencia de 2 y menor a 2048
        #Poscondicion: se establece el valor de la celda correctamente
        
        """Método para asignar un valor a la celda, solo 0, 2 o 4 son válidos."""
        if value < 0 or (value != 0 and (value & (value - 1)) != 0) or value > 2048 or value == 1:
            raise ValueError("El valor debe ser 0 o una potencia de 2 y no debe ser mayor que 2048")
        self.value = value
        
        # Poscondicion (valor = 0, o valor = potencia de 2 y menor o igual que 2048)
        if not (self.value == 0 or (self.value > 0 and (self.value & (self.value - 1)) == 0 and self.value <= 2048)):
            raise AssertionError("Poscondición fallida: el valor no es 0 o una potencia de 2 válida.")

    def reset(self):
        """
        Resetea la celda a su valor inicial (vacía).
        """
        self.value = 0
        assert self.is_empty() #Poscondicion: valor de la celda debe ser 0
        
    
    def get_value(self):  # Método que devuelve el valor de la celda
        assert self.value >= 0 #Invariante: El valor de la celda debe ser positivo o 0
        return self.value