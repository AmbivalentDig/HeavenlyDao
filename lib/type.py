

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def to_tuple(cls, x, y):
        return tuple(x, y)

    def to_tuple(self):
        return tuple([self.x, self.y])

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __str__(self):
        return f"{self.x=} {self.y=}"


