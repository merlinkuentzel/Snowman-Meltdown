import random
import ascii_art
import time

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]

def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    # Display the snowman stage for the current number of mistakes.
    if mistakes == 0:
        print(ascii_art.STAGES[0])
    else:
        for stage in ascii_art.STAGES[(mistakes - 1) * 3 + 1: mistakes * 3 + 1]:
            print(stage)
            time.sleep(0.5)
    # Build a display version of the secret word.
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word: ", display_word)
    print("\n")


def play_game():
    print("Welcome to Snowman Meltdown!")

    game_run = True
    while game_run:
        secret_word = get_random_word()
        word_check = set(secret_word)
        guessed_letters = []
        mistakes = 0

        while True:
            display_game_state(mistakes, secret_word, guessed_letters)
            guess = input("Guess a letter: ").lower()
            print("You guessed:", guess)
            if len(guess) > 1 or not guess.isalpha():
                print("Please enter one letter")
            else:
                if guess in secret_word:
                    if guess in guessed_letters:
                        print("Letter already uncovered")
                        continue
                    else:
                        guessed_letters.append(guess)
                else:
                    mistakes += 1

                if word_check.issubset(guessed_letters):
                    display_game_state(mistakes, secret_word, guessed_letters)
                    print("Congratulations, you saved the snowman!")
                    break
                if mistakes > 2:
                    display_game_state(mistakes, secret_word, guessed_letters)
                    print(f"Game Over! The word was: {secret_word}")
                    break

        while True:
            play_again = input("Do you want to play again? (yes/no): ").lower()
            if play_again == "yes":
                break
            elif play_again == "no":
                print("Bye")
                print()
                game_run = False
                break