"""
mathCustom: A custom math module for working with complex numbers and vectors.

This module provides classes for handling:
- `Compl`: For complex numbers, supporting basic arithmetic, trigonometric
  representations, and utility methods.
- `Vec`: For working with mathematical vectors of arbitrary dimensions, supporting
  addition, subtraction, dot product, and more.

Example usage:
    from mathCustom import Compl, Vec

    c = Compl(3, 4)
    v = Vec(1, 2, 3)
"""

from .complexe import Compl
from .vector import Vec

__all__ = ["Compl", "Vec"]
