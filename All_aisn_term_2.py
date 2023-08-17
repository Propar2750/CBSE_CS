# Question 1 : WAP to take input 2 strings and check if string 1 is a prefix, postfix, or nothing from string 2
string_1 = input("Enter string 1: ").strip()
string_2 = input("Enter string 2: ").strip()
print(string_2.find(string_1))
if string_2[string_2.find(string_1)] == string_2[len(string_2)- len(string_1)]:
    print(f"{string_1} is a postfix of {string_2}")
elif string_2[string_2.find(string_1)] == string_2[len(string_1)]:
    print(f"{string_2} is a prefix of {string_2}")
else: 
    print('Nothing')
