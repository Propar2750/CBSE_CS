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
