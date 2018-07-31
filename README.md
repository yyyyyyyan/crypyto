# crypyto

crypyto [_kri-**pahy**-toh_] is a Python package that provides simple usage of cryptography tools and ciphers on your programs.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Dependencies

* Python >= 2.7 / Python >= 3.4
* Python packages (no need to worry if you use pip to install crypyto):
	* (unidecode)[https://pypi.org/project/Unidecode/] to normalize strings

### Installing

The easiest way to install crypyto is by using pip:

```
pip install crypyto
```

You can also clone this repository using git

```
git clone https://github.com/yanorestes/crypyto.git
```

## Usage

Ciphers crypyto supports:
- [x] [Polybius Square](#polybius-square)
- [x] [Atbash](#atbash)
- [x] [Caesar Cipher](#caesar-cipher)
- [x] [ROT13](#rot13)
- [x] [Affine Cipher](#affine-cipher)

<h3 id="polybius-square"><a href="https://en.wikipedia.org/wiki/Polybius_square">Polybius Square</a></h3>

```python
>>> from crypyto.ciphers import PolybiusSquare
>>> ps = PolybiusSquare(width=5, height=5)
>>> ps.encrypt('EncryptedMessage')
'5x5#5-1;3-3;3-1;2-4;4-5;5-3;4-4;5-1;4-1;2-3;5-1;3-4;3-4;1-1;2-2;5-1'
>>> ps.decrypt('5x5#5-1;3-3;3-1;2-4;4-5;5-3;4-4;5-1;4-1;2-3;5-1;3-4;3-4;1-1;2-2;5-1')
'ENCRYPTEDMESSAGE'
```

<h3 id="atbash"><a href="https://en.wikipedia.org/wiki/Atbash">Atbash</a></h3>

```python
>>> from crypyto.ciphers import Atbash
>>> atbash = Atbash()
>>> atbash.encrypt('Hello, world!')
'SVOOL, DLIOW!'
>>> atbash.decrypt('SVOOL, DLIOW!')
'HELLO, WORLD!'
```

<h3 id="caesar-cipher"><a href="https://en.wikipedia.org/wiki/Caesar_cipher">Caesar Cipher</a></h3>

```python
>>> from crypyto.ciphers import Caesar
>>> caesar = Caesar(key=5)
>>> caesar.encrypt('Hello, world!')
'MJQQT, BTWQI!'
>>> caesar.decrypt('MJQQT, BTWQI!')
'HELLO, WORLD!'
>>> caesar.brute_force('MJQQT, BTWQI!')
NKRRU, CUXRJ!
OLSSV, DVYSK!
...
HELLO, WORLD!
IFMMP, XPSME!
...
```

<h3 id="rot13"><a href="https://en.wikipedia.org/wiki/ROT13">ROT13</a></h3>

```python
>>> from crypyto.ciphers import ROT13
>>> ROT13.encrypt('Hello, world!')
'URYYB, JBEYQ!'
>>> ROT13.encrypt('URYYB, JBEYQ!')
'HELLO, WORLD!'
```

<h3 id="affine-cipher"><a href="https://en.wikipedia.org/wiki/Affine_cipher">Affine Cipher</a></h3>

```python
>>> from crypyto.cipher import Affine
>>> af = Affine(a=5, b=8)
>>> af.encrypt('Hello, world!')
'RCLLA, OAPLX!'
>>> af.decrypt('RCLLA, OAPLX!')
'HELLO, WORLD!'
```
TODO Ciphers:
- [ ] RAIL FENCE
- [ ] KEYWORD
- [ ] BEAUFORT
- [ ] PORTA
- [ ] VIGENERE
- [ ] GRONSFELD
- [ ] AUTOKEY
- [ ] BACON
- [ ] CHAOCIPHER
- [ ] ADFGVX
- [ ] PLAYFAIR
- [ ] FOUR-SQUARE
- [ ] ONE-TIME PAD
- [ ] BIFID
- [ ] HILL CIPHER
- [ ] ENIGMA

Substitution Alphabets crypyto supports:
- [x] [Morse Code](#morse-code)

<h3 id="morse-code"><a href="https://en.wikipedia.org/wiki/Morse_code">Morse Code</a></h3>

```python
>>> from crypyto.substitution_alphabets import Morse
>>> mc = Morse()
>>> mc.encrypt('Hello, world!')
'.... . .-.. .-.. --- --..-- / .-- --- .-. .-.. -.. -.-.--'
>>> mc.decrypt('.... . .-.. .-.. --- --..-- / .-- --- .-. .-.. -.. -.-.--')
'HELLO, WORLD!'
```

TODO Substitution Alphabets:
- [ ] Templar
- [ ] Binary
- [ ] Hexadecimal
- [ ] Octal
- [ ] L33TSP34K
- [ ] T9
- [ ] Base64
- [ ] Braille

TODO Features:
- [ ] Cipher identifier
- [ ] Auto decoder

## Authors

* **Yan Orestes** - *Initial work* - [yanorestes](https://github.com/yanorestes)


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.txt) file for details