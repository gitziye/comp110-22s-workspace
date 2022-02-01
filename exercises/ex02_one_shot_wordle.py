"""ex02_one_shot_wordle.py""" 

__author__ = "730528622"

secret = "python"

inp = input(f"What is your {len(secret)}-letter guess? ")

while len(inp) != len(secret):
    inp = input(f"That was not {len(secret)} letters! Try again: ")

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

i = 0
emoji = ""
while i < len(secret):
    if inp[i] == secret[i]:
        emoji = emoji + GREEN_BOX
        
    else: 
        # if not consistent, here to determine whether this is yellow or white
        j = 0
        times = 0
        while j < len(secret):
            if inp[i] == secret[j]:
                times += 1     
            j += 1
        if times == 0:
            emoji = emoji + WHITE_BOX
        else:
            emoji = emoji + YELLOW_BOX
    i += 1

print(emoji)

if inp == secret:
    print(f"Woo! You got it!")
else:
    print(f"Not quite. Play again soon!")
