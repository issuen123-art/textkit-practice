from textkit import to_snake_case, to_title_case, is_palindrome


def test_to_snake_case():
    assert to_snake_case("Hello World") == "hello_world"


def test_to_snake_case_collapses_extra_whitespace():
    assert to_snake_case("  Hello   World  ") == "hello_world"


def test_to_snake_case_single_word():
    assert to_snake_case("Python") == "python"


def test_to_snake_case_empty_string():
    assert to_snake_case("") == ""


def test_to_title_case():
    assert to_title_case("hello world") == "Hello World"


def test_to_title_case_collapses_extra_whitespace():
    assert to_title_case("  hello   world  ") == "Hello World"


def test_to_title_case_lowercases_rest_of_word():
    assert to_title_case("PYTHON ROCKS") == "Python Rocks"


def test_to_title_case_empty_string():
    assert to_title_case("") == ""


def test_is_palindrome():
    assert is_palindrome("racecar") is True
    assert is_palindrome("A man a plan a canal Panama") is True
    assert is_palindrome("hello") is False


def test_is_palindrome_empty_string():
    assert is_palindrome("") is True


def test_is_palindrome_single_character():
    assert is_palindrome("a") is True


def test_is_palindrome_mixed_case_without_punctuation():
    assert is_palindrome("Was it a car or a cat I saw") is True


def test_is_palindrome_does_not_strip_punctuation():
    # Punctuation is not removed, only whitespace, so a phrase that is a
    # palindrome once punctuation is stripped can still fail here.
    assert is_palindrome("A man, a plan, a canal: Panama") is False
