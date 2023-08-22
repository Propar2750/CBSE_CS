"""
This is a menu based program.
Input are taken in 1, 2 , 3... so that the choice can be executed easily and affectively
"""


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
            rot = rot - 26 * (rot // 26)

            # It breaks if value is received without any error
            break

        # If there is an error it re-prompts the user to enter
        except ValueError:
            print("Enter an Number")

    # The string which will be encrypted or decrypted
    string = list(input("Please enter the string: "))

    # The encryption logic
    def encrypt():

        # Looping for all characters in the string
        for i in range(len(string)):

            # Checks if the character is lower or upper case so that the output letter is in the same case using the
            # ordinal of the uppercase letter or the lowercase letter
            if string[i].isupper():
                z = "Z"
            elif string[i].islower():
                z = 'z'

            # If the ordinal of the character is less than the amount it needs to be rotated by
            # That is, the amount it has to be rotated by can just be added
            if ord(string[i]) <= ord(z) - rot:
                print(chr(ord(string[i]) + rot), end="")

            # If the ordinal of the character is more than the amount it needs to be rotated by
            # That is, the amount it has to be rotated by can't just be added and hence 26 is also subtracted
            elif ord(string[i]) > ord(z) - rot:
                print(chr(ord(string[i]) + rot - 26), end="")

        # An empty line is printed so that the next prompt isn't in the same line
        print("\n")

    # The decryption logic
    def decrypt():

        # Looping for all characters in the string
        for i in range(len(string)):

            # Checks if the character is lower or upper case so that the output letter is in the same case using the
            # ordinal of the uppercase letter or the lowercase letter
            if string[i].isupper():
                a = "A"
            elif string[i].islower():
                a = 'a'

            # If the ordinal of the character is greater than the amount it needs to be rotated by
            # That is, the amount it has to be rotated by can just be subtracted
            if ord(string[i]) >= ord(a) + rot:
                print(chr(ord(string[i]) - rot), end="")

            # If the ordinal of the character is less than the amount it needs to be rotated by
            # That is, the amount it has to be rotated by can't just be subtracted and hence 26 is also added
            elif ord(string[i]) < ord(a) + rot:
                print(chr(ord(string[i]) - rot + 26), end="")

        # An empty line is printed so that the next prompt isn't in the same line
        print("\n")

    # Executes the encryption / decryption
    if encrypt_decrypt == 1:
        encrypt()
    elif encrypt_decrypt == 2:
        decrypt()


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
