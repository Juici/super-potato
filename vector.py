import math
from typing import Any


class Vector(object):
    """
    A vector in 2d space, with x and y components.
    """

    def __init__(self, x: float, y: float):
        """
        Creates a vector from the x and y components.

        :param x: float
        :param y: float
        """
        self.x = x
        self.y = y

    # Add

    def add(self, *other) -> 'Vector':
        """
        Add other to this vector, and return this instance.

        :param other: Vector | (float, float) | float, float | float
        :return: Vector
        """

        try:
            # vector
            x = other[0].x
            y = other[0].y
        except TypeError:
            try:
                # tuple
                x = other[0][0]
                y = other[0][1]
            except TypeError:
                try:
                    # args
                    x = other[0]
                    y = other[1]
                except IndexError:
                    # scalar
                    x = other[0]
                    y = other[0]

        self.x += x
        self.y += y

        return self

    def __add__(self, *other) -> 'Vector':
        """
        Add other and this vector, and return the new vector.

        :param other: Vector | (float, float) | float, float | float
        :return: Vector
        """
        return self.copy().add(other)

    def subtract(self, other):
        return self.add(-other)

    def __sub__(self, other):
        return self.copy().subtract(other)

    def negate(self):
        return self.mult(-1)

    def __neg__(self):
        return self.copy().negate()

    def mult(self, k):
        self.x *= k
        self.y *= k
        return self

    def __mul__(self, k):
        return self.copy().mult(k)

    def __rmul__(self, k):
        return self.copy().mult(k)

    def divide_scalar(self, k: float):
        return self.mult(1 / k)

    def __truediv__(self, k: float):
        return self.copy().divide_scalar(k)

    # Normalizes the vector
    def normalize(self):
        return self.divide_scalar(self.length())

    # Returns a normalized version of the vector
    def __abs__(self):
        return self.copy().normalize()

    # Returns the dot product of this vector with another one
    def dot(self, other):
        return self.x * other.x + self.y * other.y

    # Returns the length of the vector
    def length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    # Returns the squared length of the vector
    def length_squared(self):
        return self.x ** 2 + self.y ** 2

    # Reflect this vector on a normal
    def reflect(self, normal):
        n = normal.copy()
        n.mult(2 * self.dot(normal))
        self.sub(n)
        return self

    # Returns the angle between this vector and another one
    # You will need to use the arccosine function:
    # acos in the math library
    def angle(self, other) -> 'Vector':
        """
        Returns the angle between two vectors
        in the range of 0 tp pi radians.
        """
        return math.acos(self.normalize().Dot(other.normalize()))

    def copy(self) -> 'Vector':
        """
        Creates a copy of the vector.

        :return: Vector
        """
        return Vector(self.x, self.y)

    # Equality

    def __eq__(self, other: Any) -> bool:
        """
        Checks equality of this vector and other.

        :param other: Any
        :return: bool
        """
        return self.x == other.x and self.y == other.y

    def __ne__(self, other: Any) -> bool:
        """
        Checks equality of this vector and other.

        :param other: Any
        :return: bool
        """
        return self.x == other.x and self.y == other.y

    # Stringify

    def __str__(self) -> str:
        """
        Returns a string representation of the vector.

        :return: str
        """
        return "(" + str(self.x) + "," + str(self.y) + ")"

    # Support copy module

    def __copy__(self) -> 'Vector':
        """
        Creates a copy of the vector.

        :return: Vector
        """
        return self.copy()

    # Behave like a tuple

    def __getitem__(self, index: int) -> float:
        """
        Returns an indexed item in the vector.

        :param index: int
        :return: float
        """
        if index == 0:
            return self.x
        if index == 1:
            return self.y
        raise IndexError

    def __len__(self) -> int:
        """
        Returns the number of indices in the vector.

        :return: int
        """
        return 2
