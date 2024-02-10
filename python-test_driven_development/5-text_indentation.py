#!/usr/bin/python3
"""Function that prints a text with 2 new lines after each of these characters: ., ? and :"""


def text_indentation(text):
    """Prints a text with 2 new lines after each ., ? and : characters.

    Args:
        text (str): Input text.

    Raises:
        TypeError: If text is not a string.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    text = text.replace('.', '.\n\n')
    text = text.replace('?', '?\n\n')
    text = text.replace(':', ':\n\n')

    print(text, end="")