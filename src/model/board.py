from src.model.cell import Cell

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
