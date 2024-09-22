from __future__ import annotations

from collections.abc import Iterable


class Vec:
    """
    A class representing a mathematical vector with arbitrary dimensions.

    This class supports various vector operations such as addition, subtraction,
    multiplication (dot product), division, and normalization.

    Attributes:
        `__coords` (tuple[float | int, ...]): The coordinates of the vector.

    Examples:
        >>> v1 = Vec(1, 2, 3)
        >>> v2 = Vec(4, 5, 6)
        >>> v3 = v1 + v2
        >>> v3
        (5, 7, 9)
        >>> v3.norm()
        14.0
    """

    def __init__(self, *coord) -> None:
        """
        Initialize a vector with given coordinates.

        Args:
            *coord (float | int) or iterable: Coordinate values for the vector.
        """
        if len(coord) == 1 and isinstance(coord[0], Iterable):
            # If a single iterable is passed, unpack its contents
            self.__coords: tuple[float | int, ...] = tuple(coord[0])
        else:
            # Otherwise, treat each element of coord as individual coordinates
            self.__coords = coord

    def norm(self) -> float:
        """
        Calculate the Euclidean norm (magnitude) of the vector.

        Returns:
            float: The magnitude of the vector.
        """
        return sum(c**2 for c in self.__coords) ** 0.5

    def __str__(self) -> str:
        """
        Return a string representation of the vector.

        Returns:
            str: A string in the format "(x, y, z, ...)"
        """
        return f"({", ".join(str(c) for c in self.__coords)})"

    def __repr__(self) -> str:
        """
        Return a string representation of the vector.

        Returns:
            str: Same as __str__ method.
        """
        return self.__str__()

    def __neg__(self) -> Vec:
        """
        Negate the vector.

        Returns:
            Vec: A new vector with all coordinates negated.
        """
        return Vec(*(-c for c in self.__coords))

    def __add__(self, other: object) -> Vec:
        """
        Add another vector or a scalar to this vector.

        Args:
            other (Vec | int | float): The vector or scalar to add.

        Returns:
            Vec: A new vector representing the sum.

        Raises:
            ValueError: If adding vectors of different sizes.
            TypeError: If the operation is not supported.
        """
        if isinstance(other, Vec):
            if len(self.__coords) != len(other.__coords):
                raise ValueError("Cannot add vectors of different sizes")

            return Vec(*(a + b for a, b in zip(self.__coords, other.__coords)))

        if isinstance(other, (int, float)):
            return Vec(*(a + other for a in self.__coords))

        raise TypeError(
            f"Unsupported operation (+) between types {type(self).__name__}"
            f" and {type(other).__name__}"
        )

    def __radd__(self, other: object) -> Vec:
        """
        Add this vector to a scalar (right-side addition).

        Args:
            other (int | float): The scalar to add.

        Returns:
            Vec: A new vector representing the sum.
        """
        return self.__add__(other)

    def __sub__(self, other: object) -> Vec:
        """
        Subtract another vector or a scalar from this vector.

        Args:
            other (Vec | int | float): The vector or scalar to subtract.

        Returns:
            Vec: A new vector representing the difference.

        Raises:
            ValueError: If subtracting vectors of different sizes.
            TypeError: If the operation is not supported.
        """
        if isinstance(other, Vec):
            if len(self.__coords) != len(other.__coords):
                raise ValueError("Cannot subtract vectors of different sizes")

            return Vec(*(a - b for a, b in zip(self.__coords, other.__coords)))

        if isinstance(other, (int, float)):
            return Vec(*(a - other for a in self.__coords))

        raise TypeError(
            f"Unsupported operation (-) between types {type(self).__name__}"
            f" and {type(other).__name__}"
        )

    def __rsub__(self, other: object) -> Vec:
        """
        Subtract this vector from another vector or scalar (right-side subtraction).

        Args:
            other (Vec | int | float): The vector or scalar to subtract from.

        Returns:
            Vec: A new vector representing the difference.

        Raises:
            ValueError: If subtracting vectors of different sizes.
            TypeError: If the operation is not supported.
        """
        if isinstance(other, Vec):
            if len(self.__coords) != len(other.__coords):
                raise ValueError("Cannot subtract vectors of different sizes")

            return Vec(*(b - a for a, b in zip(self.__coords, other.__coords)))

        if isinstance(other, (int, float)):
            return Vec(*(other - a for a in self.__coords))

        raise TypeError(
            f"Unsupported operation (-) between types {type(other).__name__}"
            f" and {type(self).__name__}"
        )

    def __mul__(self, other: object) -> float | int:
        """
        Multiply this vector by another vector (dot product) or a scalar.

        Args:
            other (Vec | int | float): The vector or scalar to multiply by.

        Returns:
            float | int: The result of the multiplication.

        Raises:
            ValueError: If multiplying vectors of different sizes.
            TypeError: If the operation is not supported.
        """
        if isinstance(other, Vec):
            if len(self.__coords) != len(other.__coords):
                raise ValueError("Cannot multiply vectors of different sizes")

            return sum(a * b for a, b in zip(self.__coords, other.__coords))

        if isinstance(other, (int, float)):
            return sum(a * other for a in self.__coords)

        raise TypeError(
            f"Unsupported operation (*) between types {type(self).__name__}"
            f" and {type(other).__name__}"
        )

    def __rmul__(self, other: object) -> Vec | float:
        """
        Multiply this vector by another vector (dot product) or a scalar.

        Args:
            other (Vec | int | float): The vector or scalar to multiply by.

        Returns:
            float | int: The result of the multiplication.

        Raises:
            ValueError: If multiplying vectors of different sizes.
            TypeError: If the operation is not supported.
        """
        return self.__mul__(other)

    def __eq__(self, other: object) -> bool:
        """
        Check if this vector is equal to another vector.

        Args:
            other (object): The object to compare with.

        Returns:
            bool: True if the vectors are equal, False otherwise.
        """
        if isinstance(other, Vec):
            return self.__coords == other.__coords

        if isinstance(other, (int, float)) and other == 0:
            if all(a == 0 for a in self.__coords):
                return True

        return False

    def __ne__(self, other: object) -> bool:
        """
        Check if this vector is not equal to another vector.

        Args:
            other (object): The object to compare with.

        Returns:
            bool: True if the vectors are not equal, False otherwise.
        """
        return not self.__eq__(other)

    def __truediv__(self, other: object) -> Vec | float:
        """
        Divide this vector by another vector or a scalar.

        Args:
            other (Vec | int | float): The vector or scalar to divide by.

        Returns:
            Vec | float: A new vector representing the division result.

        Raises:
            ValueError: If dividing vectors of different sizes.
            ZeroDivisionError: If dividing by zero.
            TypeError: If the operation is not supported.
        """
        if isinstance(other, Vec):
            if other == 0:
                raise ZeroDivisionError("Vector cannot be divided by zero")

            if len(self.__coords) != len(other.__coords):
                raise ValueError("Cannot divide vectors of different sizes")

            return Vec(*(a / b for a, b in zip(self.__coords, other.__coords)))

        if isinstance(other, (int, float)):
            if other == 0:
                raise ZeroDivisionError

            return Vec(*(a / other for a in self.__coords))

        raise TypeError(
            f"Unsupported operation (/) between types {type(self).__name__}"
            f" and {type(other).__name__}"
        )

    def __rtruediv__(self, other: object) -> Vec | float:
        """
        Divide a scalar or another vector by this vector (right-side division).

        Args:
            other (Vec | int | float): The scalar or vector to be divided.

        Returns:
            Vec | float: A new vector representing the division result.

        Raises:
            ValueError: If dividing vectors of different sizes.
            ZeroDivisionError: If dividing by zero.
            TypeError: If the operation is not supported.
        """
        if isinstance(other, Vec):
            if other == 0:
                raise ZeroDivisionError("Vector cannot be divided by zero")

            if len(self.__coords) != len(other.__coords):
                raise ValueError("Cannot divide vectors of different sizes")

            return Vec(*(b / a for a, b in zip(self.__coords, other.__coords)))

        if isinstance(other, (int, float)):
            if other == 0:
                raise ZeroDivisionError

            return Vec(*(other / a for a in self.__coords))

        raise TypeError(
            f"Unsupported operation (/) between types {type(other).__name__}"
            f" and {type(self).__name__}"
        )

    def __iadd__(self, other: object) -> Vec:
        """
        Add another vector or a scalar to this vector in-place.

        Args:
            other (Vec | int | float): The vector or scalar to add.

        Returns:
            Vec: This vector after the addition.

        Raises:
            ValueError: If adding vectors of different sizes.
            TypeError: If the operation is not supported.
        """
        if isinstance(other, Vec):
            if len(self.__coords) != len(other.__coords):
                raise ValueError("Cannot add vectors of different sizes")

            self.__coords = tuple(
                a + b for a, b in zip(self.__coords, other.__coords)
            )

        elif isinstance(other, (int, float)):
            self.__coords = tuple(a + other for a in self.__coords)

        else:
            raise TypeError(
                f"Unsupported operation (+) between types {type(self).__name__}"
                f" and {type(other).__name__}"
            )

        return self

    def __isub__(self, other: object) -> Vec:
        """
        Subtract another vector or a scalar from this vector in-place.

        Args:
            other (Vec | int | float): The vector or scalar to subtract.

        Returns:
            Vec: This vector after the subtraction.

        Raises:
            ValueError: If subtracting vectors of different sizes.
            TypeError: If the operation is not supported.
        """
        if isinstance(other, Vec):
            if len(self.__coords) != len(other.__coords):
                raise ValueError("Cannot subtract vectors of different sizes")

            self.__coords = tuple(
                a - b for a, b in zip(self.__coords, other.__coords)
            )

        elif isinstance(other, (int, float)):
            self.__coords = tuple(a - other for a in self.__coords)

        else:
            raise TypeError(
                f"Unsupported operation (-) between types {type(self).__name__}"
                f" and {type(other).__name__}"
            )

        return self

    def __imul__(self, other: object) -> Vec:
        """
        Multiply this vector by another vector or a scalar in-place.

        Args:
            other (Vec | int | float): The vector or scalar to multiply by.

        Returns:
            Vec: This vector after the multiplication.

        Raises:
            ValueError: If multiplying vectors of different sizes.
            TypeError: If the operation is not supported.
        """
        if isinstance(other, Vec):
            if len(self.__coords) != len(other.__coords):
                raise ValueError("Cannot multiply vectors of different sizes")

            self.__coords = tuple(
                a * b for a, b in zip(self.__coords, other.__coords)
            )

        elif isinstance(other, (int, float)):
            self.__coords = tuple(a * other for a in self.__coords)

        else:
            raise TypeError(
                f"Unsupported operation (*) between types {type(self).__name__}"
                f" and {type(other).__name__}"
            )

        return self

    def __itruediv__(self, other: object) -> Vec:
        """
        Divide this vector by another vector or a scalar in-place.

        Args:
            other (Vec | int | float): The vector or scalar to divide by.

        Returns:
            Vec: This vector after the division.

        Raises:
            ValueError: If dividing vectors of different sizes.
            ZeroDivisionError: If dividing by zero.
            TypeError: If the operation is not supported.
        """
        if isinstance(other, Vec):
            if len(self.__coords) != len(other.__coords):
                raise ValueError("Cannot divide vectors of different sizes")

            self.__coords = tuple(
                a / b for a, b in zip(self.__coords, other.__coords)
            )

        elif isinstance(other, (int, float)):
            if other == 0:
                raise ZeroDivisionError

            self.__coords = tuple(a / other for a in self.__coords)

        else:
            raise TypeError(
                f"Unsupported operation (/) between types {type(self).__name__}"
                f" and {type(other).__name__}"
            )

        return self

    def __abs__(self) -> float:
        """
        Calculate the absolute value (magnitude) of the vector.

        Returns:
            float: The magnitude of the vector.
        """
        return self.norm()

    def __len__(self) -> int:
        """
        Get the number of dimensions of the vector.

        Returns:
            int: The number of coordinates in the vector.
        """
        return len(self.__coords)


def main():
    v1 = Vec(1, 2, 3, 4, 5, 6)
    v2 = Vec(1, 2, 3, 4, 5, 6)
    v4 = Vec(1, 3, 4)
    v3 = Vec(5, 6, 9)
    v5 = Vec([1, 2, 3])

    print(v5)

    # print(v1 + v2)
    print(1 + v2)
    print(v4 * v3)
    print(v2 + 1)
    print(v2 - 1)
    print(1 - v2)

    print(v1 * 2)
    print(v1 * v2)
    print(v1)
    print(v1 != v2)
    zero = Vec(0, 0, 0)

    print(v1 / zero)
    # print(v1 + "hello")


if __name__ == "__main__":
    main()
