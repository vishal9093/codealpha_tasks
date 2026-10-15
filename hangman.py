import random

words = ["python", "computer", "network", "security", "database"]

word = random.choice(words)

guessed = []
wrong = 0
limit = 6

print("----- HANGMAN GAME -----")
print("Guess the word one letter at a time")
print("You have 6 wrong chances")

while wrong < limit:

    result = ""

    for ch in word:
        if ch in guessed:
            result = result + ch
        else:
            result = result + "_"

    print("\nWord:", result)
    print("Wrong guesses:", wrong)

    if result == word:
        print("You won!")
        print("The word was:", word)
        break

    letter = input("Enter a letter: ").lower()

    if len(letter) != 1:
        print("Please enter only one letter.")
        continue

    if not letter.isalpha():
        print("Please enter a valid letter.")
        continue

    if letter in guessed:
        print("You already tried this letter.")
        continue

    guessed.append(letter)

    if letter in word:
        print("Correct!")
    else:
        print("Wrong guess!")
        wrong = wrong + 1

else:
    print("\nGame Over!")
    print("The correct word was:", word)