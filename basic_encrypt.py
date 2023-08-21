def basic_encrypt():
    string = list(input("Enter the string you want to encrypt: "))
    for i in range(len(string)):
        print(chr(ord(string[i])+ 3),end="")

            

def basic_decrypt():
    string = list(input("Enter the string you want to decrypt: "))
    for i in range(len(string)):
        print(chr(ord(string[i])- 3),end="")

