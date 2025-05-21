#Use parameterization to test count_word_matches with multiple input combinations of text and target,
# along with their expected outputs. Write a parameterized test to validate the function across basic,
# mixed-case, and simple edge-case scenarios.

import pytest
from count_word_matches import count_word_matches

@pytest.mark.parametrize(
    "text, target, expected",
    [
        ("The cat sat on the mat", "cat", 1),
        ("Dog dog DOG dOg", "dog", 4),
        ("Hello world", "world", 1),
        ("hello hello HELLO", "hello", 3),
        ("No matches here", "yes", 0),
        ("catcat cat catdog", "cat", 1),
        ("a a a", "a", 3),
    ]
)
def test_count_word_matches(text, target, expected):
    assert count_word_matches(text, target) == expected

# Edge Case Testing : Create a fixture that provides common edge-case inputs,and test the `count_word_matches` function
# using parameterized tests. Focus on empty inputs, spaces, and punctuation.
@pytest.fixture(scope='function')
def sample_edge_cases():
    return [
        ("", "word", 0),                # Empty text
        ("hello world", "", 0),         # Empty target
        ("", "", 0),                    # Both empty
        ("hello  world", "world", 1),   # Multiple spaces
        (" cat ", "cat", 1),            # Leading/trailing spaces
        ("cat,dog cat", "cat", 2),      # Punctuation not handled, comma is part of "cat,"
        ("x y z", "x", 1),              # Single character
    ]

# Parameterized test using the fixture values
@pytest.mark.parametrize("text, target, expected", [
    ("", "word", 0),
    ("hello world", "", 0),
    ("", "", 0),
    ("hello  world", "world", 1),
    (" cat ", "cat", 1),
    ("cat,dog cat", "cat", 1),
    ("x y z", "x", 1),
])
def test_count_word_matches(text, target, expected):
    assert count_word_matches(text, target) == expected

#Test the function for invalid inputs like None, integers, or lists to ensure it raises the appropriate exceptions.
# Use a fixture to prepare test cases for invalid input.
# Fixture to provide each invalid case individually
@pytest.fixture(params=[
    (None, "word"),  # None as text
    ("hello world", None),  # None as target
    (123, "word"),  # Integer as text
    ("hello world", 456),  # Integer as target
    (["hello", "world"], "world"),  # List as text
    ("hello world", ["world"])  # List as target
])
def invalid_input_case(request):
    return request.param


# Test function to check for TypeError
def test_count_word_matches_invalid_input(invalid_input_case):
    text, target = invalid_input_case
    with pytest.raises(TypeError, match="Both 'text' and 'target' must be strings."):
         count_word_matches(text, target)
