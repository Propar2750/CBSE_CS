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
