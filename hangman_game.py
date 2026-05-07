import random

# List of words with hints
word_hint = {
    "python": "A popular programming language used in AI and web development.",
    "java": "Programming language commonly used for Android development.",
    "angular": "A frontend framework developed by Google.",
    "spring": "A powerful Java framework for backend development.",
    "coding": "The process of writing computer programs.",
    "tree": "A tall plant found in nature."
}

# Select random word
word = random.choice(list(word_hint.keys()))
hint = word_hint[word]

guessed_letters = []
attempts = 6

print(" Welcome to Hangman Game!")
print("Hint:", hint)

while attempts > 0:

    display_word = ""

    # Display guessed letters and underscores
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Attempts left:", attempts)

    # User input
    guess = input("Guess a letter: ").lower()

    # Validation
    if len(guess) != 1 or not guess.isalpha():
        print(" Please enter a single alphabet letter.")
        continue

    # Already guessed check
    if guess in guessed_letters:
        print(" You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    # Wrong guess
    if guess not in word:
        attempts -= 1
        print(" Wrong guess!")

    # Win condition
    if all(letter in guessed_letters for letter in word):
        print("\n Congratulations! You guessed the word:", word)
        break

# Lose condition
if attempts == 0:
    print("\n You lost! The word was:", word)