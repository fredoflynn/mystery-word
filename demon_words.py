import random
import re


def read_and_sort_words():
    """Read in words from a file. Returns a list of words sorted by len(word)"""
    with open("/usr/share/dict/words") as words:
        full_word_list = words.read().upper().split('\n')
        sorted_word_list = sorted(full_word_list, key=len)
    return sorted_word_list


def choose_word_length(list_of_words):
    """Prompts user to input word length
    Args -- Bigger List of words to be narrowed down
    Return -- List of words for user's desired length
    """
    min_len = len(list_of_words[0])
    max_len = len(list_of_words[-1])

    while True:
        try:
            user_choice = int(input("How many letters would you like your word to be? ({} - {} letters) > "
                                    .format(min_len, max_len)))
            if min_len <= user_choice <= max_len:
                break
            else:
                print("Please try again. Only {} - {} letters long".format(min_len, max_len))
                continue
        except:
            print("Please enter only a whole number between {} and {}".format(min_len, max_len))
            continue

    current_words = []
    for word in list_of_words:
        if len(word) != user_choice:
            continue
        else:
            current_words.append(word)

    return current_words


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


def is_word_complete(word):
    """If word contains a '-' it is not a complete word"""
    if '-' in word:
        return False
    else:
        return True


def create_word_families(list_of_words, cur_guess, guess_li):
    """Creates word families.
    Args -- List of words, current guess i.e. 's', and list of letters already guessed
    Return -- Dictionary of word families with family as the key, and list of words as the value
            e.g. list_of_words = ['SPOT', 'BANG', 'STAR'], cur_guess = 'S', guess_li = []
            return_dict = {'S---': ['SPOT', 'STAR'], '----': ['BANG']
    """
    word_families1 = {}
    for word in list_of_words:
        word_family = ""
        for letter in word:
            if letter == cur_guess or letter in guess_li:
                word_family += letter
            else:
                word_family += "-"

        # if word_family doesn't exist yet, Create it
        if word_family not in word_families1:
            word_families1[word_family] = []

        word_families1[word_family].append(word)
    return word_families1


def find_max_family(word_families_dict, cur_guess):
    """Finds word_family with the most remaining words
    Args -- dict of word families, current guess e.g. 's'
    Return -- String that represents word family which has the most remaining words...
            i.e. for list_of_words = ['SPOT', 'BANG', 'STAR'] there are 2 word families...
            S--- and ---- . S--- has 2 words 'SPOT' and 'STAR'. ---- has only 'BANG' so return S---
    """
    count = 0
    maximum_family = ""
    for family in word_families_dict:

        # if word_families are equal and one family doesn't contain the current guess, that family rules
        # if word_families are equal and both contain the current guess, the first one called rules
        if len(word_families_dict[family]) >= count and cur_guess not in family:
            count = len(word_families_dict[family])
            maximum_family = family
        elif len(word_families_dict[family]) > count:
            count = len(word_families_dict[family])
            maximum_family = family
        else:
            continue

    return maximum_family


def game_time():
    """Run an EVIL Hangman Game."""
    # read in entire word_list
    word_list = read_and_sort_words()

    # narrow word_list by chosen length of word
    current_word_list = choose_word_length(word_list)

    max_guesses = 10
    guess_list = []
    guesses_used = 0

    while guesses_used < max_guesses:
        current_guess = guess()
        if current_guess in guess_list:
            print("You already guessed that")
            continue
        guess_list.append(current_guess)

        # create word families
        word_families = create_word_families(current_word_list, current_guess, guess_list)

        # find most common family
        max_family = find_max_family(word_families, current_guess)

        # narrow current_word_list biggest family of words remaining
        current_word_list = word_families[max_family]

        # Did you win? I doubt it.
        if is_word_complete(max_family):
            print("Congrats! You got it!")
            print(max_family)
            break

        # prints remaining guesses, the biggest remaining word family, and tells how many words are left
        if current_guess in max_family:
            print("You got one! You have {} guesses remaining".format(max_guesses - guesses_used))
            print(max_family)
            print("There are {} words left".format(len(current_word_list)))
        else:
            guesses_used += 1
            print("You suck! It's not in the word. You have {} guesses remaining.".format(max_guesses - guesses_used))
            print(max_family)
            print("There are {} words left".format(len(current_word_list)))
        if max_guesses - guesses_used == 0:
            print("Sorry you lose. The word is {}.".format(random.choice(current_word_list)))


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
