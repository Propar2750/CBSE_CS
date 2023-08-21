def main():

    while True:
        try:
            encrypt_decrypt = int(input("Enter 1 to encrypt or 2 to decrypt: ") or 1)
            if encrypt_decrypt != 2 or encrypt_decrypt != 1:
                print("Enter a number which is either 1 or 2")
                continue
            rot = int(input("Enter the ROT(Rotate by places): ")or 13)
            rot = rot - 26*(rot//26)
            break
        except TypeError:
            print("Enter an number")
    
    string = list(input("Please enter the string: "))

    def encrypt(): 
        z = "z"
        if string(i).isupper():
            z = "Z"

        for i in range(len(string)):
            if ord(string[i]) <= ord(z) - rot:
                print(chr(ord(string[i] + rot)),end="")
            else:
                print(chr(ord()))
            

            
    def decrypt():
        pass

    if encrypt_decrypt == 1:
        encrypt()
    elif encrypt_decrypt == 2: 
        decrypt()
    

    
    

while True:
    main()
    while True:
        try:
            continue_not = int(input("Enter 1 to continue or 2 to discontinue") or 2)
            if continue_not == 2:
                break
        except TypeError:
            print("Enter an number")
            

    if continue_not != 1:
        continue
    else:
        break
