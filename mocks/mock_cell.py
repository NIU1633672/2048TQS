class MockCell:
    def __init__(self, initial_value=0):
        self.value = initial_value

    def is_empty(self):
        return self.value == 0

    def set_value(self, value):
        if value < 0 or value > 2048 or (value != 0 and (value & (value - 1)) != 0):
            raise ValueError("El valor debe ser 0 o una potencia de 2 y no mayor que 2048")
        self.value = value

    def get_value(self):
        return self.value

    def reset(self):
        self.value = 0

class MockCellGenerator:
    def __init__(self):
        self.called = False

    def generate(self):
        self.called = True
        return MockCell(2)  # Simula siempre generar una celda con valor 2