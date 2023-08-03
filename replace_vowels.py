sentence = input("Enter the sentence: ")
vowels = ['a','e','i','o','u']
for i in range(0,4):
    sentence = sentence.replace(vowels[i],"*")
    sentence = sentence.replace(vowels[i].upper(),"*")
print(sentence)
