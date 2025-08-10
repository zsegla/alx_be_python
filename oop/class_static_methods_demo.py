class Calculator:
    """
    A class that demonstrates the use of static and class methods.
    """
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        A static method to add two numbers.
        
        This method doesn't access any class or instance state.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        A class method to multiply two numbers.
        
        This method uses the 'cls' parameter to access a class attribute.
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b