#Hangman Game
import random

# Words list
words = ["python", "computer", "programming", "django", "database"]

# Random word select
word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Total chances
attempts = 6

print("===== HANGMAN GAME =====")
print("Guess the word!")

while attempts > 0:

    # Display hidden word
    display = ""

    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)
    print("Attempts left:", attempts)

    # Check win
    if "_" not in display:
        print("🎉 Congratulations! You Win!")
        break

    # Take input
    guess = input("Enter a letter: ").lower()

    # Check input
    if len(guess) != 1:
        print("Please enter only one letter.")
        continue

    if not guess.isalpha():
        print("Please enter an alphabet.")
        continue

    if guess in guessed_letters:
        print("You already guessed this letter.")
        continue

    # Add guessed letter
    guessed_letters.append(guess)

    # Check guess
    if guess in word:
        print("✅ Correct guess!")
    else:
        print("❌ Wrong guess!")
        attempts -= 1

else:
    print("\n💀 Game Over!")
    print("The correct word was:", word)