""""This python file is mean to finish my COMP 110 exercise 06 homeowrk."""

__author__ = "730528622"

def invert(dict1: dict[str, str]) -> dict[str, str]:
    dict2: dict[str, str]
    dict2 = dict()
    for i in dict1:
        dict2[dict1[i]] = i
    return dict2

  
def favorite_color(dict1: dict[str, str]) -> str:
    list1: list[str] = list()
    dict2: dict[str, int] = dict()
    max_color: str = ""
    number: int = 0
    for key in dict1:
        list1.append(dict1[key])
    for i in list1:
        if i in dict2:
            dict2[i] += 1
        else:
            dict2[i] = 1
    
    for i in dict2:
        if dict2[i] > number:
            max_color = i
            number = dict2[i]
        
    print(dict2)
    return max_color


def count(list1: list[str]) -> dict[str, int]:
    dict1: dict[str, int] = dict()
    for i in list1:
        if i in dict1:
            dict1[i] += 1
        else:
            dict1[i] = 1
    return dict1



