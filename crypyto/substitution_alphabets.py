import re
import string
from math import ceil
from unidecode import unidecode
from PIL import Image

class Morse:
    def __init__(self, word_splitter='/'):
        self.word_splitter = word_splitter
        self.char_to_morse = {
        ' ': word_splitter,
        'A': '.-',
        'B': '-...',
        'C': '-.-.',
        'D': '-..',
        'E': '.',
        'F': '..-.',
        'G': '--.',
        'H': '....',
        'I': '..',
        'J': '.---',
        'K': '-.-',
        'L': '.-..',
        'M': '--',
        'N': '-.',
        'O': '---',
        'P': '.--.',
        'Q': '--.-',
        'R': '.-.',
        'S': '...',
        'T': '-',
        'U': '..-',
        'V': '...-',
        'W': '.--',
        'X': '-..-',
        'Y': '-.--',
        'Z': '--..',
        '0': '-----',
        '1': '.----',
        '2': '..---',
        '3': '...--',
        '4': '....-',
        '5': '.....',
        '6': '-....',
        '7': '--...',
        '8': '---..',
        '9': '----.',
        '.': '.-.-.-',
        ',': '--..--',
        '?': '..--..',
        '\'': '.----.',
        '!': '-.-.--',
        '/': '-..-.',
        '(': '-.--.',
        ')': '-.--.-',
        '&': '.-...',
        ':': '---...',
        ';': '-.-.-.',
        '=': '-...-',
        '+': '.-.-.',
        '-': '-....-',
        '_': '..--.-',
        '"': '.-..-.',
        '$': '...-..-',
        '@': '.--.-.',
        }

        self.morse_to_char = {v:k for k, v in self.char_to_morse.items()}
 
    def encrypt(self, text):
        text = unidecode(text).upper()
        cipher = ' '.join([self.char_to_morse.get(character, character) for character in text]).strip()
        return cipher

    def decrypt(self, cipher):
        text = ''
        for word in cipher.split(self.word_splitter):
            text += ''.join([self.morse_to_char.get(character, '�') for character in word.split()])
            text += ' '
        return text.strip()

class ImageSubstitution:
    def __init__(self, abc, directory, extension):
        self.abc = abc.upper()
        self.not_abc_pattern = re.compile('[^{}]+'.format(abc), re.UNICODE)
        self.filename = 'static/{}/'.format(directory) + '{}' + '.{}'.format(extension)

    def encrypt(self, text, filename, max_in_line=float('inf')):
        text = unidecode(text).upper()
        text = self.not_abc_pattern.sub('', text)
        abc_to_img = {letter:Image.open(self.filename.format(letter)) for letter in set(text)}
        max_height = max(abc_to_img[letter].size[1] for letter in text)
        if len(text) > max_in_line:
            total_width = sum(abc_to_img[letter].size[0] for letter in text[:max_in_line])
            max_height *= ceil(len(text) / max_in_line)
        else:
            total_width = sum(abc_to_img[letter].size[0] for letter in text)

        new_img = Image.new('RGB', (total_width, max_height))
        x_offset = 0
        y_offset = 0
        for letter in text:
            new_img.paste(abc_to_img[letter], (x_offset, y_offset))
            y_offset = y_offset + abc_to_img[letter].size[1] if x_offset + abc_to_img[letter].size[0] >= total_width else y_offset
            x_offset = 0 if x_offset + abc_to_img[letter].size[0] >= total_width else x_offset + abc_to_img[letter].size[0]
        new_img.save(filename)

Templar = ImageSubstitution(string.ascii_uppercase, 'Templar', 'png')