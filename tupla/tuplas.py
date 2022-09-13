# -*- coding: utf-8 -*-
"""
"abacabad" c
"abacabaabacaba" _
"abcdefghijklmnopqrstuvwxyziflskecznslkjfabe" d
"bcccccccccccccyb" y
"""

def first_not_repeating_char(char_sequence):

    word_not_repeat = []

    for letter in char_sequence:
        if char_sequence.count(letter) == 1:
            word_not_repeat.append(letter)
    
    if word_not_repeat == []:
        return '_'
    else:
        return word_not_repeat[0]    

if __name__ == '__main__':

    char_sequence = input('Escriba una secuencia de caracteres: ')

    result = first_not_repeating_char(char_sequence)

    if result == '_':
        print('Todos los caracteres se repiten')
    
    else:
        print('El primer caracter no repetido es {}'.format(result))