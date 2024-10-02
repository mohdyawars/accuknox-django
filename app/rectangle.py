class Rectangle:
    """A class to represent a rectangle."""

    length: int
    width: int

    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def __iter__(self):
        yield {"length": self.length}
        yield {"width": self.width}
