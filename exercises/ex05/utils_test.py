"""This file is used to test the utils python file."""

__author__ = "730528622"


from utils import only_evens, sub, concat


def test_only_evens() -> None:
    assert only_evens([1,2,3,4,5,6,7,8]) == [2,4,6,8]
    assert only_evens([57,87,34,12,65,98,58,35,92]) == [34,12,98,58,92]
    assert only_evens([]) == []


def test_sub() -> None:
    assert sub([1,2,3,4,5], 2, 4) == [3,4]
    assert sub([23,54,76,58,23,85,34,96], 3, 5) == [58,23]
    assert sub([1,2,3,4,5], -4, 10) == [1,2,3,4,5]


def test_concat() -> None:
    assert concat([1,2,3,4,5], [6,7,8,9]) == [1,2,3,4,5,6,7,8,9]
    assert concat([8,5,2,6], [7,1,0,9]) == [8,5,2,6,7,1,0,9]
    assert concat([], []) == []
    



