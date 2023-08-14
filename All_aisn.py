# Question 1 : WAP to calculate the area and circumference of a circle if radius is given
def area_circumference_circle():
    radius = int(input("Please enter the radius: "))
    print(f'Area is {3.14*radius*radius}, circumference is {2*3.14*radius}')


# Question 2 : WAP to make a simple calculator that reads two numbers and an operator. On selection of an operator, perform operation and print the result
def basic_calculator():
    n_1 = int(input("Enter the number 1: "))
    n_2 = int(input("Enter the number 2: "))
    operator = input("Please enter the operation you want to do: ")
    if operator == "*" or operator == "x":
        result = n_1*n_2
    elif operator == "/":
        result = n_1/n_2
    elif operator == "-":
        result = n_1-n_2
    elif operator == "+":
        result = n_1+n_2
    else: 
        print("Enter a valid operator next time")
    print(f'{n_1} {operator} {n_2} = {result}')


# Question 3 : You are driving a little too fast and the police officer stops you and issues a ticker. Write code to compute the result encoded as an integer value: 0 = no ticket, 1 = small ticket and 2= big ticket.
# If speed is 60 or less, the result is 0. If speed is between 61 and 80 inclusive, the result is 1. If speed is 81 or more, the result is 2. Unless its your birthday, on that day, your speed can be 5 higher in all cases. WAP to model the above scenario
def speeding_ticket():
    speed = int(input("Please enter the speed: "))
    bday = input("Was it his/her bday today(y/n): ")
    ticket = 0 
    if bday.startswith("y"):
        speed = speed - 5
    elif bday.startswith("n"):
        pass
    else:
        print("Please enter yes or no for whether it was the drivers birthday or not")
    
    if speed < 60:
        pass
    elif 80 <= speed >= 60:
        ticket = 1
    elif speed >= 81:
        ticket = 2
    
    if ticket == 0:
        print("no ticket")
    elif ticket == 1:
        print("Small ticket")
    elif ticket == 2:
        print("Big ticket")


""" Pattern 1:
    *
    **
    ***
    ****
    *****
"""


# Question 4(i): Generating Pattern 1
def pattern_1():
    number_of_lines = 1 + int(input("How many lines of this pattern do you want? "))
    for i in range(1, number_of_lines):
        print("*" * i)


'''
Pattern 2:
    *
   **
  ***
 ****
*****
'''


# Question 4(ii): Generating pattern 2
def pattern_2():
    number_of_lines =1 +int(input("How many lines of this pattern do you want? "))
    for i in range(number_of_lines-1, 0,-1):
        print(" " * i, "*"*(number_of_lines-i))
        

# Question 5: WAP that reads n digit number, After reading the number, compute and display the sum of the odd oppositioned digits, multiply all even positioned digits and add these two number
def question_5():
    n = list(input("Enter number: "))
    Sum = 0
    Product = 1
    for i in range(len(n)):
        if i % 2 == 0:
            Sum += int(n[i])
        else:
            Product *= int(n[i])
    print(Sum+Product)


# Question 6: Write a program which will find all such numbers which are divisible by 7 and are not multiple of 5, between
def question_6():
    for i in range(2000,3201):
        if i%7==0 and i%5 != 0:
            print(i,end=", ")


# Question 7: Develop a program to classify students amongst various categories as per their age entered. Read age if B students and count no if students falling in each category as described below print a report as follows-
'''
Group A :  12yrs and above but less than 15 yrs -XX
Group B :  15yrs and above but less than 17 yrs -XX
Group C :  17yrs and above but less than 19 yrs -XX
Group D :  Lesser than 12 yrs
'''
def question_7():
    N = int(input("Number of students? "))
    below_12 = 0
    above_12 = 0
    above_15 = 0
    above_17 = 0
    for i in range(1,N+1):
        age = float(input(f"Enter the age of student {i}: "))
        if age <12:
            below_12 +=1
        elif 12<=age<15:
            above_12+=1
        elif 15<=age<17:
            above_15+=1
        elif 17 <= age < 19:
            above_17 +=1
        print(f"Group A :  12yrs and above but less than 15 yrs - {above_12}\n",
              f"Group B :  15yrs and above but less than 17 yrs - {above_15}\n",
              f"Group C :  17yrs and above but less than 19 yrs - {above_17}\n",
              f"Group D : Lesser than 12 yrs - {below_12}")


# Question 8 : WAP to find if a number entered is a palindrome or not
def palindrome_number():
    number = input("Please enter the number: ")
    if number == number[::-1]:
        print(f"{number} is a palindrome number")
    else:
        print(f"{number} is not a palindrome number")


#Question 9 : According to a study, the approzimate level of intelligence of a person can be caluclated using the following formula i =2(y+05.x). Write a program, which produces a table of values of i, y and x . Where y varies from 1 to 6 and for each value of y, x varies from 5.5 to 12.5 in steps of 0.5
def question_9():
    output = {}
    for y in range(1,7):
        for x in range(55, 130,5):
            l=x/10
            i = 2*(y+(0.5*l))
            output[i]=[l,y]
    print(output)


# Question 10(A) : WAP to print the result of the sequence x + x^2/2 + x^3/3 ... x^n/n
def question_10A():
    x = int(input("Enter value of x: "))
    n = int(input("Enter value of n: "))
    sum = 0
    for i in range(1,n+1):
        sum+= (x**n)/n
    print(sum)


# Question 10(B) : WAP to print the result of the sequence 1/sqrt(2) + 2/sqrt(3) ... n/(sqrt(n+1))
def question_10B():
    n = int(input("Enter value of n: "))
    sum = 0
    for i in range(1,n+1):
        sum+= n/(n**1/2)
    print(sum)
