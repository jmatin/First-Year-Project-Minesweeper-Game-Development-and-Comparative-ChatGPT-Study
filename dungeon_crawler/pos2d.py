class Pos2D:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
    def __eq__(self, other):
        return other.x == self.x and other.y == self.y


