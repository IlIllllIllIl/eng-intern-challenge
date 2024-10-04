import sys

braille_to_english = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'O',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y', 
    'O..OOO': 'z', '.....O': 'capital follows', '.O...O': 'decimal follows', '.O.OOO': 'number follows', 
    '..OO.O': '.', '..O...': ',', '..O.OO': '?', '..OOO.': '!', '..OO..': ':', 
    '..O.O.': ';', '....OO': '-', '.O..O.': '/', '.OO..O': '<', 'O..OO.': '>',
    'O.O..O': '(', '.O.OO.': ')', '......': ' '
}

number_braille = {
    'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 'O..O..': '5', 
    'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8', '.OO...': '9', '.OOO..': '0', 
}

english_to_braille = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'O': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 
    'z': 'O..OOO', 'capital follows': '.....O', 'decimal follows': '.O...O', 'number follows': '.O.OOO', 
    '.': '..OO.O', ',': '..O...', '?': '..O.OO', '!': '..OOO.', ':': '..OO..', 
    ';': '..O.O.', '-': '....OO', '/': '.O..O.', '<': '.OO..O', '>': 'O..OO.',
    '(': 'O.O..O', ')': '.O.OO.', ' ': '......'
}

number_english = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', 
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..', 
}

def is_braille(input):
    return all(c in 'O.' for c in input)

def translator(input):
    if is_braille(input):  
        return translatorToEnglish(input)
    else:
        return translatorToBraille(input)

def translatorToEnglish(input):
    english = []
    is_capital = False
    is_number = False
    i = 0

    while i < len(input):
        braille_char = input[i:i+6]

        if braille_to_english[braille_char] == 'capital follows':
            is_capital = True
        elif braille_to_english[braille_char] == 'number follows':
            is_number = True
        elif braille_char == '......':
            english.append(' ')
            i += 6
            continue
        else:
            if is_capital: 
                english.append(braille_to_english[braille_char].upper())
                is_capital = False
            elif is_number:
                while braille_char != '......' and i < len(input):
                    english.append(number_braille[braille_char])
                    i += 6
                    if i < len(input):
                        braille_char = input[i:i+6]
                    else:
                        break
                is_number = False
                continue
            else: 
                english.append(braille_to_english[braille_char])
        i += 6
    return ''.join(english)

def translatorToBraille(input):
    braille = []
    is_num_seq = False

    for i in input:
        if i.isupper():
            braille.append(english_to_braille['capital follows'])
            braille.append(english_to_braille[i.lower()])
        elif i.isdigit():
            if not is_num_seq:
                braille.append(english_to_braille['number follows'])
                is_num_seq = True    
            braille.append(number_english[i])
        else:
            if is_num_seq:
                is_num_seq = False
            braille.append(english_to_braille[i])
    return ''.join(braille)

print(translator(' '.join(sys.argv[1:])))