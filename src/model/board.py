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
