from textkit import to_snake_case, to_title_case


def test_to_snake_case():
    assert to_snake_case("Hello World") == "hello_world"


def test_to_title_case():
    assert to_title_case("hello world") == "Hello World"
