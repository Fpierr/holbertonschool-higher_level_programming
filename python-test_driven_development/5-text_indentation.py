#!/usr/bin/python3
"""print a text with 2 new lines after each of these characters: ., ? and :"""


def text_indentation(text):
    """Prints a text with 2 new lines after each ., ? and : characters.

    Args:
        text (str): Input text.

    Raises:
        TypeError: If text is not a string.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for char in ['.', '?', ':']:
        text = text.replace(char, f'{char}\n\n')

    print(text, end="")
