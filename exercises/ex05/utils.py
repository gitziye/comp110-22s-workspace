"""This file is to implement three list related functions."""

__author___ = "730528622"


def only_evens(listing: list[int]) -> list[int]:
    """Output only the even items from the original list."""
    listing2: list[int] = list()
    for i in listing:
        if i % 2 == 0:
            listing2.append(i)
    return listing2


def sub(listing: list[int], a: int, b: int) -> list[int]:
    """Output the sublist from the original list."""
    listing2: list[int] = list()
    if a < 0:
        a = 0
    if b > len(listing) - 1:
        b = len(listing)
    
    while a < b:
        listing2.append(listing[a])
        a += 1
    return listing2


def concat(listing1: list[int], listing2: list[int]) -> list[int]:
    """Output is the combined two lists."""
    listing3: list[int] = listing1
    for i in listing2:
        listing3.append(i)
    return listing3
