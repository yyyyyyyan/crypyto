# crypyto

crypyto [_**kri**-pahy-toh_] is a Python package that provides simple usage of cryptography tools and ciphers on your programs.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

* Python >= 2.7 / Python >= 3.0
* Python packages:
	* (unidecode)[https://pypi.org/project/Unidecode/] to normalize strings

You can install **unidecode** with pip:
```
pip install unidecode
```

### Installing

For now, you can clone this repository using git

```
git clone https://github.com/yanorestes/crypyto.git
```

## Usage

Ciphers crypyto supports:
* [Polybius Square](https://en.wikipedia.org/wiki/Polybius_square)

```python
>>> from ciphers import PolybiusSquare
>>> ps = PolybiusSquare(width=5, height=5)
>>> ps.encrypt('EncryptedMessage')
'5x5#5-1;3-3;3-1;2-4;4-5;5-3;4-4;5-1;4-1;2-3;5-1;3-4;3-4;1-1;2-2;5-1'
>>> ps.decrypt('5x5#5-1;3-3;3-1;2-4;4-5;5-3;4-4;5-1;4-1;2-3;5-1;3-4;3-4;1-1;2-2;5-1')
'ENCRYPTEDMESSAGE'
```
* [Atbash](https://en.wikipedia.org/wiki/Atbash)

```python
>>> from ciphers import Atbash
>>> atbash = Atbash()
>>> atbash.encrypt('Hello, world!')
'SVOOL, DLIOW!'
>>> atbash.decrypt('SVOOL, DLIOW!')
'HELLO, WORLD!'
```

* [Caesar cipher](https://en.wikipedia.org/wiki/Caesar_cipher)

```python
>>> from ciphers import Caesar
>>> caesar = Caesar(key=5)
>>> caesar.encrypt('Hello, world!')
'MJQQT, BTWQI!'
>>> caesar.decrypt('MJQQT, BTWQI!')
HELLO, WORLD!
>>> caesar.brute_force('MJQQT, BTWQI!')
NKRRU, CUXRJ!
OLSSV, DVYSK!
...
HELLO, WORLD!
IFMMP, XPSME!
...
```

* [ROT13](https://en.wikipedia.org/wiki/ROT13)

```python
>>> from ciphers import ROT13
>>> ROT13.encrypt('Hello, world!')
'URYYB, JBEYQ!'
>>> ROT13.encrypt('URYYB, JBEYQ!')
'HELLO, WORLD!'
```

Cipher crypyto will soon support:
* AFFINE
* RAIL FENCE
* KEYWORD
* BEAUFORT
* TEMPLAR
* PORTA
* VIGENERE
* GRONSFELD
* AUTOKEY
* BACON
* CHAOCIPHER
* ADFGVX
* PLAYFAIR
* FOUR-SQUARE
* ONE-TIME PAD
* BIFID
* HILL CIPHER
* ENIGMA

## Authors

* **Yan Orestes** - *Initial work* - [yanorestes](https://github.com/yanorestes)


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details