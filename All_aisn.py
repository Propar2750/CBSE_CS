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
