sentence = list(input("Enter the sentence: ").replace(" ",""))
score = {}
for i in range(len(sentence)):
    try:
        a = score[sentence[i]]
    except KeyError:
        score[sentence[i]] =  1
    else:
        score[sentence[i]] = score[sentence[i]] + 1
x = sorted(score.items(), key=lambda kv:
                 (kv[1]))
x = x[len(x)-1]
print(x)
