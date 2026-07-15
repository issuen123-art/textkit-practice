from textkit import to_snake_case, to_title_case, is_palindrome


def test_to_snake_case():
    assert to_snake_case("Hello World") == "hello_world"


def test_to_title_case():
    assert to_title_case("hello world") == "Hello World"


def test_is_palindrome():
    assert is_palindrome("racecar") is True
    assert is_palindrome("A man a plan a canal Panama") is True
    assert is_palindrome("hello") is False
