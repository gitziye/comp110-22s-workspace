""""This python file is mean to finish my COMP 110 exercise 06 homeowrk by test function."""

__author__ = "730528622"


from dictionary import invert, favorite_color, count


def test_invert() -> None:
    """This function is used to test the first function in dictionary."""
    assert invert({'unc': 'good', 'duke': 'bad'}) == {'good': 'unc', 'bad': 'duke'}
    assert invert({'a': 'c'}) == {'c': 'a'}
    assert invert({}) == {}


def test_favorite_color() -> None:
    """This function is used to test the second function in dictionary."""
    assert favorite_color({"Marc": "yellow", "Ezri": "blue", "Kris": "blue", "Kriss": "blue"}) == "blue"
    assert favorite_color({'a': 'c', 'b': 'c'}) == "c"
    assert favorite_color({}) == ""

def test_count() -> None:
    """This function is used to test the third function in dictionary."""
    assert count(["blue", "blue", "blue", "yellow"]) == {'yellow': 1, 'blue': 3}
    assert count(["a", "b", "a", "e", "e", "a"]) == {'a': 3, 'b': 1, 'e': 2}
    assert count([]) == {}




