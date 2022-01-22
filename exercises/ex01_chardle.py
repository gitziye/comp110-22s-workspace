"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730528622"

word = input("Enter a 5-character word: ")
if len(word) != 5:
    print("Error: Word must contain 5 characters")
    exit()
char = input("Enter a single character: ")
if len(char) != 1:
    print("Error: Character must be a single character.")
    exit()
print("Searching for " + char + " in " + word)

num = 0

if word[0] == char:
    print(char + " found at index 0")
    num = num + 1

if word[1] == char:
    print(char + " found at index 1")
    num = num + 1

if word[2] == char:
    print(char + " found at index 2")
    num = num + 1

if word[3] == char:
    print(char + " found at index 3")
    num = num + 1

if word[4] == char:
    print(char + " found at index 4")
    num = num + 1

if num == 0:
    print("No instances of " + char + " found in " + word)
else:
    if num == 1:
        print("1 instance of " + char + " found in " + word)
    else:
        print(str(num) + " instances of " + char + " found in " + word)




