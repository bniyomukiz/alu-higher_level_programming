#!/usr/bin/python3


def add_attribute(obj, attr, value):
  """Adds a new attribute to an object if it's possible.
  Args:
    obj: The object to which the attribute will be added.
    attr: The name of the attribute to be added.
    value: The value of the attribute to be added.
  Raises:
    TypeError: If the object cannot have new attributes.
  """


  # Check if the object can have new attributes.
  if not hasattr(obj, "__setattr__"):
    raise TypeError("can't add new attribute")
  # Add the new attribute to the object.
  setattr(obj, attr, value)
