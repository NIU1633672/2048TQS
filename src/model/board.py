from src.model.cell import Cell
import random

class Board:
    """
    Clase que representa un tablero de juego para 2048.
    """

    def __init__(self, size=4):
        """
        Inicializa un tablero vacío de tamaño `size x size`.
        Cada posición del tablero contiene una instancia de la clase Cell.

        size: Dimensión del tablero (número de filas y columnas).
        """
        if size != 4:
            raise ValueError("El tamaño del tablero debe ser 4x4.")
        
        self.size = size
        self.grid = [[Cell() for _ in range(size)] for _ in range(size)]
        self.last_move_score = 0  # Inicializamos el puntaje del último movimiento
        
    def reset(self):
        for row in self.grid:
            for cell in row:
                cell.reset()  # Asume que reset() en Cell establece el valor a 0 


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
        Devuelve True si hubo algún cambio, False en caso contrario.
        """
        self.last_move_score = 0  # Inicializamos el puntaje del último movimiento
        moved = False
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
                    combined_value = values[i] * 2
                    self.last_move_score += combined_value
                    skip = True  # Saltar la siguiente celda
                else:
                    new_values.append(values[i])

            # Rellenamos con ceros hasta completar el tamaño original de la fila
            new_values.extend([0] * (self.size - len(new_values)))

            # Verificamos si hubo cambios
            if new_values != [cell.value for cell in row]:
                moved = True

            # Actualizamos la fila del tablero
            for i in range(self.size):
                row[i].set_value(new_values[i])

        return moved


    def move_right(self):
        """
        Mueve todas las fichas hacia la derecha, combinando las que sean iguales.
        Devuelve True si hubo algún cambio, False en caso contrario.
        """
        self.last_move_score = 0
        moved = False
        for row in self.grid:
            # Extraemos los valores no vacíos
            values = [cell.value for cell in row if not cell.is_empty()]

            # Combinamos valores iguales
            new_values = []
            skip = False
            for i in range(len(values) - 1, -1, -1):  # Iteramos de derecha a izquierda
                if skip:
                    skip = False
                    continue
                if i > 0 and values[i] == values[i - 1]:  # Comparar con la celda a la izquierda
                    new_values.append(values[i] * 2)
                    combined_value = values[i] * 2
                    self.last_move_score += combined_value
                    skip = True  # Saltar la siguiente celda
                else:
                    new_values.append(values[i])

            # Rellenamos con ceros hasta completar el tamaño original de la fila
            new_values.extend([0] * (self.size - len(new_values)))

            # Actualizamos la fila del tablero en el orden correcto (de derecha a izquierda)
            new_values.reverse()  # Invertir para colocar los valores de nuevo en la fila

            # Verificamos si hubo cambios
            if new_values != [cell.value for cell in row]:
                moved = True

            for i in range(self.size):
                row[i].set_value(new_values[i])

        return moved


    def move_up(self):
        """
        Mueve todas las fichas hacia arriba, combinando las que sean iguales.
        Devuelve True si hubo algún cambio, False en caso contrario.
        """
        self.last_move_score = 0
        moved = False
        for col in range(self.size):
            # Extraemos los valores no vacíos
            values = [self.grid[row][col].value for row in range(self.size) if not self.grid[row][col].is_empty()]

            # Combinamos valores iguales
            new_values = []
            skip = False
            for i in range(len(values)):
                if skip:
                    skip = False
                    continue
                if i < len(values) - 1 and values[i] == values[i + 1]:
                    new_values.append(values[i] * 2)
                    combined_value = values[i] * 2
                    self.last_move_score += combined_value
                    skip = True  # Saltar la siguiente celda
                else:
                    new_values.append(values[i])

            # Rellenamos con ceros hasta completar el tamaño original de la columna
            new_values.extend([0] * (self.size - len(new_values)))

            # Verificamos si hubo cambios
            current_column = [self.grid[row][col].value for row in range(self.size)]
            if new_values != current_column:
                moved = True

            # Actualizamos la columna del tablero
            for i in range(self.size):
                self.grid[i][col].set_value(new_values[i])

        return moved
    
    def move_down(self):
        """
        Mueve todas las fichas hacia abajo, combinando las que sean iguales.
        Devuelve True si hubo algún cambio, False en caso contrario.
        """
        self.last_move_score = 0
        moved = False
        for col in range(self.size):
            # Extraemos los valores no vacíos de la columna (de abajo hacia arriba)
            values = [self.grid[row][col].value for row in range(self.size - 1, -1, -1) if not self.grid[row][col].is_empty()]

            # Combinamos valores iguales
            new_values = []
            skip = False
            for i in range(len(values)):
                if skip:
                    skip = False
                    continue
                # Cambiamos la comparación para trabajar correctamente con los índices
                if i < len(values) - 1 and values[i] == values[i + 1]:
                    new_values.append(values[i] * 2)
                    self.last_move_score += values[i] * 2  # Sumar el valor combinado al puntaje
                    skip = True  # Saltar la siguiente celda
                else:
                    new_values.append(values[i])

            # Rellenamos con ceros hasta completar el tamaño original de la columna
            new_values.extend([0] * (self.size - len(new_values)))

            # Verificamos si hubo cambios
            current_column = [self.grid[row][col].value for row in range(self.size)]
            if new_values[::-1] != current_column:  # Revertimos para comparar con la columna original
                moved = True

            # Actualizamos la columna del tablero
            for i in range(self.size):
                self.grid[i][col].set_value(new_values[self.size - 1 - i])  # Colocar desde arriba hacia abajo

        return moved
    
    def is_full(self):
        """Verifica si todas las celdas del tablero están llenas."""
        for row in self.grid:
            for cell in row:
                if cell.is_empty():
                    return False
        return True

    def has_moves(self):
        """
        Verifica si hay movimientos posibles en el tablero:
        - Celdas vacías.
        - Combinaciones posibles entre celdas adyacentes.
        """
        # Verifica si hay celdas vacías
        if not self.is_full():
            return True

        # Verifica si hay combinaciones posibles
        for i in range(self.size):
            for j in range(self.size):
                current_value = self.grid[i][j].value

                # Verifica combinaciones horizontales
                if j + 1 < self.size and self.grid[i][j + 1].value == current_value:
                    return True

                # Verifica combinaciones verticales
                if i + 1 < self.size and self.grid[i + 1][j].value == current_value:
                    return True

        # Si no hay combinaciones posibles
        return False


