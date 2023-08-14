# Pascals Triangle

# Getting all the values of the pascals triangle for n lines in storage
n = int(input("Number of lines: "))
storage = {}
for i in range(1,n+1):
    storage[i] = []
    for j in range(1,i+1):
        if j == 1 or j ==  i:
            storage[i].append(1)
        else:
            x = storage[i-1][j-2]+storage[i-1][j-1]
            storage[i].append(x)


# formatting the answer
total_len = (2*n) - 1

for x in storage.values():
    spaces = int(total_len - (len(x)*2)-1)/2
    spaces = int(spaces) # Was otherwise giving errors sometimes
    for i in range(len(x)):
        if i == 0:
            print(" "*spaces,x[i],end = "")
        else:
            print(" ", x[i], end ="" )
    print()
