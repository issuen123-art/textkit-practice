"""Tiny collection of string helper functions."""


def to_snake_case(text):
    """Convert a string like 'Hello World' to 'hello_world'."""
    return "_".join(text.strip().split()).lower()


def to_title_case(text):
    """Convert a string like 'hello world' to 'Hello World'."""
    return " ".join(word.capitalize() for word in text.strip().split())


def is_palindrome(text):
    """Return True if text reads the same forwards and backwards, ignoring case and spaces."""
    cleaned = "".join(text.lower().split())
    return cleaned == cleaned[::-1]
