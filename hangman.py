import random

def hangman():
    words = ["python", "coding", "gamer", "happy", "learning"]
    word = random.choice(words)
    guessed_letters = []
    attempts = 6

    while attempts > 0:
        display_word = ""
        for letter in word:
            if letter in guessed_letters:
                display_word += letter
            else:
                display_word += "_"

        print("\nCurrent Word:", display_word)
        guess = input("Guess a letter: ").lower()

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed that letter. Try again.")
            elif guess in word:
                print("Good guess!")
                guessed_letters.append(guess)
            else:
                print("Incorrect guess!")
                attempts -= 1
                print("Attempts left:", attempts)
        else:
            print("Invalid input. Please enter a single letter.")

        if "_" not in display_word:
            print("Congratulations! You guessed the word:", word)
            break

    if attempts == 0:
        print("Sorry, you ran out of attempts. The word was:", word)

# Run the hangman game
hangman()
