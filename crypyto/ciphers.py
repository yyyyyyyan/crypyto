import string
import re
import random
from math import gcd
from unidecode import unidecode

class PolybiusSquare:
    def __init__(self, width, height, abc=string.ascii_uppercase, ij=True):
        self.abc = self.abc.replace('J', '') if ij else self.abc
        self.width = width
        self.height = height
        self.mount_square()

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value < 1:
            raise ValueError('This square is not large enough to comprehend the whole alphabet.\nPlease increase width or height.')

    @property
    def height(self):
        return self._width

    @height.setter
    def height(self, value):
        if value * self.width < len(self.abc):
            raise ValueError('This square is not large enough to comprehend the whole alphabet.\nPlease increase width or height.')

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
        self.pos_to_abc['0-0'] = '�'

    def encrypt(self, text):
        text = unidecode(text).upper()
        text = text.replace('J', 'I') if len(self.abc) == 25 else text
        cipher = '{}x{}#'.format(self.width, self.height)
        positions = [random.choice(self.abc_to_pos.get(letter, ['0-0'])) for letter in text]
        cipher += ';'.join(positions)
        return cipher

    def decrypt(self, cipher):
        cipher = cipher.lower()
        match = re.search(r'(?:\d+x\d+#)?((?:\d+-\d+;?)+)', cipher)
        if match:
            positions = match.group(1).split(';')
            text = ''.join([self.pos_to_abc.get(pos, '0-0') for pos in positions])
            return text
        else:
            raise ValueError('Cipher doesn\'t match the Polybius Square pattern.')

class Atbash:
    def __init__(self, abc=string.ascii_uppercase):
        self.abc = abc
        self.cba = abc[::-1]
        self.convertion_dict = dict(zip(self.abc, self.cba))

    def encrypt(self, text, decode_unicode=True):
        text = unidecode(text).upper() if decode_unicode else text.upper()
        cipher = ''.join([self.convertion_dict.get(character, character) for character in text])
        return cipher

    decrypt = encrypt

class Caesar:
    def __init__(self, abc=string.ascii_uppercase, key=1):
        self.abc = abc
        self.max_value = len(abc) - 1
        self.key = abs(key)
        self.caesar_dict = dict(enumerate(abc, 1))

    def encrypt(self, text, decode_unicode=True, key=0):
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

    def decrypt(self, cipher, decode_unicode=True, key=0):
        key = key if key else self.key
        text = self.encrypt(cipher, decode_unicode, -key)
        return text

    def brute_force(self, cipher, decode_unicode=True):
        for try_number in range(1, self.max_value + 1):
            text = self.encrypt(cipher, decode_unicode, try_number)
            print(text)

ROT13 = Caesar(key=13)

class Affine:
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

    def encrypt(self, text):
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
        text = self.not_alnum_pattern.sub('', text) if self.only_alnum else text
        rails = [''] * self.n_rails
        def add_char(rail_index, *params):
            nonlocal rails
            rails[rail_index] += params[0]
        self._zig_zag_for(text, add_char)
        cipher = ''.join(rails)
        return cipher

    def decrypt(self, cipher):
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
        n_possibilities = len(cipher) * 2 - 4
        if n_possibilities > 20 and not output_file:
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