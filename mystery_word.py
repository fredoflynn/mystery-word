import random
import re


def read_in_words():
    """Read in words from a file."""
    with open("/usr/share/dict/words") as words:
        words_full = words.read().upper().split('\n')
    return words_full


def choose_difficulty():
    """Prompts user to input difficulty and returns a string"""
    while True:
        user_choice = input("Choose your level [E]asy, [N]ormal, or [H]ard > ").lower()
        if user_choice == "e" or user_choice == "easy":
            return "easy"
        elif user_choice == "n" or user_choice == "normal":
            return "normal"
        elif user_choice == "h" or user_choice == "hard":
            return "hard"
        else:
            print("Please try again")


def easy_words(list_of_words):
    """Return a list of words <= 6 characters long
       Argument: List of words
    """
    easy_word_list = []
    for word in list_of_words:
        if len(word) <= 6:
            easy_word_list.append(word)
    return easy_word_list


def medium_words(list_of_words):
    """Return a list of words 6-8 characters long
       Argument: List of words
    """
    medium_word_list = []
    for word in list_of_words:
        if 6 <= len(word) <= 8:
            medium_word_list.append(word)
    return medium_word_list


def hard_words(list_of_words):
    """Return a list of words >= 8 characters long
       Argument: List of words
    """
    hard_word_list = []
    for word in list_of_words:
        if len(word) >= 8:
            hard_word_list.append(word)
    return hard_word_list


def random_word(list_of_words):
    """Return a random word from a list of words"""
    return random.choice(list_of_words)


def guess():
    """Return a single character A-Z only, uppercased"""
    while True:
        user_guess = input("Please guess a letter > ")
        user_guess = re.sub('[^A-Za-z]', '', user_guess).upper()
        if len(user_guess) == 1:
            return user_guess
        else:
            print("Please enter only a single letter A - Z")
            continue


def display_word(word, letter_list):
    """Display only letters of a word that are in a list of letters: e.g. H _ L L _
       Arguments:
       word -- e.g. HELLO
       list of letters -- e.g. ['H', 'L', 'J']
    """
    display_list = []
    for letter in word:
        if letter in letter_list:
            display_list.append(letter.upper())
        else:
            display_list.append("_")
    display = (" ".join(display_list))
    return display


def is_word_complete(word, letter_list):
    """Check to see if all letters in a word are in a list of letters"""
    for letter in word:
        if letter in letter_list:
            continue
        else:
            return False
    return True


def game_time():
    """Run a Hangman Game. Requires guess(), display_word(), is_word_complete()"""

    word_list = read_in_words()

    difficulty = choose_difficulty()

    if difficulty == "easy":
        game_word = random_word(easy_words(word_list))
    elif difficulty == "normal":
        game_word = random_word(medium_words(word_list))
    else:
        game_word = random_word(hard_words(word_list))

        print("The word contains {} letters".format(len(game_word)))
    max_guesses = 8
    guess_list = []
    guesses_used = 0

    while guesses_used < max_guesses:
        current_guess = guess()
        if current_guess in guess_list:
            print("You already guessed that!")
            continue
        guess_list.append(current_guess)
        if is_word_complete(game_word, guess_list):
            print("Congrats! You got it!")
            print(game_word)
            break
        if current_guess in game_word:
            print("You guessed a letter! You have {} guesses left".format(max_guesses - guesses_used))
            print(display_word(game_word, guess_list))
        else:
            guesses_used += 1
            print("No! That letter is not in the word. You have {} guesses left".format(max_guesses - guesses_used))
            print(display_word(game_word, guess_list))
        if max_guesses - guesses_used == 0:
            print("Sorry you lose. The word is {}.".format(game_word))


def play_again():
    """Prompt user to play again or not and returns True or False"""
    while True:
        play_more = input("Would you like to play again? [Y]es or [N]o > ").lower()
        if play_more == "y" or play_more == "yes":
            return True
        elif play_more == "n" or play_more == "no":
            return False
        else:
            print("Please enter [Y]es or [N]o")


if __name__ == '__main__':

    play = True

    while play:
        game_time()
        play = play_again()

    print("Thanks for playing")
