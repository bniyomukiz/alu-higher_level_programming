#!/usr/bin/python3

class MyClass:
    """This is a sample class."""

    def __init__(self, name):
        """
        Initialize a MyClass object.

        Parameters:
            name (str): The name of the object.
        """
        self.name = name

    def greet(self):
        """
        Print a greeting message.

        Returns:
            str: A greeting message.
        """
        return f"Hello, {self.name}!"

def add_attribute(obj, name, value):
    """
    Add a new attribute to an object if possible.

    Parameters:
        obj: The object to which the attribute will be added.
        name (str): The name of the attribute.
        value: The value of the attribute.

    Raises:
        TypeError: If the object cannot have a new attribute.
    """
    if hasattr(obj, name):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")

# Sample test cases
if __name__ == "__main__":
    mc = MyClass("John")
    print(mc.greet())

    try:
        a = "My String"
        add_attribute(a, "name", "Bob")
        print(a.name)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
