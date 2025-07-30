# simple_calculator.py

class SimpleCalculator:
    """A simple calculator class that supports basic arithmetic operations."""

    def addition(self, a, b):
        """Return the addition of a and b."""
        return a + b

    def subtracttion(self, a, b):
        """Return the subtraction of b from a."""
        return a - b

    def multiplication(self, a, b):
        """Return the multiplication of a and b."""
        return a * b

    def division(self, a, b):
        """Return the division of a by b. Returns None if b is zero."""
        if b == 0:
            return None
        return a / b