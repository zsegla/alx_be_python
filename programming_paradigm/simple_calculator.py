# simple_calculator.py

class SimpleCalculator:
    """A simple calculator class that supports basic arithmetic operations."""

    def test_addition(self, a, b):
        """Return the addition of a and b."""
        return a + b

    def test_subtracttion(self, a, b):
        """Return the subtraction of b from a."""
        return a - b

    def test_multiplication(self, a, b):
        """Return the multiplication of a and b."""
        return a * b

    def test_division(self, a, b):
        """Return the division of a by b. Returns None if b is zero."""
        if b == 0:
            return None
        return a / b