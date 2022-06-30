import string
import time

def caes_encrypt():
	
	cipherText = ""
	text = input("Enter Plain Text: ")
	shft = int(input("Enter Key: "))

	for i in range(len(text)):
		
		char = text[i]
		if (char.isupper()):
			cipherText += chr((ord(char)-65 + shft) % 26 + 65)
		else:
			cipherText += chr((ord(char)-97 + shft) % 26 + 97)
		
	print("\nCipher Text :", cipherText)

def caes_decrypt():

	alpha_dict = [i for i in string.ascii_uppercase] 
	
	print("\n1. Decrypt Using BruteForce")
	print("2. Decrypt Using Key")
	cho_dec=int(input("Enter Your Choice: "))
	
	if cho_dec==1:

		cipherText = input("\nEnter Cipher Text: ")
		print("\nApplying Brute Force in Cipher Text\n")
		time.sleep(2)

		for i in range(0, 26):
			plainText = ''
			for j in cipherText:
				letterIndex = (ord(j.upper()) - 65 - i) % 26
				if j.islower():
					plainText += alpha_dict[letterIndex].lower()
				else:
					plainText += alpha_dict[letterIndex]
			print("Key:",i,"-> Plain-Text:",plainText)

	elif cho_dec==2:

		plainText = ""
		cipherText = input("\nEnter Cipher Text: ")
		shft = int(input("Enter Key: "))

		for i in range(len(cipherText)):
		
			char = cipherText[i]
		
			if (char.isupper()):
				plainText += chr((ord(char)-65 - shft) % 26 + 65)
			else:
				plainText += chr((ord(char)-97 - shft) % 26 + 97)
		
		print("\nPlain Text :", plainText)

	else:
		print("\nInvalid Choice")


while True:
	print("\n----- Caesar Cipher Algorithm -----") 
	print("1. Encrypt Text")
	print("2. Decrypt Text")
	print("3. Exit")
	ch = int(input("\nEnter Your Choice: "))
	
	if ch == 1:
		caes_encrypt()
	elif ch == 2:
		caes_decrypt()
	elif ch == 3:
		print("\nThank You For Using This Tool !") 
		exit(0)
	else:
		print("\nInvalid Option")