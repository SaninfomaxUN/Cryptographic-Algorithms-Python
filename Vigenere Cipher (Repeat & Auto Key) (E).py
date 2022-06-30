def Print_Vigenere_Table(Vig_Ma_Fn):
	for rows in Vig_Ma_Fn: 
		print(rows)

def Vigenere_Table_Repeated_Mode(plainText_fn,key_fn):

	vig_tab_matr = []
	for i in range(26):
		tmp_lis = []
		for j in range(26):
			tmp_val = i+j+65
			if tmp_val <= 90:
				tmp_lis.append(chr(tmp_val)) 
			else: 
				tmp_val = (tmp_val % 65) + 39
				tmp_lis.append(chr(tmp_val)) 
		vig_tab_matr.append(tmp_lis)

	Print_Vigenere_Table(vig_tab_matr)

	inc_ky_rep=0
	cipherText = ''
	
	while len(key_fn) < len(plainText_fn):
		key_fn.append(key_fn[inc_ky_rep])
		inc_ky_rep= (inc_ky_rep+1)% len(key_fn)
	
	print("\nKey: ",key_fn)
	
	for i in range(len(plainText_fn)):
		pla_asc = ord(plainText_fn[i])-65
		key_asc = ord(key_fn[i])-65
		cipherText += vig_tab_matr[key_asc][pla_asc] 
	
	print("\nCipher Text:", cipherText)


def Vigenere_Table_Auto_Mode(plainText_fn,key_fn):
	
	dict1 = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4,
	'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9,
	'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14,
	'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19,
	'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25}

	dict2 = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E',
	5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J',
	10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O',
	15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T',
	20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 25: 'Z'}

	inc_ky_auto=0

	while True:
		if len(key_fn) == len(plainText_fn):
			break
		elif plainText_fn[inc_ky_auto] == ' ':
			inc_ky_auto += 1
		else:
			key_fn += plainText_fn[inc_ky_auto]
			inc_ky_auto += 1

	print("\nKey: ",key_fn)

	cipherText = ''
	inc_pla_auto = 0
	for letter in plainText_fn:
		if letter == ' ':
			cipherText += ' '
		else:
			x = (dict1[letter]+dict1[key_fn[inc_pla_auto]]) % 26
			inc_pla_auto += 1
			cipherText += dict2[x]
	print("\nCipher Text:", cipherText)

while True:
	
	print("\n------------Vigenere Cipher------------")
	print("1. Vigenere Cipher Using Repeated-Mode")
	print("2. Vigenere Cipher Using Auto-Key")
	print("3. Exit")
	cho_ky=int(input("Enter Choice: "))

	if cho_ky==1:
		plainText = list((input("\nEnter Your Plain Text: ").upper()).replace(" ", "")) 
		key = list((input("Enter Your Key: ").upper()).replace(" ", "")) 
		Vigenere_Table_Repeated_Mode(plainText,key)

	elif cho_ky==2:
		plainText = list((input("\nEnter Your Plain Text: ").upper()).replace(" ", "")) 
		key = list((input("Enter Your Key: ").upper()).replace(" ", "")) 
		Vigenere_Table_Auto_Mode(plainText,key)

	elif cho_ky==3:
		exit(0)

	else:
		print("Invalid Choice")