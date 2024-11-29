from src.model.cell import Cell
import random

class Board:
    """
    Clase que representa un tablero de juego para 2048.
    """

    def __init__(self, size):
        """
        Inicializa un tablero vacío de tamaño `size x size`.
        Cada posición del tablero contiene una instancia de la clase Cell.

        :param size: Dimensión del tablero (número de filas y columnas).
        """
        self.size = size
        self.grid = [[Cell() for _ in range(size)] for _ in range(size)]

    def add_random_tile(self):
        """
        Agrega una ficha aleatoria (2 o 4) en una celda vacía.
        """
        # Obtener todas las celdas vacías
        empty_cells = [
            (row, col) for row in range(self.size)
            for col in range(self.size) if self.grid[row][col].is_empty()
        ]
        
        # Si hay celdas vacías, seleccionar una al azar
        if empty_cells:
            row, col = random.choice(empty_cells)
            self.grid[row][col].set_value(random.choice([2, 4]))

    def move_left(self):
        """
        Mueve todas las fichas hacia la izquierda, combinando las que sean iguales.
        """
        for row in self.grid:
            # Extraemos los valores no vacíos
            values = [cell.value for cell in row if not cell.is_empty()]

            # Combinamos valores iguales
            new_values = []
            skip = False
            for i in range(len(values)):
                if skip:
                    skip = False
                    continue
                if i < len(values) - 1 and values[i] == values[i + 1]:
                    new_values.append(values[i] * 2)
                    skip = True  # Saltar la siguiente celda
                else:
                    new_values.append(values[i])

            # Rellenamos con ceros hasta completar el tamaño original de la fila
            new_values.extend([0] * (self.size - len(new_values)))

            # Actualizamos la fila del tablero
            for i in range(self.size):
                row[i].set_value(new_values[i])
