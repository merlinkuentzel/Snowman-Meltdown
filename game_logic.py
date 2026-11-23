import random
import ascii_art

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]

def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    # Display the snowman stage for the current number of mistakes.
    print(ascii_art.STAGES[mistakes])
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
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0

    print("Welcome to Snowman Meltdown!")


    while True:
        display_game_state(mistakes, secret_word, guessed_letters)
        guess = input("Guess a letter: ").lower()
        print("You guessed:", guess)
        if guess in secret_word:
            if guess in guessed_letters:
                print("Letter already uncovered")
                continue
            else:
                guessed_letters.append(guess)
        else:
            mistakes += 1

        if len(guessed_letters) == len(secret_word):
            display_game_state(mistakes, secret_word, guessed_letters)
            print("Congratulations, you saved the snowman!")
            break
        if mistakes > 2:
            display_game_state(mistakes, secret_word, guessed_letters)
            print(f"Game Over! The word was: {secret_word}")
            break
