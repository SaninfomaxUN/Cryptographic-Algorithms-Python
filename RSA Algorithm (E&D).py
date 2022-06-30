import math

cipherTextNum = []
plainTextNum = []
ListOfPrimeNum = []
cipherText=''
plainText=''

p = int(input("Enter Value of P: "))
q = int(input("Enter Value of Q: "))
message = input("Enter Message: ").upper()

n = p*q
print("\np =", p) 
print("q =", q) 
print(f"\nn = p * q = {p} * {q} = {n}") 
print()

EulerFunc = (p-1) * (q-1)
print(f"f = (p-1) * (q-1) = {p-1} * {q-1} = {EulerFunc}") 
print("\nEular's Totient Function (f): ",EulerFunc)

for x in range(1,EulerFunc+1):
	FoundGcd = math.gcd(x,EulerFunc)
	if FoundGcd == 1:
		ListOfPrimeNum.append(x)

try:
	e = ListOfPrimeNum[2]
except:
	print("\nPrime Number Error !")
	exit(0)

print(f"\nFind e Such That GCD({EulerFunc},e) = 1") 
print(f"GCD({EulerFunc},{e}) = 1") 
print("Hence e =", e) 

count = 0
while True:
	d = (1+(count*EulerFunc))/e
	if d.is_integer():
		break
	else:
		count += 1

pu = [e, n] 
pr = [int(d), n]

print(f"\nFind d Such That d * {e} % {EulerFunc} = 1") 
print(f"{int(d)} * {e} % {EulerFunc} = 1") 
print("Hence d =", int(d))
print("\nHence") 
print(f"PU = [e,n] = {pu}") 
print(f"PR = [d,n] = {pr}")

for y in range(0,len(message)):
	ConOrd = ord(message[y]) - 64
	Encryption = ConOrd ** e % n
	cipherTextNum.append(Encryption)

for z in range(0,len(cipherTextNum)):
	ConChr = chr(cipherTextNum[z]+64)
	cipherText+=ConChr

print("\nEncryption")
print("Encrypted Text: ",cipherText)
print()

for y in range(0,len(cipherText)):
	ConOrd_Dec = ord(cipherText[y]) - 64
	Encryption = ConOrd_Dec ** int(d) % n
	plainTextNum.append(Encryption)

for z in range(0,len(plainTextNum)):
	ConCh__Decr = chr(plainTextNum[z]+64)
	plainText+=ConCh__Decr

print("\nDecryption")
print("Plain Text: ",plainText)
print()