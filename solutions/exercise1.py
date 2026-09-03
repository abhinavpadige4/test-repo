# Exercise: Python Basics - Variables and Types
# Complete the functions below.

def greet(name):
    """Return a greeting string for the given name."""
    return f"Hello, {name}!"


def add_numbers(a, b):
    """Return the sum of two numbers."""
    return a + b


def describe_value(value):
    """Return a string describing the type of the value."""
    return f"The value is of type {type(value).__name__}"


def is_even(number):
    """Return True if the number is even, otherwise False."""
    return number % 2 == 0


if __name__ == "__main__":
    print(greet("World"))
    print(add_numbers(3, 5))
    print(describe_value(42))
    print(is_even(10))