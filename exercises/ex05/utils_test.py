"""This file is used to test the utils python file."""

__author__ = "730528622"


from utils import only_evens, sub, concat

def test_only_evens() -> None:
    listing = [1,2,3,4,5,6,7,8]
    assert only_evens(listing) == [2,4,6,8]

