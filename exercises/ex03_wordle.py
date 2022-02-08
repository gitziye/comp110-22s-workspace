"""exercise 3 structured wordle"""

__author__ = "730528622"

import code


def contains_char(a: str, b: str) -> bool:
    "check if the first argument contains the second argument"
    assert len(b) == 1
    i = 0
    count = 0
    while i < len(a):
        if a[i] == b:
            count += 1
        i += 1
    if count == 0:
        return False
    return True


def emojified(guess: str, secret: str) -> str:
    "compare two strings and output the emoji block"
    assert len(guess) == len(secret)

    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"

    i = 0
    emoji = ""

    while i < len(guess):
        if guess[i] == secret[i]:
            emoji += GREEN_BOX
        elif contains_char(secret, guess[i]):
            emoji += YELLOW_BOX
        else:
            emoji += WHITE_BOX
        i += 1
    return emoji


def input_guess(c: int) -> str:
    "enter the guess with correct length"
    gue = input(f"Enter a  {c}  character word: ")
    while len(gue) != c:
        gue = input(f"That wasn't {c} chars! Try again: ")
    return gue


def main() -> None:
    """The entrypoint of the program and main game loop."""
    code = "codes"
    i = 0
    while i < 6:
        print(f"=== Turn {i+1}/6 ===")
        inp = (input_guess(len(code)))
        print(emojified(inp, code))
        
        if inp == code: 
            print(f"You won in {i+1}/6 turns!")
            i = 7
        else:
            i += 1
    if i == 6:
         print(f"{i}/6 - Sorry, try again tomorrow!")
    return   

if __name__ == "__main__":
    main()