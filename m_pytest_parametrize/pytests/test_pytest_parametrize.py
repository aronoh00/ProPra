import pytest
import string


def smallest_letter_and_digit(input: str) -> tuple[str | None, int | None]:
    smallest_letter = None
    smallest_digit = None
    for char in input:
        if char in string.ascii_lowercase:
            if smallest_letter is None or char < smallest_letter:
                smallest_letter = char
        elif char in string.digits:
            if smallest_digit is None or int(char) < smallest_digit:
                smallest_digit = int(char)
    return smallest_letter, smallest_digit


@pytest.mark.parametrize("input, letter, digit", [
    ("", None, None),
    ("ljkfdsbkl", "b", None),
    ("7787987321", None, 1),
    ("i5jk3cle9o", "c", 3),
    ("LKJLKDK", None, None),
    ("9", None, 9),
    ("a1!b2@c3#", "a", 1),
    ("@!$%^&*", None, None)
])
def test_smallest_letter_and_digit(input, letter, digit):
    assert smallest_letter_and_digit(input) == (letter, digit)
