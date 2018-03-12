import math
import numbers

<<<<<<< HEAD
from typing import Any
=======
from typing import Any, Tuple, List
>>>>>>> 60d34763aaf52a4f78ca4e821767a689de121756


class Vector(object):
    """
    A vector in 2d space, with real x and y components.
    """

    def __init__(self, x: numbers.Real, y: numbers.Real):
        """
        Creates a vector from the x and y components.
        """
        assert isinstance(x, numbers.Real)
        assert isinstance(y, numbers.Real)

        self.x = x
        self.y = y

    # Add

    def _add_vec(self, other: 'Vector') -> 'Vector':
        """
        Add a vector to this vector, returns this instance.
        """
        assert isinstance(other.x, numbers.Real)
        assert isinstance(other.y, numbers.Real)

        self.x += other.x
        self.y += other.y

        return self

    def _add_scalar(self, k: numbers.Real) -> 'Vector':
        """
        Add a scalar to this vector, and return this instance.
        """
        assert isinstance(k, numbers.Real)

        self.x += k
        self.y += k

        return self

    def add(self, other: Any) -> 'Vector':
<<<<<<< HEAD
        """
        Add `other` to this vector, and return this vector.
        """
=======
        """
        Add `other` to this vector, and return this vector.
        """
>>>>>>> 60d34763aaf52a4f78ca4e821767a689de121756
        try:
            self._add_vec(other)
        except AssertionError:
            self._add_scalar(other)
<<<<<<< HEAD

        return self

=======

        return self

>>>>>>> 60d34763aaf52a4f78ca4e821767a689de121756
    def __add__(self, other: Any) -> 'Vector':
        """
        Add `other` and this vector, and return the new vector.
        """
        return self.copy().add(other)

    # Subtract

    def subtract(self, other: Any) -> 'Vector':
        """
        Subtract `other` from this vector, and return this vector.
        """
        return self.add(-other)

    def __sub__(self, other: Any) -> 'Vector':
        """
        Subtract `other` from this vector, and return the new vector.
        """
        return self.copy().subtract(other)

    # Negate

    def negate(self) -> 'Vector':
        """
        Negates this vector, returning this vector.
        """
        return self.multiply(-1)

    def __neg__(self) -> 'Vector':
        """
        Returns the negation of this vector.
        """
        return self.copy().negate()

    # Multiply

    def multiply(self, k: numbers.Real) -> 'Vector':
        """
        Performs scalar multiplication on this vector with k.
        Returns this vector.
        """
        assert isinstance(k, numbers.Real)

        self.x *= k
        self.y *= k

        return self

    def __mul__(self, k: numbers.Real) -> 'Vector':
        """
        Performs scalar multiplication with this vector and k.
        Returns the new vector.
        """
        return self.copy().multiply(k)
<<<<<<< HEAD

    def __rmul__(self, k: numbers.Real) -> 'Vector':
        """
        Performs scalar multiplication with this vector and k.
        Returns the new vector.
        """
        return self.copy().multiply(k)

    # Divide

    def divide(self, k: numbers.Real) -> 'Vector':
        """
        Performs scalar division on this vector with k.
        Returns this vector.
        """
        assert isinstance(k, numbers.Real)

        return self.multiply(1.0 / k)

    def __truediv__(self, k: numbers.Real) -> 'Vector':
        """
        Performs scalar division with this vector and k.
        Returns the new vector.
        """
        return self.copy().divide(k)

    # Normalize

    def normalize(self) -> 'Vector':
        """
        Normalizes this vector. *Length of 1.*
        """
        return self.divide(self.length())

    # Dot product

    def dot(self, other: 'Vector') -> float:
        """
        Returns the dot product of this and the `other` vector.
        """
        assert isinstance(other.x, numbers.Real)
        assert isinstance(other.y, numbers.Real)

        return float(self.x * other.x + self.y * other.y)

    # Length

=======

    def __rmul__(self, k: numbers.Real) -> 'Vector':
        """
        Performs scalar multiplication with this vector and k.
        Returns the new vector.
        """
        return self.copy().multiply(k)

    # Divide

    def divide(self, k: numbers.Real) -> 'Vector':
        """
        Performs scalar division on this vector with k.
        Returns this vector.
        """
        assert isinstance(k, numbers.Real)

        return self.multiply(1.0 / k)

    def __truediv__(self, k: numbers.Real) -> 'Vector':
        """
        Performs scalar division with this vector and k.
        Returns the new vector.
        """
        return self.copy().divide(k)

    # Normalize

    def normalize(self) -> 'Vector':
        """
        Normalizes this vector. *Length of 1.*
        """
        return self.divide(self.length())

    # Dot product

    def dot(self, other: 'Vector') -> float:
        """
        Returns the dot product of this and the `other` vector.
        """
        assert isinstance(other.x, numbers.Real)
        assert isinstance(other.y, numbers.Real)

        return float(self.x * other.x + self.y * other.y)

    # Length

>>>>>>> 60d34763aaf52a4f78ca4e821767a689de121756
    def length_squared(self) -> float:
        """
        Returns the square of the length of this vector. *Faster for comparisons.*
        """
        return self.x ** 2 + self.y ** 2

    def length(self) -> float:
        """
        Returns the length of this vector.
        """
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __abs__(self) -> float:
        """
        Returns the length of this vector.
        """
        return self.length()

    # Reflect

    def reflect(self, normal: 'Vector') -> 'Vector':
        """
        Reflects this vector using the given normal vector.
        """
        n = normal.copy()
        n.multiply(2 * self.dot(normal))
        self.subtract(n)
        return self

    # Angle

    def angle(self, other: 'Vector') -> float:
        """
        Returns an angle between two vectors in the range of 0 to PI radians.
        """
        return math.acos(self.dot(other) / (self.length() * other.length()))

    # Copy

    def copy(self) -> 'Vector':
        """
        Creates a copy of the vector.
        """
        return Vector(self.x, self.y)

    # Equality

    def __eq__(self, other: Any) -> bool:
        """
        Checks equality of this vector and other.
        """
        return isinstance(other, Vector) and self.x == other.x and self.y == other.y

    def __ne__(self, other: Any) -> bool:
        """
        Checks inequality of this vector and other.
        """
        return not self == other

    # Stringify

    def __str__(self) -> str:
        """
        Returns a string representation of the vector.
        """
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

    # Support copy module

    def __copy__(self) -> 'Vector':
        """
        Creates a copy of the vector.
        """
        return self.copy()

    # Behave like a tuple

    def __getitem__(self, index: int) -> float:
        """
        Returns an indexed item in the vector.
        """
        if index == 0:
            return self.x
        if index == 1:
            return self.y
        raise IndexError

    def __setitem__(self, index: int, value: numbers.Real):
        """
        Returns an indexed item in the vector.
        """
        if index == 0:
            self.x = value
        if index == 1:
            self.y = value
        raise IndexError

    def __len__(self) -> int:
        """
        Returns the number of components in the vector.
        """
        return 2

    # Into

    def into_tuple(self) -> Tuple[float, float]:
        return float(self.x), float(self.y)

    def into_list(self) -> List:
        return [float(self.x), float(self.y)]

    # From

    def from_tuple(self, tuple: Tuple[float, float]):
        return Vector(tuple[0], tuple[1])

    def from_list(self, list: List):
        return Vector(list[0], list[1])