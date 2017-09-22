import random
import string

def display_hint():
    print (hint_word)

def get_user_guess():
    guess = raw_input('enter your guess: ')
    return guess

    # fuction that return true if guess char is 1 char only
def is_guessed_char(guess):
    yes = False
    index = len(guess)
    print ("index: ",index)
    if index == 0:
        yes = True
    return yes



def reduce_number_of_guess(number_of_guessing_left):
    number_of_guessing_left -= 1
    return number_of_guessing_left


def init_built_word(secret_word):
    index = len(secret_word)
    print ("secret word:", secret_word)

    count = 1
    built_word = "_"
    while (count < index):
        built_word = built_word+"_"
        count +=1
    print ("built word: ",built_word)

    return built_word
def replace_chararacter(buit_word, index, char):
    built_word[index] = char


def compare_guessed_char_and_secret_word_char(built_word,guessed_char, secret_word):
    match = False
    index = -1
    print ("secret word: ",secret_word)
    for char in secret_word:
        index = index + 1
        if char == guessed_char:
            replace_chararacter(built_word,index, char)
            print("the character ", char," is in position ", index)
            match = True

    return match

def is_playing(secret_word,play):
    if secret_word is None:
        play = False
    else:
        play = True
    print ("is playing: ",play)
    print ("secret word: ", secret_word)
    return play

def init_game(secret_word,buil_word):
    print("gane initialized")
    secret_word = random_word()
    init_built_word(secret_word,built_word,number_of_guessing_left)

def random_word():
    print("random word was picked")
    file = "/Users/yveslym/Desktop/portfolio/CS1/Hangman_Project/hangman_words.txt"
    openfile = open(file).read().split()
    index = random.randint(0, len(openfile) - 1)
    return (openfile[index])

def win(cond):
    return cond

# function to check if the user guess different character then what guessed already
def is_guessed_char_used(user_guess, guessed_char):

    for guess in guessed_char:
        if guess == user_guess:
            print (" character already guess, and either add or nit in in the secret word!!!")
            return True
    return False

def wining_condition(number_of_guessing_left,built_word,secret_word,win):

    if number_of_guessing_left == 0 and built_word != secret_word:
        print(" the game is over.. LOSER ")
    elif built_word == secret_word:
        win = True


#def play(number_of_guessing_left, built_word, secret_word, user_guess, win,play):


        #play(number_of_guessing_left, built_word, secret_word, user_guess, win)

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
    while win == False and number_of_guessing_left > 0:
        if  secret_word != None:

            user_guess = get_user_guess()   #get user guessing char

            if is_guessed_char(user_guess) == True:

                print("it's a char")

                if is_guessed_char_used(user_guess,guessed_word) == False:


                else:
                    print(" enter different Char ' ",user_guess," ' was already used")



            else:
                print("enter a chatacter")


        else:
            print("init secret word")
            secret_word = random_word()
            number_of_guessing_left = len(secret_word)
            built_word = init_built_word(secret_word)
            play = True
    print("game over")

