class Board:
    def __init__(self, size):
        self.size = size
        self.grid = [[0] * size for _ in range(size)]
