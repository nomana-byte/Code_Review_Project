
"""
Refactored script for processing numbers and strings.

This module demonstrates descriptive naming, documentation,
and Pythonic list comprehensions.
"""


def process_numbers(numbers):
    """Process numbers by doubling even values and tripling odd values.

    Args:
        numbers: A list of integers to process.

    Returns:
        A list containing the processed numbers.
    """
    return [
        number * 2 if number % 2 == 0 else number * 3
        for number in numbers
    ]


def process_strings(strings):
    """Change string capitalization based on string length.

    Strings longer than five characters become uppercase.
    Other strings become lowercase.

    Args:
        strings: A list of strings to process.

    Returns:
        A single string containing the processed words,
        separated by spaces.
    """
    return " ".join(
        string.upper() if len(string) > 5 else string.lower()
        for string in strings
    )


def main():
    """Run the number and string processing examples.

    Returns:
        None.
    """
    numbers = [1, 2, 3, 4, 5, 6, 7]
    strings = ["apple", "banana", "kiwi", "grapefruit", "cherry"]

    processed_numbers = process_numbers(numbers)
    processed_strings = process_strings(strings)

    print("Processed Numbers:", processed_numbers)
    print("Processed Strings:", processed_strings)


if __name__ == "__main__":
    main()
