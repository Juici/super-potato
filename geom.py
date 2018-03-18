import math

from typing import Tuple, List, Any
from numbers import Real

__all__ = ['Vector', 'Polygon', 'on_segment', 'orientation', 'lines_intersect']


class CollisionBox(object):

    def get_vertices(self) -> Tuple:
        return (
            self.pos, # Top left
            self.pos + self.size.x_vec(), # Top  right
            self.pos + self.size, # Bottom right
            self.pos + self.size.y_vec() # Bottom left
        )

    def is_colliding(self, box: 'CollisionBox') -> bool:
        pos = self.pos
        size = self.size
        other_pos = other.pos
        other_size = other.size
        return (
            pos.x + size.width > other_pos.x and
            pos.x < other_pos.x + other_size.width and
            size.height + pos.y > other_pos.y and
            pos.y < other_pos.y + other_size.height
        )

    def update(self):
        self.position = self.subject.get_pos()
        self.size = self.subject.get_size()

    def __init__(self, subject: 'Renderable'):
        self.subject = subject
        self.update()



class Vector(object):
    """
    A vector in 2d space, with real x and y components.
    """

    def __init__(self, x: Real, y: Real):
        """
        Creates a vector from the x and y components.
        """
        assert isinstance(x, Real)
        assert isinstance(y, Real)

        self.x = x
        self.y = y

    # Add

    def _add_vec(self, other: 'Vector') -> 'Vector':
        """
        Add a vector to this vector, returns this instance.
        """
        assert isinstance(other.x, Real)
        assert isinstance(other.y, Real)

        self.x += other.x
        self.y += other.y

        return self

    def _add_indexable(self, other) -> 'Vector':
        """
        Add a vector to this vector, returns this instance.
        """
        assert isinstance(other[0], Real)
        assert isinstance(other[1], Real)

        self.x += other[0]
        self.y += other[1]

        return self

    def _add_scalar(self, k: Real) -> 'Vector':
        """
        Add a scalar to this vector, and return this instance.
        """
        assert isinstance(k, Real)

        self.x += k
        self.y += k

        return self

    def add(self, other: Any) -> 'Vector':
        """
        Add `other` to this vector, and return this vector.
        """
        try:
            self._add_vec(other)
        except (AttributeError, AssertionError):
            try:
                self._add_indexable(other)
            except (IndexError, TypeError, AssertionError):
                self._add_scalar(other)

        return self

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

    def multiply(self, k: Real) -> 'Vector':
        """
        Performs scalar multiplication on this vector with k.
        Returns this vector.
        """
        assert isinstance(k, Real)

        self.x *= k
        self.y *= k

        return self

    def __mul__(self, k: Real) -> 'Vector':
        """
        Performs scalar multiplication with this vector and k.
        Returns the new vector.
        """
        return self.copy().multiply(k)

    def __rmul__(self, k: Real) -> 'Vector':
        """
        Performs scalar multiplication with this vector and k.
        Returns the new vector.
        """
        return self.copy().multiply(k)

    # Divide

    def divide(self, k: Real) -> 'Vector':
        """
        Performs scalar division on this vector with k.
        Returns this vector.
        """
        assert isinstance(k, Real)

        return self.multiply(1.0 / k)

    def __truediv__(self, k: Real) -> 'Vector':
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
        assert isinstance(other.x, Real)
        assert isinstance(other.y, Real)

        return float(self.x * other.x + self.y * other.y)

    # Length

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

    # Lerp

    def lerp(self, other: 'Vector', factor) -> 'Vector':
        """
        Transitions one vector into another across a line with scalar 'factor'
        """
        return (1.0 - factor) * self + factor * other

    # Copy

    def copy(self) -> 'Vector':
        """
        Creates a copy of the vector.
        """
        return Vector(self.x, self.y)

    # Stripping

    def x_vec(self) -> 'Vector':
        """
        Returns (x, 0)
        """
        return Vector(0, y)

    def y_vec(self) -> 'Vector':
        """
        Returns (0, y)
        """
        return Vector(self.x, 0)


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
            return float(self.x)
        elif index == 1:
            return float(self.y)
        else:
            raise IndexError

    def __setitem__(self, index: int, value: Real):
        """
        Returns an indexed item in the vector.
        """
        if index == 0:
            self.x = value
        elif index == 1:
            self.y = value
        else:
            raise IndexError

    def __len__(self) -> int:
        """
        Returns the number of components in the vector.
        """
        return 2

    # Into

    def into_tuple(self) -> Tuple[float, float]:
        """
        Returns this vector as a tuple.
        """
        return float(self.x), float(self.y)


class Polygon(object):
    """
    Represents a bounding area in the form of a polygon.
    """

    def __init__(self, *points: Vector):
        """
        Constructs a polygon from a list of Vectors.
        """
        self.points = list(points)

    def __getitem__(self, item: int) -> Vector:
        return self.points[item]

    def __setitem__(self, key: int, value: Vector):
        self.points[key] = value

    def __len__(self):
        return len(self.points)

    def __iter__(self):
        yield from self.points

    def contains(self, p: Vector) -> bool:
        """
        Returns `true` if the vector `p` is inside the polygon.
        """
        n = len(self.points)

        i = 0
        j = n - 1
        c = False

        while i < n:
            if ((self.points[i].y > p.y) != (self.points[j].y > p.y)) and (
                    p.x < (self.points[j].x - self.points[i].x) * (p.y - self.points[i].y) / (
                    self.points[j].y - self.points[i].y) + self.points[i].x):
                c = not c

            j = i
            i += 1

        return c

    def into_point_list(self) -> List[Tuple[float, float]]:
        """
        Returns the polygon as point list.
        """
        return [p.into_tuple() for p in self.points]


def on_segment(l: Tuple[Vector, Vector], p: Vector) -> bool:
    """
    Returns `true` if `p` lies on line segment `l`.
    """
    return (min(l[0].x, l[1].x) <= p.x <= max(l[0].x, l[1].x)
            and min(l[0].y, l[1].y) <= p.y <= max(l[0].y, l[1].y))


def orientation(p: Vector, q: Vector, r: Vector) -> int:
    """
    Find the orientation of (p, q, r).
    < 0: anti-clockwise
    0: colinear
    > 0: clockwise
    """
    return (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)


def lines_intersect(l1: Tuple[Vector, Vector], l2: Tuple[Vector, Vector]) -> bool:
    """
    Returns `true` if the lines `l1` and `l2` intersect.
    """
    o1 = orientation(*l1, l2[0])
    o2 = orientation(*l1, l2[1])
    o3 = orientation(*l2, l1[0])
    o4 = orientation(*l2, l1[1])

    if o1 != o2 and o3 != o4:
        return True

    if o1 == 0 and on_segment(l1, l2[0]):
        return True
    if o2 == 0 and on_segment(l1, l2[1]):
        return True
    if o3 == 0 and on_segment(l2, l1[0]):
        return True
    if o4 == 0 and on_segment(l2, l1[1]):
        return True