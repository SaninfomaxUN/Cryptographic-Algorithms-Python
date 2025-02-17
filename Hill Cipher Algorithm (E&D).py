import numpy as np


# Función para convertir texto a matriz de números
def text_to_matrix(text, size):
    text = text.upper().replace(" ", "")
    while len(text) % size != 0:
        text += 'X'  # Relleno con 'X' si es necesario
    matrix = []
    for i in range(0, len(text), size):
        block = [ord(char) - ord('A') for char in text[i:i + size]]
        matrix.append(block)
    return np.array(matrix)


# Función para convertir matriz de números a texto
def matrix_to_text(matrix):
    text = ""
    for row in matrix:
        for num in row:
            text += chr(num % 26 + ord('A'))
    return text


# Función para encriptar
def encrypt_hill(plaintext, key):
    size = len(key)
    plaintext_matrix = text_to_matrix(plaintext, size)
    key_matrix = np.array(key)
    ciphertext_matrix = np.dot(plaintext_matrix, key_matrix) % 26
    return matrix_to_text(ciphertext_matrix)


# Función para desencriptar
def decrypt_hill(ciphertext, key):
    size = len(key)
    ciphertext_matrix = text_to_matrix(ciphertext, size)
    key_matrix = np.array(key)
    det = int(np.round(np.linalg.det(key_matrix)))  # Determinante de la matriz clave
    det_inv = pow(det, -1, 26)  # Inverso modular del determinante
    adjugate = (det_inv * np.round(det * np.linalg.inv(key_matrix)).astype(int)) % 26
    plaintext_matrix = np.dot(ciphertext_matrix, adjugate) % 26
    return matrix_to_text(plaintext_matrix)


def get_key_matrix(key_text):
    key = [ord(char.upper()) - ord('A') for char in key_text]
    size = int(len(key) ** 0.5)
    key = np.array(key).reshape(size, size)
    return key


# Función principal
def main():
    option = input("Seleccione la opción (E para encriptar, D para desencriptar): ").upper()
    if option == 'E':
        plaintext = input("Ingrese el mensaje a encriptar: ")
        key_text = input("Ingrese la clave como texto: ")
        key = get_key_matrix(key_text)

        ciphertext = encrypt_hill(plaintext, key)
        print("--------------------------------------------------")
        print("Texto cifrado: ", ciphertext)
        print("--------------------------------------------------")

    elif option == 'D':
        ciphertext = input("Ingrese el texto cifrado: ")
        key_text = input("Ingrese la clave como texto: ")
        key = get_key_matrix(key_text)

        plaintext = decrypt_hill(ciphertext, key)
        print("--------------------------------------------------")
        print("Texto descifrado: ", plaintext)
        print("--------------------------------------------------")

    else:
        print("Opción no válida.")

    print("\n\n")


if __name__ == "__main__":
    while True:
        main()
