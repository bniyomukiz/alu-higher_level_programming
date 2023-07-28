#!/usr/bin/python3

class BaseGeometry:
    """
    Base class for geometry operations.
    """

    def area(self):
        """
        Calculate the area of the geometry.
        Raises:
            Exception: This method should be implemented in the subclass.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate an integer value.

        Parameters:
            name (str): The name of the value.
            value: The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

# Sample test case
if __name__ == "__main__":
    try:
        bg = BaseGeometry()
        bg.area()
    except Exception as e:
        print(f"Exception: {e}")

    try:
        bg = BaseGeometry()
        bg.integer_validator("width", 10)
        bg.integer_validator("height", "hello")
    except Exception as e:
        print(f"Exception: {e}")
