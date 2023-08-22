"""
This is a menu based program.
Input are taken in 1, 2 , 3... so that the choice can be executed easily and affectively
"""


# The encryption logic
def encrypt(chars: list, rotate: int):
    # Looping for all characters in the string
    for i in range(len(chars)):

        chars[i] = str(chars[i])
        # Checks if the character is lower or upper case so that the output letter is in the same case using the
        # ordinal of the uppercase letter or the lowercase letter
        if chars[i].isupper():
            z = "Z"
            dif = 26
            rotate = rotate - 26*(rotate // 26)

        elif chars[i].islower():
            z = 'z'
            dif = 26
            rotate = rotate - 26*(rotate // 26)

        # For all the characters
        elif ord('a') > ord(chars[i]) > ord('Z'):
            z = chr(ord('a') - 1)
            dif = (ord('a') -ord('Z'))

        elif ord('z') < ord(chars[i]):
            z = chr(127)
            dif = 127 - ord('z')

        elif ord(chars[i]) < ord('A'):
            z = chr(ord('A') - 1)
            dif = ord('A')

        rotate = rotate - dif*(rotate // dif)

        # If the ordinal of the character is less than the amount it needs to be rotated by
        # That is, the amount it has to be rotated by can just be added
        if ord(chars[i]) <= ord(z) - rotate:
            print(chr(ord(chars[i]) + rotate), end="")

        # If the ordinal of the character is more than the amount it needs to be rotated by
        # That is, the amount it has to be rotated by can't just be added and hence 26 is also subtracted
        elif ord(chars[i]) > ord(z) - rotate:
            print(chr(ord(chars[i]) + rotate - dif), end="")

    # An empty line is printed so that the next prompt isn't in the same line
    print("\n")


# The decryption logic
def decrypt(chars: list, rotate: int):
    # Looping for all characters in the string
    for i in range(len(chars)):

        # Checks if the character is lower or upper case so that the output letter is in the same case using the
        # ordinal of the uppercase letter or the lowercase letter
        if chars[i].isupper():
            a = "A"
            dif = 26

        elif chars[i].islower():
            a = 'a'
            dif = 26

        elif ord('a') > ord(chars[i]) > ord('Z'):
            a = chr(ord('Z') + 1)
            dif = ord('a') -ord('Z')

        elif ord('z') < ord(chars[i]):
            a = chr(ord('z') + 1)
            dif = 127 - ord('z')

        elif ord(chars[i]) < ord('A'):
            a = chr(0)
            dif = ord('A')

        rotate = rotate - dif*(rotate // dif)

        # If the ordinal of the character is greater than the amount it needs to be rotated by
        # That is, the amount it has to be rotated by can just be subtracted
        if ord(chars[i]) >= ord(a) + rotate:
            print(chr(ord(chars[i]) - rotate), end="")

        # If the ordinal of the character is less than the amount it needs to be rotated by
        # That is, the amount it has to be rotated by can't just be subtracted and hence 26 is also added
        elif ord(chars[i]) < ord(a) + rotate:
            print(chr(ord(chars[i]) - rotate + 26), end="")

    # An empty line is printed so that the next prompt isn't in the same line
    print("\n")


def logic():
    # There is a loop till the user enters a 1 or 2 or nothing for the first choice.
    while True:

        # The code doesnt give an error even when an number is not entered. It instead asks to re enter
        try:

            # Getting to know whether to encrypt or decrypt
            encrypt_decrypt = int(input("Enter 1 to encrypt or 2 to decrypt: ") or 1)

            # If the user chose an option that is not in the option
            if encrypt_decrypt != 1 and encrypt_decrypt != 2:
                print("Enter a number which is either 1 or 2")
                continue

            # When the value is successfully received and stored it breaks the loop
            break

        # When we do get an error this will be the error prompt
        except TypeError or ValueError:
            print("Enter an number")

    # Loop till user enters a valid integer
    while True:

        # The code doesnt give an error even when an number is not entered. It instead asks to re enter
        try:
            rot = int(input("Enter the ROT(Rotate by places): ") or 13)

            # It breaks if value is received without any error
            break

        # If there is an error it re-prompts the user to enter
        except ValueError:
            print("Enter an Number")

    # The string which will be encrypted or decrypted
    string = list(input("Please enter the string: "))

    # Executes the encryption / decryption
    if encrypt_decrypt == 1:
        encrypt(string,rot)
    elif encrypt_decrypt == 2:
        decrypt(string,rot)


# Executes the code in a loop asking for whether to continue or not after each loop
def cipher():
    while True:
        try:
            logic()
            continue_not = int(input("Enter 1 to continue or 2 to discontinue") or 2)
            if continue_not == 2:
                break
        except TypeError:
            print("Enter an number")


cipher()
