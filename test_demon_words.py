from mystery_word import *

words = ['ALLY', 'BETA', 'COOL', 'DEAL', 'ELSE', 'FLEW', 'GOOD', 'HOPE', 'IBEX']

def test_create_word_families()
    assert test_create_word_families(words, 'A', []) == \
           {'A---': ['ALLY'], '----': ['COOL', 'ELSE', 'FLEW', 'GOOD', 'HOPE', 'IBEX'], '---A': ['BETA'], '--A-': ['DEAL']}