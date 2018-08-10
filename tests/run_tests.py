import os
from crypyto.ciphers import *
from crypyto.substitution_alphabets import *

ciphers = {
	'tests/PolybiusSquare.out':PolybiusSquare(5, 5),
	'tests/Atbash.out':Atbash(),
	'tests/Caesar.out':Caesar(key=7),
	'tests/Affine.out':Affine(5, 8),
	'tests/RailFence.out':RailFence(3),
	'tests/Morse.out':Morse(),
	'tests/Keyword.out':Keyword('secret'),
	'tests/Vigenere.out':Vigenere('secret'),
	}

with open('tests/input.in', 'r') as input_file:
	input_strings = input_file.read().split('\n')

for cipher in ciphers:
	with open(cipher, 'r') as output:
		encrypted_outputs = output.read().split('\n')
	for input_text, encrypted_text in zip(input_strings, encrypted_outputs):
			encrypted, decrypted = encrypted_text.split(' <<equals to>> ')
			assert ciphers[cipher].encrypt(input_text) == encrypted
			assert decrypted == ciphers[cipher].decrypt(encrypted)