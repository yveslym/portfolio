import random
import string

def display_hint():
    print (hint_word)

def get_user_guess():
    guess = raw_input('Character: ')
    return guess

    # fuction that return true if guess char is 1 char only
def is_guessed_char(guess):

    index = 1
    if index == len(guess):
        return True
    else:
        return False



def reduce_number_of_guess(number_of_guessing_left):
    number_of_guessing_left -= 1
    return number_of_guessing_left


def init_built_word(secret_word):
    index = len(secret_word)


    count = 1
    built_word = "_"
    while (count < index):
        built_word = built_word+"_"
        count +=1

    return built_word
def replace_chararacter(built_word, index, char):


    built_word = built_word[:index] + char + built_word[index + 1:]

    return built_word


def compare_guessed_char_and_secret_word_char(built_word,guessed_char, secret_word):
    match = False
    index = -1
    for char in secret_word:
        index = index + 1
        if char == guessed_char:
            built_word = replace_chararacter(built_word, index, char)
            match = True

    return [match, built_word]

def is_playing(secret_word,play):
    if secret_word is None:
        play = False
    else:
        play = True

    return play


def random_word():
    print("random word was picked")
    file = "/Users/yveslym/Desktop/portfolio/CS1/Hangman_Project/hangman_words.txt"
    openfile = open(file).read().split()
    index = random.randint(0, len(openfile) - 1)
    return (openfile[index])

# function to check if the user guess different character then what guessed already
def is_guessed_char_used(user_guess, guessed_char):

    for guess in guessed_char:
        if guess == user_guess:
            print (" character already guess, and either add or nit in in the secret word!!!")
            return True
    return False


if __name__ == "__main__":

    secret_word = None
    user_guess = ""
    hint_word = ""
    built_word = ""
    guessed_word = ""
    number_of_character_in_secret_word = 0
    number_of_guessing_left = 1
    play = True
    win = False
    isPlaying = False
    result = []
    while win == False and number_of_guessing_left > 0:
        if  secret_word != None:

            user_guess = get_user_guess()   #get user guessing char

            if is_guessed_char(user_guess) == True:

                if is_guessed_char_used(user_guess,guessed_word) == False:
                    guessed_word = guessed_word+user_guess
                    number_of_guessing_left = reduce_number_of_guess(number_of_guessing_left)  # reduce number of guessing
                    result = compare_guessed_char_and_secret_word_char(built_word,user_guess,secret_word) # true if char match, also return the new built word

                    if result[0] == True: # if guessed character match with one of the character

                        built_word = result[1]
                        print (built_word)
                        print("guessing left: ", number_of_guessing_left)

                        if secret_word == built_word:
                            win == True
                            print(" Nice Job You Won")
                    else:
                        print(" Wrong character try again")
                        print('number of guessing left: ', number_of_guessing_left)



            else:
                print("enter a chatacter")
                print(is_guessed_char(user_guess))


        else:
            print("init secret word")
            secret_word = random_word()
            number_of_guessing_left = len(secret_word)
            built_word = init_built_word(secret_word)
            print( secret_word)
            play = True
    print("game over")

