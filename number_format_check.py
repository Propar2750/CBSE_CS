sentence = list(input("Enter the phone number: ").replace(" ",""))
check = False
if sentence[3] == '-' and sentence[7] == '-' and len(sentence) == 12:
        check = True
print(check)
