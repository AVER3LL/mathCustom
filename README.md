# Math Module

This module provides two classes for mathematical operations: `Compl` for complex numbers and `Vec` for vectors.

## Compl Class

The `Compl` class represents complex numbers and supports various operations.

I recommend creating `i = Compl(0, 1)` to represent the imaginary unit.
This will allow you to write complex numbers more naturally in your code.

### Features:

- Basic arithmetic operations: addition, subtraction, multiplication, division
- Trigonometric representation
- Conjugate and reciprocal calculations
- Exponentiation
- Conversion to and from Python's built-in complex type

### Usage:

```python
from customMath import Compl

# Create complex numbers
c1 = Compl(3, 4)  # 3 + 4i
c2 = Compl(1, 1)  # 1 + i
i = Compl(0, 1)
c3 = Compl(2 + 3j) # Default python representation

test = 2 + (3 * i)
print(test) # (2 + 3i)

print(test == c3)  # True

# Perform operations
result = c1 + c2
print(result)  # (4 + 5i)

# Calculate norm
norm = c1.norm()
print(norm)  # 5.0

# Get trigonometric representation
r, theta = c1.trig()
print(f"r: {r}, theta: {theta}")
```

## Vec Class

The `Vec` class represents mathematical vectors with arbitrary dimensions.

### Features:

- Vector operations: addition, subtraction, dot product
- Scalar operations: multiplication, division
- Normalization
- Equality comparison

### Usage:

```python
from customMath import Vec

# Create vectors
v1 = Vec(1, 2, 3)
v2 = Vec(4, 5, 6)

# Perform operations
result = v1 + v2
print(result)  # (5, 7, 9)

# Calculate dot product
dot_product = v1 * v2
print(dot_product)  # 32

# Calculate norm
norm = v1.norm()
print(norm)  # 3.7416573867739413
```

## Installation

To use this package, simply clone the repository and run `cd customMath && pip install .` .

(Not sure about that yet, just clone the repo and import it normally)

## Dependencies

This module has no external dependencies and works with Python 3.6+.

## Contributing

Contributions to improve the module are welcome. Please ensure that you add or update tests as necessary.
