"""
This module provides simple usage of functions related to substitutions alphabets
"""
import os
import re
import string
import random
from math import ceil, sqrt
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

class Binary:
    """
    `Binary` represents a text-to-binary manipulator

    Args:
        letter_splitter (str): A string which will be used to indicate characters separation. Defaults to ``' '``
    """

    def __init__(self, letter_splitter=' '):
        self.letter_splitter = letter_splitter

    def encrypt(self, text):
        """
        Returns the text translated to binary

        Args:
            text (str): The text to be translated to binary

        Examples:
            >>> from crypyto.substitution_alphabets import Binary
            >>> b = Binary()
            >>> b.encrypt('Hello, world!')
            '1001000 1100101 1101100 1101100 1101111 101100 100000 1110111 1101111 1110010 1101100 1100100 100001'
        """

        return self.letter_splitter.join(format(ord(char), 'b') for char in text)

    def decrypt(self, cipher):
        """
        Returns the binary-cipher translated to text

        Args:
            cipher (str): The binary-cipher to be translated to normal text

        Examples:
            >>> from crypyto.substitution_alphabets import Binary
            >>> b = Binary()
            >>> b.decrypt('1001000 1100101 1101100 1101100 1101111 101100 100000 1110111 1101111 1110010 1101100 1100100 100001')
            'Hello, world!'
        """

        return ''.join(chr(int(char, 2)) for char in cipher.split(self.letter_splitter))      

class ImageSubstitution:
    def __init__(self, abc, directory, extension):
        self.abc = abc.upper()
        self.not_abc_pattern = re.compile('[^{}]+'.format(re.escape(abc)), re.UNICODE)
        base_dir = os.path.dirname(os.path.realpath(__file__))
        self.filename = '{}/static/{}/'.format(base_dir, directory) + '{}' + '.{}'.format(extension)
        self.abc_to_img = self._get_abc_to_img()
        self.abc_to_img[''] = Image.open(self.filename.format('blank'))

    def _get_abc_to_img(self):
        abc_to_img = {letter:Image.open(self.filename.format(letter)) for letter in self.abc}
        return abc_to_img

    def _encrypt(self, text, filename='output.png', max_in_line=30):
        text = unidecode(text).upper()
        text = self.not_abc_pattern.sub('', text)
        max_height = max(self.abc_to_img[letter].size[1] for letter in text)
        if len(text) > max_in_line:
            total_width = sum(self.abc_to_img[letter].size[0] for letter in text[:max_in_line])
            max_height *= ceil(len(text) / max_in_line)
        else:
            total_width = sum(self.abc_to_img[letter].size[0] for letter in text)

        new_img = Image.new('RGB', (total_width, max_height), (255, 255, 255))
        x_offset = 0
        y_offset = 0
        for letter in text:
            new_img.paste(self.abc_to_img[letter], (x_offset, y_offset))
            y_offset = y_offset + self.abc_to_img[letter].size[1] if x_offset + self.abc_to_img[letter].size[0] >= total_width else y_offset
            x_offset = 0 if x_offset + self.abc_to_img[letter].size[0] >= total_width else x_offset + self.abc_to_img[letter].size[0]
        new_img.save(filename)

    def _get_rms(self, h1, h2):
        h1 = h1.histogram()
        h2 = h2.histogram()
        diff_squares = [(h1[i] - h2[i]) ** 2 for i in range(len(h1))]
        rms = sqrt(sum(diff_squares) / len(h1))
        return rms

    def _decrypt(self, filename):
        cipher = Image.open(filename)
        base_width, base_height = self.abc_to_img[self.abc[0]].size
        if cipher.size[0] % base_width > 0 or cipher.size[1] % base_height > 0:
            raise ValueError('Encrypted image is not properly sized')
        n_letters_p_line = cipher.size[0] // base_width
        n_lines = cipher.size[1] // base_height
        text = ''
        y_offset = 0
        for line in range(n_lines):
            x_offset = 0
            for letter in range(n_letters_p_line):
                cropped_letter = cipher.crop((x_offset, y_offset, x_offset + base_width, y_offset + base_height))
                all_rms = {l:self._get_rms(i, cropped_letter) for l,i in self.abc_to_img.items()}
                letter = min(all_rms, key=lambda k: all_rms[k])
                text += letter
                x_offset += base_width
            y_offset += base_height
        return text

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

    def decrypt(self, filename):
        """
        Returns the image cipher translated to normal text (str). It will most often do it wrong, because of specifications on Pigpen. I'll try to fix that soon.

        Args:
            filename (str): Filename of the cipher image file

        Raise:
            ValueError: If the size of the respective image doensn't match the cipher pattern. I'll try to work on that.

        Examples:
            >>> from crypyto.substitution_alphabets import Pigpen
            >>> pigpgen = Pigpen()
            >>> pigpen.decrypt('pigpen_hello.png')
            'BEJJMWMJJD'
            >>> pigpen.decrypt('pigpen_hello_max.png')
            'BEJJMWMJJD'
        """

        return super()._decrypt(filename)

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

    def decrypt(self, filename):
        """
        Returns the image cipher translated to normal text (str)

        Args:
            filename (str): Filename of the cipher image file

        Raise:
            ValueError: If the size of the respective image doensn't match the cipher pattern. I'll try to work on that.

        Examples:
            >>> from crypyto.substitution_alphabets import Templar
            >>> templar = Templar()
            >>> templar.decrypt('templar_hello.png')
            'HELLOWORLD'
            >>> templar.decrypt('templar_hello_max.png')
            'HELLOWORLD'
        """
        
        return super()._decrypt(filename)

class Betamaze(ImageSubstitution):
    """
    `Betamaze` represents a Betamaze Alphabet Manipulator

    Args:
        random_rotate (bool): Whether to randomly rotate each square letter (as it is possible with Betamaze). Defaults to ``False``
    """

    def __init__(self, random_rotate=False):
        self._random_rotate = True if random_rotate else False
        self._symbols_dict = {',':'comma', '.':'period', ' ':'space', '(':'parenthesis', ')':'parenthesis', ':':'colon', ';':'semicolon', '"':'quote'}
        abc = string.ascii_uppercase + ' ,.:;"()0123456789'
        super().__init__(abc, 'Betamaze', 'png')

    @property
    def random_rotate(self):
        return self._random_rotate

    @random_rotate.setter
    def random_rotate(self, value):
        self._random_rotate = True if value else False
        self.abc_to_img = self._get_abc_to_img()
        self.abc_to_img[''] = Image.open(self.filename.format('blank'))

    def _get_abc_to_img(self):
        symbols_dict = {'.'}
        if self.random_rotate:
            abc_to_img = {char:Image.open(self.filename.format(self._symbols_dict.get(char, char))).rotate(90 * random.randint(0,3)) for char in self.abc}
        else:
            abc_to_img = {char:Image.open(self.filename.format(self._symbols_dict.get(char, char))) for char in self.abc}
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

    def decrypt(self, filename):
        """
        Returns the image cipher translated to normal text (str)

        Args:
            filename (str): Filename of the cipher image file

        Raise:
            ValueError: If the size of the respective image doensn't match the cipher pattern. I'll try to work on that.

        Examples:
            >>> from crypyto.substitution_alphabets import Betamaze
            >>> betamaze = Betamaze()
            >>> betamaze.decrypt('betamaze_hello.png')
            'HELLO, WORLD'
            >>> betamaze.decrypt('betamaze_hello_random.png')
            'HELLO, WORLD'
        """

        return super()._decrypt(filename)