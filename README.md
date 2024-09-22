# mathCustom Module

This module provides two classes for mathematical operations: `Compl` for complex numbers and `Vec` for vectors.

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Module Structure](#module-structure)
- [Compl Class](#compl-class)
  - [Features:](#features)
  - [Usage:](#usage)
- [Vec Class](#vec-class)
  - [Features:](#features-1)
  - [Usage:](#usage-1)
- [Dependencies](#dependencies)
- [Installation](#installation)
- [Running Tests](#running-tests)
- [Contributing](#contributing)
- [License](#license)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Module Structure

The module contains two main classes:

- `Compl`: Located in `src/mathCustom/complexe.py`
- `Vec`: Located in `src/mathCustom/vector.py`

You can import these classes directly from the `mathCustom` module.

## Compl Class

The `Compl` class represents complex numbers and supports various operations.

### Features:

- Basic arithmetic operations: addition, subtraction, multiplication, division
- Trigonometric representation
- Conjugate and reciprocal calculations
- Exponentiation
- Conversion to and from Python's built-in complex type

### Usage:

```python
from mathCustom import Compl

# Create complex numbers
c1 = Compl(3, 4)  # 3 + 4i
c2 = Compl(1, 1)  # 1 + i
i = Compl(0, 1)   # Representing the imaginary unit
c3 = Compl(2 + 3j)  # From Python's built-in complex type

# Operations
result = c1 + c2
result2 = 1 + (3 * i)
print(result)  # (4 + 5i)
print(result2) # (1 + 3i)

# Norm calculation
norm = c1.norm()
print(norm)  # 5.0

# Trigonometric representation
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
from mathCustom import Vec

# Create vectors
v1 = Vec(1, 2, 3)
v2 = Vec(4, 5, 6)

# Vector addition
result = v1 + v2
print(result)  # (5, 7, 9)

# Dot product
dot_product = v1 * v2
print(dot_product)  # 32

# Norm calculation
norm = v1.norm()
print(norm)  # 3.7416573867739413
```

## Dependencies

This module has no external dependencies and works with Python 3.6+.

## Installation

To use this module, follow these steps:

1. Clone the repository:

   ```
   git clone https://github.com/AVER3LL/mathCustom.git
   cd mathCustom
   ```

2. Install the module in editable mode:

   _Make sure you are in the root directory before running this._

   ```
   pip install -e .
   ```

## Running Tests

To run the tests for this module:

1. Ensure you are in the root directory of the project.
2. Run the following command:

   ```
   python -m unittest discover tests
   ```

This command will automatically discover and run all test files in the `tests` directory.

To run a specific test file:

```
python -m unittest tests.test_file_name
```

Replace `test_file_name` with the name of the test file you want to run (without the `.py` extension).

## Contributing

Contributions to improve the module are welcome. Please ensure that you:

1. Add or update tests as necessary.
2. Run the full test suite before submitting changes.
3. Follow the existing code style (I currently use ruff as my formatter with line length 79)

When submitting changes, make sure all tests pass by running the test suite as described above.

## License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.
