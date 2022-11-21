import random

MAX_TRIES = 4
WORD_LIST = ["test", "word", "sky"]
HANGMAN_STAGE_GRAPHICS = [
    "\n +---+\n  |   |\n      |\n      |\n      |\n      |\n=========''', '''",
    "\n+---+\n |   |\n  O   |\n  |   |\n      |\n      |\n=========''', '''",
    "\n=========''', '''\n  +---+\n  |   |\n  O   |\n /|\  |\n      |\n      |\n=========''', '''",
    "\n  +---+\n  |   |\n  O   |\n /|\  |\n / \  |\n      |\n=========''']"
]
WIN_MESSAGE = "You win! :D WOOP!"
LOSE_MESSAGE = "You lose D:"


def main():
    random_word = random.choice(WORD_LIST)
    tries = 0
    guessed_letters = ["_"] * len(random_word)

    print("".join(guessed_letters))

    while True:
        guessed_letter_or_word = input("Guess a letter or the whole word:")

        if guessed_letter_or_word == random_word:
            print(WIN_MESSAGE)
            break

        if guessed_letter_or_word in random_word:
            indices = find_all(random_word, guessed_letter_or_word)

            for index in indices:
                guessed_letters[index] = guessed_letter_or_word

            print("".join(guessed_letters))

            if "".join(guessed_letters) == random_word:
                print(WIN_MESSAGE)
                break

            continue

        print(HANGMAN_STAGE_GRAPHICS[tries])

        tries += 1
        if tries == MAX_TRIES:
            print(LOSE_MESSAGE)
            break


def find_all(str: str, value: str) -> list[int]:
    indices = []
    current_index = 0

    while True:
        current_index = str.find(value, current_index)

        if current_index == -1:
            break

        indices.append(current_index)
        current_index += 1

    return indices


if __name__ == "__main__":
    main()
