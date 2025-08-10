import math

class Shape:
    """
    A base class for shapes.
    
    This class defines an 'area' method that must be overridden by subclasses.
    """
    def area(self):
        """
        Calculates the area of the shape.
        
        Raises a NotImplementedError to ensure subclasses provide their own implementation.
        """
        raise NotImplementedError("Subclass must implement abstract method")

class Rectangle(Shape):
    """
    A class representing a rectangle, inheriting from Shape.
    """
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        """
        Calculates the area of the rectangle.
        """
        return self.length * self.width

class Circle(Shape):
    """
    A class representing a circle, inheriting from Shape.
    """
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """
        Calculates the area of the circle.
        """
        return math.pi * self.radius ** 2