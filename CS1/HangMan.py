import random


def display_hint():
    print (hint_word)


def display_build_word(built_word):
    print(built_word)


def get_user_guess(guess):
    guess = input('enter your guess: ')
    reduce_number_of_guess()

    # fuction that return true if guess char is 1 char only
def is_guessed_char(guess):
    yes = False
    index = len(guess)
    if index == 1:
        yes = True
    return yes


def check_if_guessed_character_exist(secret_word, user_guess):
    found = False
    for check in secret_word:
        if check == user_guess:
            found = True
    return found


def reduce_number_of_guess(number_of_guessing_left):
    number_of_guessing_left -= 1


def print_result_so_far(built_word):
    print (built_word)


def init_built_word(secret_word, built_word):
    index = len(secret_word)
    count = 0
    while (count < index):
        build_word.append("_")


def replace_chararacter(index, char):
    build_word[index] = char


def compare_guessed_char_and_secrect_word_char(guessed_char, secret_word):
    match = False
    count = -1
    for char in secret_word:
        index = index + 1
        if char == guessed_char:
            replace_chararacter(index, char)
            match = True

    return match


def random_word():
    file = "/Users/yveslym/Desktop/portfolio/CS1/Hangman_Project/hangman_words.txt"
    openfile = open(file).read().split()
    index = random.randint(0, len(openfile) - 1)
    return (openfile[index])


if __name__ == "__main__":
    secret_word = ""
    user_guess = ""
    hint_word = ""
    build_word = ""
    guessed_character = ""
    number_of_character_in_secret_word = 0
    number_of_guessing_left = 0

    name = "yves"
    for index in name:
        print (index)