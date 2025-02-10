from collections import OrderedDict

def set_digrams():
    i = 0
    while i != len(text_list):
        if i == (len(text_list) - (len(text_list) % 2)) and len(text_list) % 2 != 0:
            text_list.append('x')
            break
        if text_list[i] == text_list[i + 1]:
            text_list.insert(i + 1, 'x')
        i += 2


def generate_matrix():
    matrix_alphabet_list.extend(key_formatted)

    ascii_index = 0

    while len(matrix_alphabet_list) != 25:
        letter = chr(97 + ascii_index)
        if letter not in matrix_alphabet_list:
            if letter != 'j':
                matrix_alphabet_list.append(letter)
        ascii_index += 1

    for i in range(0, len(matrix_alphabet_list), 5):
        matrix_pf.append(matrix_alphabet_list[i:i + 5])

    print("\nMatrix: ")
    for i in matrix_pf:
        print(i, end="\n")



def get_position(letter):
    for index_row, row in enumerate(matrix_pf):
        for index_col, col in enumerate(row):
            if col == letter:
                return index_row, index_col


def cipher():
    for i in range(0, len(text_list) - 1, 2):
        index_row_first, index_col_first = get_position(text_list[i])
        index_row_second, index_col_second = get_position(text_list[i + 1])

        # Same Row
        if index_row_first == index_row_second:
            index_col_first = (index_col_first + 1) % 5
            index_col_second = (index_col_second + 1) % 5
            cipher_text.extend(matrix_pf[index_row_first][index_col_first])
            cipher_text.extend(matrix_pf[index_row_second][index_col_second])

        # Same Column
        elif index_col_first == index_col_second:
            index_row_first = (index_row_first + 1) % 5
            index_row_second = (index_row_second + 1) % 5
            cipher_text.extend(matrix_pf[index_row_first][index_col_first])
            cipher_text.extend(matrix_pf[index_row_second][index_col_second])

        # Different Row and Column
        else:
            cipher_text.extend(matrix_pf[index_row_first][index_col_second])
            cipher_text.extend(matrix_pf[index_row_second][index_col_first])

    print("\nCipher Text: ", "".join(cipher_text))


def decipher():
    for i in range(0, len(text_list) - 1, 2):
        index_row_first, index_col_first = get_position(text_list[i])
        index_row_second, index_col_second = get_position(text_list[i + 1])

        # Same Row
        if index_row_first == index_row_second:
            index_col_first = (index_col_first - 1) % 5
            index_col_second = (index_col_second - 1) % 5
            cipher_text.extend(matrix_pf[index_row_first][index_col_first])
            cipher_text.extend(matrix_pf[index_row_second][index_col_second])

        # Same Column
        elif index_col_first == index_col_second:
            index_row_first = (index_row_first - 1) % 5
            index_row_second = (index_row_second - 1) % 5
            cipher_text.extend(matrix_pf[index_row_first][index_col_first])
            cipher_text.extend(matrix_pf[index_row_second][index_col_second])

        # Different Row and Column
        else:
            cipher_text.extend(matrix_pf[index_row_first][index_col_second])
            cipher_text.extend(matrix_pf[index_row_second][index_col_first])

    print("\nPlain Text: ", "".join(cipher_text))


def format_inputs(text, key):
    text = text.replace(" ", "").lower()
    text = text.replace("j", "i")
    text = list(text)
    key = key.replace(" ", "").lower()
    key = key.replace("j", "i")
    key = "".join(OrderedDict.fromkeys(key))
    return text, key


def encrypt():
    plainText = input("\nEnter Plain Text: ")
    key = input("Enter Key: ")

    global key_formatted, text_list
    text_list, key_formatted = format_inputs(plainText, key)

    set_digrams()
    generate_matrix()
    cipher()



def decrypt():
    cipherText = input("\nEnter Cipher Text: ")
    key = input("Enter Key: ")

    global key_formatted, text_list
    text_list, key_formatted = format_inputs(cipherText, key)

    set_digrams()
    generate_matrix()
    decipher()



def display_menu():
    print("\nMenu: ")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Exit")

    choice = input("\nEnter Choice: ")

    if choice == '1':
        encrypt()
    elif choice == '2':
        decrypt()
    elif choice == '3':
        exit()
    else:
        print("Invalid Choice")
        display_menu()



key_formatted = []
text_list = []
matrix_pf = []
matrix_alphabet_list = []
cipher_text = []


display_menu()