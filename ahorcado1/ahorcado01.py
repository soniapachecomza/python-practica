import random
import pygame

pygame = ['''

    +---+
    |   |
        |
        |
        |
        |
        ==========''','''

    +---+
    |   |
    0   |
        |
        |
        |
        ==========''','''

    +---+
    |   |
    0   |
    |   |
        |
        |
        ==========''','''

    +---+
    |   |
    0   |
   /|   |
        |
        |
        ==========''','''

    +---+
    |   |
    0   |
   /|\  |
        |
        |
        ==========''','''

    +---+
    |   |
    0   |
   /|\  |
   /    |
        |
        ==========''','''

    +---+
    |   |
    0   |
   /|\  |
   / \  |
        |
        ==========''','''
''']
WORDS = [
    'soskil',
    'programador',
    'desarrollador',
    'teclado',
    'imperio',
    'palindromo',
    'yucatan'
]

def display_board(hidden_word, tries):
    print(pygame[tries])
    print('')
    print(list(hidden_word))
    print('---*---*---*---*---*---')

def letter_replace(hidden_word, current_letter, word):
    if current_letter in word:
        for l in range(len(word)):
            if current_letter == word[l]:
                hidden_word = hidden_word[:l] + word[l] + hidden_word[l+1:]
    return hidden_word

def random_word():
    idx = random.randint(0,len(WORDS)-1)
    return str(WORDS[idx])

def run():
    word =  random_word()
    hidden_word = '-' * len(word)
    tries = 0
    loopcontrol = True
    usedletter = []
    won = True

    while loopcontrol:
        display_board(hidden_word, tries)
        current_letter = str(input('Escoge una letra: '))
        if current_letter in word and current_letter not in usedletter:
            hidden_word = letter_replace(hidden_word, current_letter, word)
            usedletter.append(current_letter)
        else:
            tries += 1
        if '-' not in hidden_word or tries > 6:
            loopcontrol = False
            won = False
            tries = 6

    display_board(hidden_word, tries)
    if won:
        print('F E L I C I D A D E S !')
    else:
        print('S U E R T E  L A  P R O X I M A')
    print('G R A C I A S  P O R  J U G A R!')




if __name__ == '__main__':
    print('B I E N V E N I D O S  A  A H O R C A D O S')
    run()