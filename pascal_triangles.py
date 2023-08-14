#Pascals Triangle


# Getting the values of the pascals triangle and storing them into the dictionary of storage
n = int(input("Number of lines: "))
storage = {}
for i in range(1,n+1):
    storage[i] = []
    for j in range(1,i+1):
        if j == 1 or j ==  i:
            storage[i].append(1)
        else:
            storage[i].append(storage[i-1][j-2]+storage[i-1][j-1])

# Properly printing the output
# To do later: Making it into an excel
for x in storage.values():
    for i in range(len(x)):
        if i == 0:
            print(" "*int(((2*n) - 1 - (len(x)*2)-1)/2),x[i],end = "")
        else:
            print(" ", x[i], end ="" )
    print()
