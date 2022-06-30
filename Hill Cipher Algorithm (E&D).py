import math
import string
import numpy as np
from sympy import Matrix

def get_alphabet():
	alphabet = {}
	for character in string.ascii_uppercase:
		alphabet[character] = string.ascii_uppercase.index(character)

	reverse_alphabet = {}
	for key, value in alphabet.items():
		reverse_alphabet[value] = key

	return alphabet, reverse_alphabet

def is_square(key):
	key_length = len(key)
	if 2 <= key_length == int(math.sqrt(key_length)) ** 2:
		return True
	else:
		return False

def get_key_matrix(key, alphabet):
	k = list(key)
	m = int(math.sqrt(len(k)))
	for (i, character) in enumerate(k):
		k[i] = alphabet[character]
	
	return np.reshape(k, (m, m))

def get_text_matrix(text, m, alphabet):
	matrix = list(text)
	remainder = len(text) % m
	for (i, character) in enumerate(matrix):
		matrix[i] = alphabet[character]
	if remainder != 0:
		for i in range(m - remainder):
			matrix.append(25)

	return np.reshape(matrix, (int(len(matrix) / m), m)).transpose()

def encrypt(key, plaintext, alphabet):
	m = key.shape[0]
	m_grams = plaintext.shape[1]

	ciphertext = np.zeros((m, m_grams)).astype(int)
	for i in range(m_grams):
		ciphertext[:, i] = np.reshape(np.dot(key, plaintext[:, i]) % len(alphabet), m)
	return ciphertext

def matrix_to_text(matrix, order, alphabet):
	if order == 't':
		text_array = np.ravel(matrix, order='F')
	else:
		text_array = np.ravel(matrix)
	text = ""
	for i in range(len(text_array)):
		text = text + alphabet[text_array[i]]
	return text

def get_inverse(matrix, alphabet):
	alphabet_len = len(alphabet)
	if math.gcd(int(round(np.linalg.det(matrix))), alphabet_len) == 1:
		matrix = Matrix(matrix)
		return np.matrix(matrix.inv_mod(alphabet_len))
	else:
		return None

def decrypt(k_inverse, c, alphabet):
	return encrypt(k_inverse, c, alphabet)

while True:
	print("\n---- Hill Cipher ----\n")
	print("1) Encrypt a Message.")
	print("2) Decipher a Message.")
	print("3) Quit.\n")
	choice=int(input("Enter Choice: "))

	alphabet, reverse_alphabet = get_alphabet()

	if choice == 1:
		plaintext = input("\nEnter Plain Text: ").replace(" ","").upper()
		key = input("\nEnter Key: ").replace(" ","").upper()

		if is_square(key):
			k = get_key_matrix(key, alphabet)
			print("\nKey Matrix:\n", k)

			p = get_text_matrix(plaintext, k.shape[0], alphabet)
			print("\nPlaintext Matrix:\n", p)

			c = encrypt(k, p, alphabet)

			ciphertext = matrix_to_text(c, "t", reverse_alphabet)

			print("\nCiphertext Matrix:\n", c, "\n")
			
			print("\nCiphertext: ", ciphertext)
		    
		else:
		    print("\nThe length of the key must be a square and >= 2.\n")

	elif choice == 2:
		ciphertext = input("\nEnter Cipher Text: ").replace(" ","").upper()
		key = input("\nEnter Key: ").replace(" ","").upper()

		if is_square(key):
			k = get_key_matrix(key, alphabet)

			k_inverse = get_inverse(k, alphabet)

			if k_inverse is not None:
				c = get_text_matrix(ciphertext, k_inverse.shape[0], alphabet)

				print("\nKey Matrix:\n", k)

				print("\nKey Matrix Inverse:\n", k_inverse)

				print("\nCiphertext Matrix:\n", c)

				p = decrypt(k_inverse, c, alphabet)

				plaintext = matrix_to_text(p, "t", reverse_alphabet)

				print("\nPlaintext Matrix:\n", p, "\n")

				print("\nPlaintext: ", plaintext)

			else:
				print("\nThe matrix of the key provided is not invertible.\n")
		else:
		    print("\nThe key must be a square and size >= 2.\n")
	
	elif choice == 3:
		exit(0)