"""
Exercise: FizzBuzz

Write a function `fizzbuzz(n)` that returns a list of strings for numbers
from 1 to n (inclusive), following these rules:
- If the number is divisible by 3, use "Fizz".
- If the number is divisible by 5, use "Buzz".
- If the number is divisible by both 3 and 5, use "FizzBuzz".
- Otherwise, use the number as a string.

Example:
    fizzbuzz(5) -> ["1", "2", "Fizz", "4", "Buzz"]
"""


def fizzbuzz(n):
    result = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result


if __name__ == "__main__":
    print(fizzbuzz(15))