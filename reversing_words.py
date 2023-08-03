# Reversing words in a sentence
sentence = input("Enter the sentence: ").split()
final_sentence = ""
for i in range(0,len(sentence)):
    final_sentence = final_sentence + " " + (sentence[i][::-1])
print(final_sentence)
