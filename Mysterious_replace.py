def transpose_2(text):
    alt_text = []
    
    for i in range(0,len(text)):
        #print(i)
        for j in range(0,len(text[i])):
            #print(text[i][j])
            alt_text[j][i] = text[i][j]
            #print(alt_text[j][i])
            
    print(alt_text)
