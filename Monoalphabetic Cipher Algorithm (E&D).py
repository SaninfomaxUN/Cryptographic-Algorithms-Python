import string
import random

def mono_encrypt():
	
	alph_lst_ky = [i for i in string.ascii_uppercase] 
	random.shuffle(alph_lst_ky)
	key = ''.join(map(str, alph_lst_ky))
	cipherText = ''
	plainText = input("Enter Plain Text: ")

	for i in plainText:
		letterIndex = ord(i.upper()) - 65
		if i.islower():
			cipherText += alph_lst_ky[letterIndex].lower()
		else:
			cipherText += alph_lst_ky[letterIndex]
	print(f"\nKey:\n{string.ascii_uppercase}\n{key}")
	print("\nCipher Text :", cipherText)

def mono_decrypt():

	alph_lst_ky = [i for i in string.ascii_uppercase] 

	plainText = ""
	cipherText = input("\nEnter Cipher Text: ")
	key = input("Enter Key: ")

	for i in cipherText:
		letterIndex = (key.find(i.upper())) + 65
		if i.islower():
			plainText += chr(letterIndex).lower()
		else:
			plainText += chr(letterIndex)
	print(f"\nKey:\n{string.ascii_uppercase}\n{key}")
	print("\nPlain Text :", plainText)


while True:
	print("\n----- Mono Alphabetic Algorithm -----") 
	print("1. Encrypt Text")
	print("2. Decrypt Text")
	print("3. Exit")
	ch = int(input("\nEnter Your Choice: "))
	
	if ch == 1:
		mono_encrypt()
	elif ch == 2:
		mono_decrypt()
	elif ch == 3:
		print("\nThank You For Using This Tool !") 
		exit(0)
	else:
		print("\nInvalid Option")