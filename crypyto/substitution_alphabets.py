"""
This module provides simple usage of functions related to substitutions alphabets
"""
import os
import re
import string
import random
from math import ceil
from unidecode import unidecode
from PIL import Image

class Morse:
    """
    `Morse` represents a Morse Code manipulator

    Args:
        word_splitter (str): A string which will be used to indicate words separation. Defaults to ``'/'``
    """

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
        """
        Returns translated text into Morse Code (str)

        Args:
            text (str): The text to be translated into Morse Code

        Examples:
            >>> from crypyto.subsititution_alphabets import Morse
            >>> morse = Morse()
            >>> morse.encrypt('Hello, world!')
            '.... . .-.. .-.. --- --..-- / .-- --- .-. .-.. -.. -.-.--'
        """

        text = unidecode(text).upper()
        cipher = ' '.join([self.char_to_morse.get(character, character) for character in text]).strip()
        return cipher

    def decrypt(self, cipher):
        """
        Returns translated cipher into plain text

        Args:
            cipher (str): The morse code to be translated into plain text

        Examples:
            >>> from crypyto.substitution_alphabets import Morse
            >>> morse = Morse()
            >>> morse.decrypt('.... . .-.. .-.. --- --..-- / .-- --- .-. .-.. -.. -.-.--')
            'HELLO, WORLD!'
        """

        text = ''
        for word in cipher.split(self.word_splitter):
            text += ''.join([self.morse_to_char.get(character, '�') for character in word.split()])
            text += ' '
        return text.strip()

class ImageSubstitution:
    def __init__(self, abc, directory, extension):
        self.abc = abc.upper()
        self.not_abc_pattern = re.compile('[^{}]+'.format(re.escape(abc)), re.UNICODE)
        base_dir = os.path.dirname(os.path.realpath(__file__))
        self.filename = '{}/static/{}/'.format(base_dir, directory) + '{}' + '.{}'.format(extension)

    def _get_abc_to_img(self, text):
        abc_to_img = {letter:Image.open(self.filename.format(letter)) for letter in set(text)}
        return abc_to_img

    def _encrypt(self, text, filename='output.png', max_in_line=30):
        text = unidecode(text).upper()
        text = self.not_abc_pattern.sub('', text)
        abc_to_img = self._get_abc_to_img(text)
        max_height = max(abc_to_img[letter].size[1] for letter in text)
        if len(text) > max_in_line:
            total_width = sum(abc_to_img[letter].size[0] for letter in text[:max_in_line])
            max_height *= ceil(len(text) / max_in_line)
        else:
            total_width = sum(abc_to_img[letter].size[0] for letter in text)

        new_img = Image.new('RGB', (total_width, max_height), (255, 255, 255))
        x_offset = 0
        y_offset = 0
        for letter in text:
            new_img.paste(abc_to_img[letter], (x_offset, y_offset), mask=abc_to_img[letter])
            y_offset = y_offset + abc_to_img[letter].size[1] if x_offset + abc_to_img[letter].size[0] >= total_width else y_offset
            x_offset = 0 if x_offset + abc_to_img[letter].size[0] >= total_width else x_offset + abc_to_img[letter].size[0]
        new_img.save(filename)

class Pigpen(ImageSubstitution):
    """
    `Pigpen` represents a Pigpen Cipher manipulator
    """

    def __init__(self):
        super().__init__(string.ascii_uppercase, 'Pigpen', 'png')

    def encrypt(self, text, filename='output.png', max_in_line=30):
        """
        Creates an image file with the translated text

        Args:
            text (str): Text to be translated to the Pigpen alphabet
            filename (str): The filename of the image file with the translated text. Defaults to ``'output.png'``
            max_in_line (int): The max number of letters per line. Defaults to ``30``

        Examples:
            >>> from crypyto.substitution_alphabets import Pigpen
            >>> pigpen = Pigpen()
            >>> pigpen.encrypt('Hello, world!', 'pigpen_hello.png')
            >>> pigpen.encrypt('Hello, world!', 'pigpen_hello_max.png', 5)
        """

        super()._encrypt(text, filename, max_in_line)

class Templar(ImageSubstitution):
    """
    `Templar` represents a Templar Cipher manipulator
    """

    def __init__(self):
        super().__init__(string.ascii_uppercase, 'Templar', 'png')

    def encrypt(self, text, filename='output.png', max_in_line=30):
        """
        Creates an image file with the translated text

        Args:
            text (str): Text to be translated to the Templar alphabet
            filename (str): The filename of the image file with the translated text. Defaults to ``'output.png'``
            max_in_line (int): The max number of letters per line. Defaults to ``30``
        
        Examples:
            >>> from crypyto.substitution_alphabets import Templar
            >>> templar = Templar()
            >>> templar.encrypt('Hello, world!', 'templar_hello.png')
            >>> templar.encrypt('Hello, world!', 'templar_hello_max.png', 5)
        """

        super()._encrypt(text, filename, max_in_line)

class Betamaze(ImageSubstitution):
    """
    `Betamaze` represents a Betamaze Alphabet Manipulator

    Args:
        random_rotate (bool): Whether to randomly rotate each square letter (as it is possible with Betamaze). Defaults to ``False``
    """

    def __init__(self, random_rotate=False):
        self.random_rotate = random_rotate
        self._symbols_dict = {',':'comma', '.':'period', ' ':'space', '(':'parenthesis', ')':'parenthesis', ':':'colon', ';':'semicolon', '"':'quote'}
        abc = string.ascii_uppercase + ' ,.:;"()0123456789'
        super().__init__(abc, 'Betamaze', 'png')

    def _get_abc_to_img(self, text):
        symbols_dict = {'.'}
        if self.random_rotate:
            abc_to_img = {char:Image.open(self.filename.format(self._symbols_dict.get(char, char))).rotate(90 * random.randint(0,3)) for char in set(text)}
        else:
            abc_to_img = {char:Image.open(self.filename.format(self._symbols_dict.get(char, char))) for char in set(text)}
        return abc_to_img

    def encrypt(self, text, filename='output.png', max_in_line=10):
        """
        Creates an image file with the translated text

        Args:
            text (str): Text to be translated to the Betamaze alphabet
            filename (str): The filename of the image file with the translated text. Defaults to ``'output.png'``
            max_in_line (int): The max number of letters per line. Defaults to ``10``

        Examples:
            >>> from crypyto.substitution_alphabets import Betamaze
            >>> betamaze = Betamaze()
            >>> betamaze.encrypt('Hello, world!', 'betamaze_hello.png', 5)
            >>>
            >>> betamaze_random = Betamaze(random_rotate=True)
            >>> betamaze_random.encrypt('Hello, world!', 'betamaze_hello_random.png', 5)
        """

        super()._encrypt(text, filename, max_in_line)