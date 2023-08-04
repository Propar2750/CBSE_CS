# If you ever need to confirm the user is entering the correct type of input
def format_check(variable, input_text, type_of_input):
    while True:
        try:
            variable = type_of_input(input(input_text))
        except Exception:
            pass
        return variable
        break


# Question 1 : Input a welcome message and display it.
def welcome():
    msg = input("What would you like the welcome message to be? ")
    print(msg)
    
# Question 2: Input two numbers and display the larger / smaller number.
def larger_smaller_2():
    n_1 = int(input("Enter the first number: "))
    n_2 = int(input("Enter the second number: "))
    if n_1 > n_2: 
        print(f'{n_1} is greater than {n_2}')
    elif n_2 > n_1:
        print(f'{n_2} is greater than {n_1}')
    else:
        print(f'{n_2} is equal to {n_1}')

# Question 3: Input three numbers and display the largest / smallest number
def larger_smaller_n():
    numbers = []
    while True:
        x = input("Enter the number or enter 'break' to break: ")
        if x == 'break':
            break
        else:
            numbers.append(int(x))
            print(numbers)
            
    print(numbers)
    print(f'{numbers[0]} is the largest number \n{numbers[len(numbers)-1]} is the smallest number')
larger_smaller_n()
