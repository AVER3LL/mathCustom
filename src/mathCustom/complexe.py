from __future__ import annotations

from math import atan2, cos, pi, sin, sqrt


class Compl:
    """
    A class representing complex numbers.

    This class provides functionality for creating and manipulating complex numbers,
    including basic arithmetic operations, trigonometric representations, and other
    utility methods. It can be initialized with separate real and imaginary parts,
    or from a Python complex number.

    Attributes:
        `real` (float | complex, optional): The real part of the complex number
                                                  or a complex number to convert.
                                                  Defaults to 0.
        `img` (float, optional): The imaginary part of the complex number. Defaults to 0.

    Examples:
        >>> c1 = Compl(3, 4)
        >>> print(c1)
        (3 + 4i)
        >>> c2 = Compl(1, 1)
        >>> c3 = c1 + c2
        >>> print(c3)
        (4 + 5i)
        >>> c4 = Compl(complex(1, 1))
        >>> print(c4)
        (1 + i)
    """

    def __init__(self, real: float | complex | None = None, img: float | None = None) -> None:
        """
        Initialize a new complex number with given real and imaginary parts,
        or from an existing complex number.

        Args:
            real (float | complex | None): The real part of the complex number,
                                                 or a complex number to convert.
                                                 Defaults to 0.
            img (float | None): The imaginary part of the complex number.
                                      Ignored if 'real' is a complex number.
                                      Defaults to 0.
        """
        if isinstance(real, complex):
            self.real: float = real.real
            self.img: float = real.imag

        else:
            self.real = real if real else 0
            self.img = img if img else 0

    def norm(self) -> float:
        """
        Calculate the norm (magnitude) of the complex number.

        Returns:
            * float: The norm of the complex number.

        Example:
            >>> c = Compl(3, 4)
            >>> c.norm()
            5.0
        """
        return sqrt(self.real**2 + self.img**2)

    def conjugate(self) -> Compl:
        """
        Calculate the conjugate of the complex number.

        Returns:
            Compl: A new Compl object representing the conjugate.

        Example:
            >>> c = Compl(3, 4)
            >>> print(c.conjugate())
            (3 - 4i)
        """
        return Compl(self.real, -self.img)

    def reciprocal(self) -> Compl:
        """
        Calculate the reciprocal of the complex number.

        Returns:
            Compl: A new Compl object representing the reciprocal.

        Example:
            >>> c = Compl(3, 4)
            >>> print(c.reciprocal())
            (0.6 - 0.8i)
        """

        # https://en.wikipedia.org/wiki/Complex_number
        # 1 / (a + bi) = (a - bi) / (a^2 + b^2) = (a / (a^2 + b^2)) - (b / (a^2 + b^2))i
        return Compl(
            self.real / (self.real**2 + self.img**2),
            -self.img / (self.real**2 + self.img**2),
        )

    def trig(self) -> tuple[float, float]:
        """
        Calculate the trigonometric representation of the complex number.

        Returns:
            tuple[float, float]: A tuple containing:
                - The norm of the complex number
                - The angle in radians

        Example:
            >>> c = Compl(1, 1)
            >>> norm, angle = c.trig()
            >>> print(f"Norm: {norm:.2f}, Angle: {angle:.2f}")
            Norm: 1.41, Angle: 0.79
        """
        return self.norm(), atan2(self.img, self.real)

    def __str__(self) -> str:
        """
        Return a string representation of the complex number.

        Returns:
            str: A string in the format "(real, img)".

        Example:
            >>> c = Compl(1, 1)
            >>> print(c)
            (1 + 1i)
        """
        realDisp: str = ""
        sign: str = ""
        imgDisp: str = ""

        if self.real != 0:
            realDisp = f"{self.real:g}"

        if self.img > 0:
            sign = "+" if self.real != 0 else ""
        elif self.img < 0:
            sign = "-"

        abs_img = abs(self.img)
        if abs_img == 1:
            imgDisp = "i"  # Displays 1i as just i
        elif abs_img != 0:
            imgDisp = f"{abs_img:g}i"

        if not realDisp and not imgDisp:
            return "0"

        return (
            f"({realDisp}"
            f"{' ' if realDisp and sign else ''}"
            f"{sign}"
            f"{' ' if sign else ''}"
            f"{imgDisp})"
        )

    def __repr__(self) -> str:
        """
        Return a string representation of the complex number.

        Returns:
            str: Same as __str__ method.

        Example:
            >>> c = Compl(1, 1)
            >>> print(repr(c))
            (1 + 1i)
        """
        return self.__str__()

    def __add__(self, other) -> Compl:
        """
        Add another complex number or a scalar to this complex number.

        Args:
            other (Compl | int | float): The complex number or scalar to add.

        Returns:
            Compl: A new complex number representing the sum.

        Raises:
            TypeError: If the operation is not supported.
        """
        if isinstance(other, Compl):
            # https://en.wikipedia.org/wiki/Complex_number
            # (a + bi) + (c + di) = (a+c) + (b+d)i
            return Compl(self.real + other.real, self.img + other.img)

        elif isinstance(other, (int, float)):
            return Compl(self.real + other, self.img)

        raise TypeError(
            f"Unsupported operation (+) between types {type(self).__name__}"
            f" and {type(other).__name__}"
        )

    def __radd__(self, other) -> Compl:
        """
        Add this complex number to a scalar (right-side addition).

        Args:
            other (int | float): The scalar to add.

        Returns:
            Compl: Same as __add__ method. A new complex number representing the sum.

        Raises:
            TypeError: If the operation is not supported.
        """
        return self.__add__(other)

    def __sub__(self, other) -> Compl:
        """
        Subtract another complex number or a scalar from this complex number.

        Args:
            other (Compl | int | float): The complex number or scalar to subtract.

        Returns:
            Compl: A new complex number representing the difference.

        Raises:
            TypeError: If the operation is not supported.
        """
        if isinstance(other, Compl):
            # https://en.wikipedia.org/wiki/Complex_number
            # (a + bi) - (c + di) = (a - c) + (b - d)i
            return Compl(self.real - other.real, self.img - other.img)

        elif isinstance(other, (int, float)):
            return Compl(self.real - other, self.img)

        raise TypeError(
            f"Unsupported operation (-) between types {type(self).__name__}"
            f" and {type(other).__name__}"
        )

    def __rsub__(self, other) -> Compl:
        """
        Subtract this complex number from a scalar (right-side subtraction).

        Args:
            other (int | float): The scalar to subtract.

        Returns:
            Compl: A new complex number representing the difference.

        Raises:
            TypeError: If the operation is not supported.
        """
        if isinstance(other, Compl):
            return Compl(other.real - self.real, other.img - self.img)

        elif isinstance(other, (int, float)):
            return Compl(other - self.real, -self.img)

        raise TypeError(
            f"Unsupported operation (-) between types {type(other).__name__}"
            f" and {type(self).__name__}"
        )

    def __mul__(self, other) -> Compl:
        """
        Multiply this complex number by another complex number or a scalar.

        Args:
            other (Compl | int | float): The complex number or scalar to multiply by.

        Returns:
            Compl: A new complex number representing the product.

        Raises:
            TypeError: If the operation is not supported.
        """
        realPart: float = 0
        imgPart: float = 0

        if isinstance(other, Compl):
            # https://en.wikipedia.org/wiki/Complex_number
            # (a + bi)(c + di) = (ac - bd) + (ad + bc)i
            realPart = (self.real * other.real) - (self.img * other.img)
            imgPart = (self.real * other.img) + (self.img * other.real)

        elif isinstance(other, (int, float)):
            realPart = other * self.real
            imgPart = other * self.img

        else:
            raise TypeError(
                f"Unsupported operation (*) between types {type(self).__name__}"
                f"and {type(other).__name__}"
            )

        return Compl(realPart, imgPart)

    def __rmul__(self, other) -> Compl:
        """
        Multiply this complex number by a scalar (right-side multiplication).

        Args:
            other (int | float): The scalar to multiply by.

        Returns:
            Compl: A new complex number representing the product.

        Raises:
            TypeError: If the operation is not supported.
        """
        return self.__mul__(other)

    def __neg__(self) -> Compl:
        """
        Negate the complex number.

        Returns:
            Compl: A new complex number with all coordinates negated.
        """
        return Compl(-self.real, -self.img)

    def __eq__(self, other) -> bool:
        """
        Check if this complex number is equal to another complex number or a scalar.

        Args:
            other (Compl | int | float): The complex number or scalar to compare with.

        Returns:
            bool: True if the complex numbers are equal, False otherwise.
        """
        if isinstance(other, Compl):
            return (self.real == other.real) and (self.img == other.img)

        elif isinstance(other, (int, float)) and other == 0:
            return self.real + self.img == other

        return False

    def __ne__(self, other) -> bool:
        """
        Check if this complex number is not equal to another complex number or a scalar.

        Args:
            other (Compl | int | float): The complex number or scalar to compare with.

        Returns:
            bool: True if the complex numbers are not equal, False otherwise.
        """
        return not self.__eq__(other)

    def __truediv__(self, other) -> Compl:
        """
        Divide this complex number by another complex number or a scalar.

        Args:
            other (Compl | int | float): The complex number or scalar to divide by.

        Returns:
            Compl: A new complex number representing the division result.

        Raises:
            ZeroDivisionError: If the scalar is zero.
            TypeError: If the operation is not supported.
        """
        if isinstance(other, Compl):
            if other == 0:
                raise ZeroDivisionError("Tried to divide by complex number 0")

            # https://en.wikipedia.org/wiki/Complex_number
            realPart: float = (
                (self.real * other.real) + (self.img * other.img)
            ) / (other.real**2 + other.img**2)

            imgPart: float = (
                (self.img * other.real) - (other.img * self.real)
            ) / (other.real**2 + other.img**2)

            return Compl(realPart, imgPart)

        elif isinstance(other, (int, float)):
            if other == 0:
                raise ZeroDivisionError

            return Compl(self.real / other, self.img / other)

        raise TypeError(
            f"Unsupported operation (/) between types {type(self).__name__}"
            f" and + {type(other).__name__}"
        )

    def __rtruediv__(self, other) -> Compl:
        """
        Divide a complex number by a scalar (right-side division).

        Args:
            other (int | float): The scalar to divide by.

        Returns:
            Compl: A new complex number representing the division result.

        Raises:
            ZeroDivisionError: If the scalar is zero.
            TypeError: If the operation is not supported.
        """
        realPart: float = 0
        imgPart: float = 0

        if isinstance(other, Compl):
            realPart = ((other.real * self.real) + (other.img * self.img)) / (
                self.real**2 + self.img**2
            )

            imgPart = ((other.img * self.real) - (self.img * other.real)) / (
                self.real**2 + self.img**2
            )

        elif isinstance(other, (int, float)):
            if not self.real and not self.img:
                raise ZeroDivisionError(
                    "Complex number at the denominator happens to be 0"
                )

            conj: Compl = self.conjugate()
            realPart = (other * self.real) / (self.real**2 + self.img**2)
            imgPart = (other * self.img) / (self.real**2 + self.img**2)

            if conj.img < 0:
                imgPart *= -1

        else:
            raise TypeError("Tried to divide with a non digit type")

        return Compl(realPart, imgPart)

    def __pow__(self, exponent) -> Compl:
        """
        Raise this complex number to a given exponent.

        Args:
            exponent (int | float): The exponent to raise to.

        Returns:
            Compl: A new complex number representing the result of the operation.

        Raises:
            TypeError: If the exponent is not a real number.
            ValueError: If the exponent is zero.
        """
        if not isinstance(exponent, (int, float)):
            raise TypeError("Exponent must be a real number")

        if exponent == 0:
            return Compl(1, 0)

        if self.real == 0 and self.img == 0:
            if exponent > 0:
                return Compl(0, 0)
            else:
                raise ValueError("Cannot raise 0 to a negative or zero power")

        r, theta = self.trig()
        new_r = r**exponent
        new_theta = theta * exponent

        # Handle potential precision issues for purely real or imaginary results
        if abs(new_theta) < 1e-10 or abs(abs(new_theta) - pi) < 1e-10:
            return Compl(round(new_r * cos(new_theta), 10), 0)
        elif abs(abs(new_theta) - pi / 2) < 1e-10:
            return Compl(0, round(new_r * sin(new_theta), 10))

        return Compl(new_r * cos(new_theta), new_r * sin(new_theta))

    def __iadd__(self, other) -> Compl:
        """
        Add another complex number or a scalar to this complex number in-place.

        Args:
            other (Compl | int | float): The complex number or scalar to add.

        Returns:
            Compl: This complex number after the addition.

        Raises:
            TypeError: If the operation is not supported.
        """
        if isinstance(other, Compl):
            self.real += other.real
            self.img += other.img

        elif isinstance(other, (int, float)):
            self.real += other

        else:
            raise TypeError(
                f"Unsupported operation (+) between types {type(self).__name__}"
                f" and {type(other).__name__}"
            )

        return self

    def __isub__(self, other) -> Compl:
        """
        Subtract another complex number or a scalar from this complex number in-place.

        Args:
            other (Compl | int | float): The complex number or scalar to subtract.

        Returns:
            Compl: This complex number after the subtraction.

        Raises:
            TypeError: If the operation is not supported.
        """
        if isinstance(other, Compl):
            self.real -= other.real
            self.img -= other.img

        elif isinstance(other, (int, float)):
            self.real -= other

        else:
            raise TypeError(
                f"Unsupported operation (-) between types {type(self).__name__}"
                f" and {type(other).__name__}"
            )

        return self

    def __imul__(self, other) -> Compl:
        """
        Multiply this complex number by another complex number or a scalar in-place.

        Args:
            other (Compl | int | float): The complex number or scalar to multiply by.

        Returns:
            Compl: This complex number after the multiplication.

        Raises:
            TypeError: If the operation is not supported.
        """
        if isinstance(other, Compl):
            self.real = (self.real * other.real) - (self.img * other.img)
            self.img = (self.real * other.img) + (self.img * other.real)

        elif isinstance(other, (int, float)):
            self.real *= other
            self.img *= other

        else:
            raise TypeError(
                f"Unsupported operation (*) between types {type(self).__name__}"
                f" and {type(other).__name__}"
            )

        return self

    def __itruediv__(self, other) -> Compl:
        """
        Divide this complex number by another complex number or a scalar in-place.

        Args:
            other (Compl | int | float): The complex number or scalar to divide by.

        Returns:
            Compl: This complex number after the division.

        Raises:
            TypeError: If the operation is not supported.
            ZeroDivisionError: If the divisor is zero.
        """
        if isinstance(other, Compl):
            self.real = ((self.real * other.real) + (self.img * other.img)) / (
                other.real**2 + other.img**2
            )

            self.img = ((self.img * other.real) - (other.img * self.real)) / (
                other.real**2 + other.img**2
            )

        elif isinstance(other, (int, float)):
            if other == 0:
                raise ZeroDivisionError
            self.real /= other
            self.img /= other

        else:
            raise TypeError(
                f"Unsupported operation (/) between types {type(self).__name__}"
                f" and {type(other).__name__}"
            )

        return self

    def __abs__(self) -> float:
        """
        Calculate the absolute value (magnitude) of the complex number.

        Returns:
            float: The magnitude of the complex number.
        """
        return self.norm()

    def __int__(self) -> int:
        """
        Convert the norm (magnitude) of the complex number to an integer.

        Returns:
            int: The norm of the complex number as a float
        """
        if self.img == 0:
            return int(self.real)
        return int(self.norm())

    def __float__(self) -> float:
        """
        Convert the norm (magnitude) of the complex number to a float.

        Returns:
            float: The norm of the complex number as a float.
        """
        if self.img == 0:
            return float(self.real)
        return self.norm()

    def __complex__(self) -> complex:
        """
        Convert the complex number to a python complex number.

        Returns:
            complex: The complex number.
        """
        return complex(self.real, self.img)


def main() -> None:
    i: Compl = Compl(0, 1)
    print((1 + i) ** 2)
    print(f"{abs(i)=}")

    test: Compl = 1 + i
    test /= 1 + i
    print(test)

    print((1 - 3 * i) / (1 + 2 * i))


if __name__ == "__main__":
    main()
