sentence = list(input("Enter the sentence: ").replace(" ",""))
score = {}
sum_s = 0
for i in range(len(sentence)):
    try:
        a = score[sentence[i]]
    except KeyError:
        score[sentence[i]] =  1
    else:
        score[sentence[i]] = score[sentence[i]] + 1
for i in range(0,10):
    try:
        sum_s = sum_s + int(score[f'{i}'])*i
    except KeyError:
        pass
print(sum_s)
