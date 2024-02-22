N = int(input("enter number of lines"))
print("Give input in form of 1 4 5 ...N terms")
matrix = []
for i in range(1,N+1):
    line = input(f"Enter the {i} list").split()
    line = [int(x) for x in line]
    matrix.append(line)

sum = 0
for i in range(0,N):
    
    for j in range(0,N-i):
        sum+= matrix[i][N-j-1]
        print(matrix[i][N-j-1])
print(matrix,sum)       
