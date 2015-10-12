from demon_words import *
words = ['ALLY', 'BETA', 'COOL', 'DEAL', 'ELSE', 'FLEW', 'GOOD', 'HOPE', 'IBEX']


def test_create_word_families():
    assert create_word_families(words, 'A', []) == \
        {'A---': ['ALLY'], '----': ['COOL', 'ELSE', 'FLEW', 'GOOD', 'HOPE', 'IBEX'],
            '---A': ['BETA'], '--A-': ['DEAL']}


def test_find_max_family():
    word_families = {'----': ['COOL', 'GOOD'], '---E': ['ELSE', 'HOPE']}
    assert find_max_family(word_families, 'E') == '----'

    word_families2 = {'----': ['COOL', 'GOOD'], '---E': ['ELSE']}
    assert find_max_family(word_families2, 'W') == '----'