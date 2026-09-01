"""
Exercise 1 (Easy): Palindrome Checker
--------------------------------------
Problem Statement:
Write a function `is_palindrome(s)` that returns True if the given string `s`
is a palindrome (reads the same forwards and backwards), ignoring case and
non-alphanumeric characters.

Example:
    is_palindrome("A man, a plan, a canal: Panama") -> True
    is_palindrome("race a car") -> False
"""


def is_palindrome(s: str) -> bool:
    """Return True if s is a palindrome ignoring case and non-alphanumerics."""
    # Keep only alphanumeric characters and lowercase them
    cleaned = "".join(ch.lower() for ch in s if ch.isalnum())
    return cleaned == cleaned[::-1]


if __name__ == "__main__":
    # Test cases
    tests = [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        ("", True),
        ("No 'x' in Nixon", True),
    ]
    for inp, expected in tests:
        result = is_palindrome(inp)
        assert result == expected, f"Failed: {inp!r} -> {result}, expected {expected}"
        print(f"is_palindrome({inp!r}) = {result}  (expected {expected})")
    print("All tests passed!")