import string
import random

def rec_mess(cipherText_dec, key):
	print("\nDecryption")
	
	print("Message Received: ",cipherText_dec) 
	plainText_dec = ''
	
	for i in range(len(key)):
		cip_asc_dec = ord(cipherText_dec[i])-65
		key_asc_dec = ord(key[i])-65
		plainText_dec += chr(((cip_asc_dec-key_asc_dec) % 26)+65)
	print("Decrypted Message: ",plainText_dec)
	print()

no_mess = int(input("Enter No Of Messages To Be Sent: "))

def sen_mess():

	for i in range(no_mess): 
		cipherText = ''
		plainText = list((input("\nEnter Your Plain Text: ").upper()).replace(" ", "")) 
		key = [i for i in string.ascii_uppercase]
		random.shuffle(key)
		key = key[0:len(plainText)]
		
		print("\nEncryption")
		print("Plain Text = ", end="")
		print(''.join(map(str, plainText)))
		print("Key = ", end="")
		print(''.join(map(str, key)))

		for i in range(len(plainText)):
			pla_asc = ord(plainText[i])-65
			key_asc = ord(key[i])-65
			cipherText += chr(((pla_asc+key_asc) % 26)+65)
		
		rec_mess(cipherText, key)

sen_mess()