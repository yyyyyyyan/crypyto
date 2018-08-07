"""
This module provides simple usage of functions related to a list of ciphers  
"""

import string
import re
import random
from math import gcd
from unidecode import unidecode

class PolybiusSquare:
    """
    `PolybiusSquare` represents a Polybius Square cipher manipulator

    Args:
        width (int): The square's width. Must be at least 1. Width times height must be greater than the alphabet length
        height (int): The square's height. Must be at least 1. Height times width must be greater than the alphabet length
        abc (str): The alphabet used in the square. Defaults to ``string.ascii_uppercase``
        ij (bool): Whether 'i' and 'j' are treated as the same letter. Defaults to ``True``

    Raises:
        ValueError: When `width` is smaller than 1
        ValueError: When ``width * height`` is smaller than ``len(abc)``

    """

    def __init__(self, width, height, abc=string.ascii_uppercase, ij=True):
        self.abc = abc.replace('J', '') if ij else self.abc
        self.width = width
        self.height = height
        self.mount_square()
        self.not_abc_pattern = re.compile('[^{}]+'.format(abc), re.UNICODE)

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value < 1:
            raise ValueError('This square is not large enough to comprehend the whole alphabet.\nPlease increase width or height.')
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value * self.width < len(self.abc):
            raise ValueError('This square is not large enough to comprehend the whole alphabet.\nPlease increase width or height.')
        self._height = value

    def mount_square(self):
        self.square_area = self.width * self.height
        self.abc_square = (self.abc * (self.square_area // len(self.abc) + 1))[:self.square_area]
        self.square = [self.abc_square[i:i+self.width] for i in range(0, len(self.abc_square), self.width)]

        self.abc_to_pos = {letter:[] for letter in self.abc}
        for line_index, line in enumerate(self.square):
            for col_index, letter in enumerate(line):
                self.abc_to_pos[letter].append('{}-{}'.format(col_index + 1, line_index + 1))
        
        self.pos_to_abc = {}
        for letter in self.abc:
            for pos in self.abc_to_pos[letter]:
                self.pos_to_abc[pos] = letter

    def encrypt(self, text):
        """
        Returns encrypted text (str)

        Args:
            text (str): The text to be encrypted

        Examples:
            >>> from crypyto.ciphers import PolybiusSquare
            >>> ps = PolybiusSquare(5, 5)
            >>> ps.encrypt('EncryptedMessage')
            '5x5#5-1;3-3;3-1;2-4;4-5;5-3;4-4;5-1;4-1;2-3;5-1;3-4;3-4;1-1;2-2;5-1'
        """

        text = unidecode(text).upper()
        text = text.replace('J', 'I') if len(self.abc) == 25 else text
        text = self.not_abc_pattern.sub('', text)
        cipher = '{}x{}#'.format(self.width, self.height)
        positions = [random.choice(self.abc_to_pos[letter]) for letter in text]
        cipher += ';'.join(positions)
        return cipher

    def decrypt(self, cipher):
        """
        Returns decrypted cipher (str)

        Args:
            cipher (str): The cipher to be decrypted. May or may not contain the square size at the beggining (e.g. '5x5#')

        Raise:
            ValueError: When ``cipher`` doesn't match the Polybius Square pattern

        Examples:
            >>> from crypyto.ciphers import PolybiusSquare
            >>> ps = PolybiusSquare(5, 5)
            >>> ps.decrypt('5x5#5-1;3-3;3-1;2-4;4-5;5-3;4-4;5-1;4-1;2-3;5-1;3-4;3-4;1-1;2-2;5-1')
            'ENCRYPTEDMESSAGE'
        """

        cipher = cipher.lower()
        match = re.search(r'(?:\d+x\d+#)?((?:\d+-\d+;?)+)', cipher)
        if match:
            positions = match.group(1).split(';')
            text = ''.join([self.pos_to_abc[pos] for pos in positions])
            return text
        else:
            raise ValueError('Cipher doesn\'t match the Polybius Square pattern.')

class Atbash:
    """
    `Atbash` represents an Atbash cipher manipulator

    Args:
        abc (str): The alphabet used in the cipher. Defaults to ``string.ascii_uppercase``

    """

    def __init__(self, abc=string.ascii_uppercase):
        self.abc = abc
        self.cba = abc[::-1]
        self.convertion_dict = dict(zip(self.abc, self.cba))

    def encrypt(self, text, decode_unicode=True):
        """
        Returns encrypted text (str)

        Args:
            text (str): The text to be encrypted
            decode_unicode (bool): Whether the text should have unicode characters converted to ascii before encrypting. Defautls to ``True``
        
        Examples:
            >>> from crypyto.ciphers import Atbash
            >>> atbash = Atbash()
            >>> atbash.encrypt('Hello, world!')
            'SVOOL, DLIOW!'
        """

        text = unidecode(text).upper() if decode_unicode else text.upper()
        cipher = ''.join([self.convertion_dict.get(character, character) for character in text])
        return cipher

    def decrypt(self, cipher, decode_unicode=True):
        """
        Returns decrypted text (str)

        Args:
            cipher (str): The cipher to be decrypted
            decode_unicode (bool): Whether the cipher should have unicode characters converted to ascii before decrypting. Defautls to ``True``
        
        Examples:
            >>> from crypyto.ciphers import Atbash
            >>> atbash = Atbash()
            >>> atbash.decrypt('SVOOL, DLIOW!')
            'HELLO, WORLD!'
        """

        return self.encrypt(cipher, decode_unicode)

class Caesar:
    """
    `Caesar` represents a Caesar cipher manipulator
    
    Args:
        abc (str): The alphabet used in the cipher. Defaults to ``string.ascii_uppercase``
        key (int): The key to initialize the cipher manipulator. Defaults to ``1``
    """

    def __init__(self, abc=string.ascii_uppercase, key=1):
        self.abc = abc
        self.max_value = len(abc) - 1
        self.key = abs(key)
        self.caesar_dict = dict(enumerate(abc, 1))

    @property
    def abc(self):
        return self._abc
    
    @abc.setter
    def abc(self, value):
        self._abc = value
        self.max_value = len(value) - 1

    @property
    def max_value(self):
        return self._max_value
    
    @max_value.setter
    def max_value(self, value):
        if value != len(self.abc) - 1:
            raise ValueError('max_value is automatically set')
        self._max_value = value

    def encrypt(self, text, decode_unicode=True, key=None):
        """
        Returns encrypted text (str)

        Args:
            text (str): The text to be encrypted
            decode_unicode (bool): Whether the text should have unicode characters converted to ascii before encrypting. Defautls to ``True``
            key (int|None): The key used to encrypt. Defaults to ``None``, which uses the value from ``self.key``

        Examples:
            >>> from crypyto.ciphers import Caesar
            >>> caesar = Caesar(key=5)
            >>> caesar.encrypt('Hello, world!')
            'MJQQT, BTWQI!'
        """

        key = key if key else self.key
        text = unidecode(text).upper() if decode_unicode else text.upper()
        cipher = ''
        for letter in text:
            if letter in self.abc:
                letter_index = self.abc.index(letter) + key
                if letter_index > self.max_value:
                    letter_index = letter_index - self.max_value - 1
                if letter_index < 0:
                    letter_index = letter_index + self.max_value + 1

                cipher += self.abc[letter_index]
            else:
                cipher += letter
        return cipher

    def decrypt(self, cipher, decode_unicode=True, key=None):
        """
        Returns decrypted cipher (str)

        Args:
            cipher (str): The cipher to be decrypted
            decode_unicode (bool): Whether the cipher should have unicode characters converted to ascii before decrypting. Defautls to ``True``
            key (int|None): The key used to decrypt. Defaults to ``None``, which uses the value from ``self.key``

        Examples:
            >>> from crypyto.ciphers import Caesar
            >>> caesar = Caesar(key=5)
            >>> caesar.decrypt('MJQQT, BTWQI!')
            'HELLO, WORLD!'
        """

        key = key if key else self.key
        text = self.encrypt(cipher, decode_unicode, -key)
        return text

    def brute_force(self, cipher, decode_unicode=True, output_file=None):
        """
        Prints (to stdout or specified file) all possible results

        Args:
            cipher (str): The cipher to be decrypted
            decode_unicode (bool): Whether the cipher should have unicode characters converted to ascii before decrypting. Defautls to ``True``
            output_file (str|None): The filename of the file the results are gonna be printed. Defaults to ``None``, which indicated printing on stdout

        Examples:
            >>> from crypyto.ciphers import Caesar
            >>> caesar = Caesar()
            >>> caesar.brute_force('MJQQT, BTWQI!')
            NKRRU, CUXRJ!
            OLSSV, DVYSK!
            ...
            HELLO, WORLD!
            IFMMP, XPSME!
            ...
        """

        if self.max_value > 30 and not output_file:
            print('There are {} possible results. You can specify an output file in the parameter output_file'.format(self.max_value))
            print('Are you sure you want to print them all (Y/N)?')
            if not input().upper().startswith('Y'):
                return

        results = ''
        for try_number in range(1, self.max_value + 1):
            text = self.encrypt(cipher, decode_unicode, try_number)
            results += text + '\n'

        if output_file:
            with open(output_file, 'w') as out:
                out.write(results.strip())
        else:
            print(results.strip())

ROT13 = Caesar(key=13)

class Affine:
    """
    `Affine` represents an Affine cipher manipulator

    Args:
        a (int): Value of ``a``. Must be coprime to ``len(self.abc)``
        b (int): Value of ``b``
        abc (str): The alphabet used in the cipher. Defaults to ``string.ascii_uppercase``
    """

    def __init__(self, a, b, abc=string.ascii_uppercase):
        self.abc = abc
        self.a = a
        self.b = b
        self.pos_to_abc = dict(enumerate(abc))
        self.abc_to_pos = {v:k for k, v in self.pos_to_abc.items()}

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, value):
        if gcd(value, len(self.abc)) != 1:
            raise ValueError('Parameter a must be coprime to {}'.format(len(self.abc)))
        self._a = value

    def encrypt(self, text):
        """
        Returns encrypted text (str)

        Args:
            text (str): Text to be encrypted

        Examples:
            >>> from crypyto.cipher import Affine
            >>> af = Affine(a=5, b=8)
            >>> af.encrypt('Hello, world!')
            'RCLLA, OAPLX!'
        """

        text = unidecode(text).upper()
        cipher = ''
        for character in text:
            if character in self.abc:
                x = self.abc_to_pos[character]
                cipher_pos = (self.a * x + self.b) % len(self.abc)
                character = self.pos_to_abc[cipher_pos]
            cipher += character
        return cipher

    def decrypt(self, cipher):
        """
        Returns decrypted cipher (str)

        Args:
            cipher (str): Cipher to be decrypted

        Examples:
            >>> from crypyto.cipher import Affine
            >>> af = Affine(a=5, b=8)
            >>> af.decrypt('RCLLA, OAPLX!')
            'HELLO, WORLD!'
        """

        cipher = cipher.upper()
        text = ''
        for character in cipher:
            if character in self.abc:
                mod_inv = -self.a % len(self.abc)
                cipher_pos = self.abc_to_pos[character]
                x = mod_inv * (cipher_pos - self.b) % 26
                character = self.pos_to_abc[x]
            text += character
        return text

class RailFence:
    """
    `RailFence` represents a Rail Fence cipher manipulator

    Args:
        n_rails (int): Number of rails
        only_alnum (bool): Whether the manipulator will only encrypt alphanumerical characters. Defaults to ``False``
        direction (str): Default direction to start zigzagging. Must be ``'D'`` (Downwards) or ``'U'`` (Upwards). Defaults to ``'D'``
    """

    def __init__(self, n_rails, only_alnum=False, direction='D'):
        self.direction = direction
        self.n_rails = n_rails
        self.only_alnum = only_alnum
        self.not_alnum_pattern = re.compile(r'[\W_]+', re.UNICODE)
        self.direction = direction

    @property
    def n_rails(self):
        return self._n_rails

    @n_rails.setter
    def n_rails(self, value):
        self._n_rails = abs(value) if abs(value) > 1 else 2
        self.cycle = self.n_rails * 2 - 2

    @property
    def cycle(self):
        return self._cycle
    
    @cycle.setter
    def cycle(self, value):
        if value != self.n_rails * 2 - 2:
            raise ValueError('Cycle number is automatically calculated')
        self._cycle = value

    @property
    def direction(self):
        return self._direction
    
    @direction.setter
    def direction(self, value):
        if value[0].upper() not in ['D', 'U']:
            raise ValueError('direction must be (U)p or (D)own')
        self._direction = value[0].upper()
    
    def _zig_zag_for(self, iterate_over, action):
        direction = self.direction
        rail_index = 0 if direction == 'D' else self.n_rails - 1
        for n in iterate_over:
            action(rail_index, n)
            if rail_index == 0:
                direction = 'U'
            elif rail_index == self.n_rails - 1:
                direction = 'D'
            rail_index = rail_index + 1 if direction == 'U' else rail_index - 1

    def encrypt(self, text):
        """
        Returns encrypted text (str)

        Args:
            text (str): The text to be encrypted

        Examples:
            >>> from crypyto.cipher import RailFence
            >>> rf = RailFence(n_rails=3, only_alnum=True)
            >>> rf.encrypt('WE ARE DISCOVERED. FLEE AT ONCE')
            'WECRLTEERDSOEEFEAOCAIVDEN'
        """

        text = self.not_alnum_pattern.sub('', text) if self.only_alnum else text
        rails = [''] * self.n_rails
        def add_char(rail_index, *params):
            nonlocal rails
            rails[rail_index] += params[0]
        self._zig_zag_for(text, add_char)
        cipher = ''.join(rails)
        return cipher

    def decrypt(self, cipher):
        """
        Returns decrypted cipher

        Args:
            cipher (str): The cipher to be decrypted

        Examples:
            >>> from crypyto.cipher import RailFence
            >>> rf = RailFence(n_rails=3, only_alnum=True)
            >>> rf.decrypt('WECRLTEERDSOEEFEAOCAIVDEN')
            'WEAREDISCOVEREDFLEEATONCE'
        """

        base_width, n_extra = divmod(len(cipher), self.cycle)
        n_characters_rails = [base_width * 2 if 0 < n_rail < self.n_rails - 1 else base_width for n_rail in range(self.n_rails)] 
        def add_n_characters(rail_index, *trash):
            nonlocal n_characters_rails
            n_characters_rails[rail_index] += 1
        self._zig_zag_for(range(n_extra), add_n_characters)
        rails = [[] for n in range(self.n_rails)]

        cipher_index = 0
        for rail_index, n_characters in enumerate(n_characters_rails):
            rails[rail_index].extend(list(cipher[cipher_index:cipher_index + n_characters]))
            cipher_index += n_characters

        text = ''
        def add_decrypted_char(rail_index, *trash):
            nonlocal text
            text += rails[rail_index].pop(0)
        self._zig_zag_for(range(len(cipher)), add_decrypted_char)
        return text

    def brute_force(self, cipher, output_file=None):
        """
        Prints (to stdout or specified file) all possible decrypted results

        Args:
            cipher (str): The cipher to be decrypted
            output_file (str|None): The filename of the file the results are gonna be printed. Defaults to ``None``, which indicated printing on stdout

        Examples:
            >>> from crypyto.ciphers import RailFence
            >>> rf = RailFence(n_rails=1, only_alnum=True)
            >>> rf.decrypt('WECRLTEERDSOEEFEAOCAIVDEN')
            There are 46 possible results. You can specify an output file in the parameter output_file
            Are you sure you want to print them all (Y/N)?
            Y
            WEEFCERALOTCEAEIRVDDSEONE
            WEAREDISCOVEREDFLEEATONCE
            ...
            NEDVIACOAEFEEOSDREETREWCL
            NEDVIACOAEFEEOSDREETLREWC
        """

        n_possibilities = len(cipher) * 2 - 4
        if n_possibilities > 30 and not output_file:
            print('There are {} possible results. You can specify an output file in the parameter output_file'.format(n_possibilities))
            print('Are you sure you want to print them all (Y/N)?')
            if not input().upper().startswith('Y'):
                return
        initial_direction = self.direction
        results = ''
        for direction in ['D', 'U']:
            self.direction = direction
            initial_n_rails = self.n_rails
            for n in range(2, len(cipher)):
                self.n_rails = n
                results += self.decrypt(cipher) + '\n'
            self.n_rails = initial_n_rails
        self.direction = initial_direction
        if output_file:
            with open(output_file, 'w') as out:
                out.write(results.strip())
        else:
            print(results.strip())