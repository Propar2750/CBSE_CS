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
    print(f'{numbers[0]} is the largest number \n{numbers[len(numbers) - 1]} is the smallest number')


""" Pattern 1:
    *
    **
    ***
    ****
    *****
"""


# Question 4: Generating Pattern 1


def pattern_1():
    number_of_lines = 1 + int(input("How many lines of this pattern do you want? "))
    for i in range(1, number_of_lines):
        print("*" * i)


""" Pattern 2:
    12345
    1234
    123
    12
    1
"""


# Question 5 : Generating Pattern 2


def pattern_2():
    number_of_lines = int(input("How many lines of this pattern do you want? "))
    for i in range(number_of_lines, 0, -1):
        for j in range(1, i + 1):
            print(j, end="")
        print()


""" 
    Pattern 3:
    A
    AB
    ABC
    ABCD
    ABCDE
"""


# Question 6 : Generating Pattern 3


def pattern_3():
    a = ord("A")
    number_of_lines = int(input("How many lines of this pattern do you want? "))
    for i in range(0, number_of_lines):
        for j in range(a, a + i + 1):
            print(chr(j), end="")
        print()


# Question 7 : Write a program to input the value of x and n and print the sum of (1 + 𝑥 + 𝑥² ..... + 𝑥ⁿ)
def sum_series_1():
    x = int(input("Enter the value of x: "))
    n = int(input("Enter the value of n: "))
    sum = 0
    for i in range(0, n):
        sum += x ** i
    print(sum)


# Question 8 : Write a program to input the value of x and n and print the sum of (1 - 𝑥 + 𝑥² ..... - 𝑥ⁿ)
def sum_series_2():
    x = int(input("Enter the value of x: "))
    n = int(input("Enter the value of n: "))
    sum = 0
    for i in range(0, n):
        if i % 2 == 0:
            sum += x ** i
        else:
            sum -= x ** i
    print(sum)


# Question 9 : Write a program to input the value of x and n and print the sum of (𝑥 + 𝑥²/2 ..... + 𝑥ⁿ/n)
def sum_series_3():
    x = int(input("Enter the value of x: "))
    n = int(input("Enter the value of n: "))
    sum = 0
    for i in range(1, n + 1):
        sum += (x ** i) / i
    print(sum)


# Question 10 : Write a program to input the value of x and n and print the sum of (𝑥 + 𝑥²/2! ..... + 𝑥ⁿ/n!)
def sum_series_4():
    x = int(input("Enter the value of x: "))
    n = int(input("Enter the value of n: "))
    sum = 0
    for i in range(1, n + 1):
        i_factorial = 1
        for j in range(1, i + 1):
            i_factorial = i_factorial * j
        sum += (x ** i) / i_factorial
    print(sum)


# Question 11 : Determining if a number is a perfect number
def perfect_number():
    number = int(input("Please enter the number: "))
    factors = []
    factor_sum = 0
    for i in range(1, (number // 2) + 1):
        if number % i == 0:
            factors.append(i)

    for factor in range(0, len(factors)):
        factor_sum += factors[factor]

    if factor_sum == number:
        print(f"{number} is a Perfect Number")
    else:
        print(f"{number} is not a Perfect Number")


# Question 12 : Determine if a number is armstrong number
def armstrong_number():
    number = int(input("Please enter the number: "))
    sum = 0
    for digit in str(number):
        sum += int(digit) ** 3

    if sum == number:
        print(f'{number} is a Armstrong number')
    else:
        print(f'{number} is not a Armstrong number')


# Question 13 : Determine if a number is palindrome number
def palindrome_number():
    number = input("Please enter the number: ")
    if number == number[::-1]:
        print(f"{number} is a palindrome number")
    else:
        print(f"{number} is not a palindrome number")


# Question 14 : Determine if a number is a prime number or composite number
def prime_check():
    number = int(input("Please enter the number: "))
    for i in range(2, (number // 2) + 1):
        if number % i == 0:
            print(f"{number} is a composite number")
            break
    else:
        print(f"{number} is a prime number")


# Question 15 : Display the terms of a Fibonacci series.
def fibonacci():
    n = int(input("How many terms of the fibonacci series? "))
    x = 1
    y = 0
    for i in range(0, n):
        sum = x + y
        print(f"{sum}, ", end="")
        x = y
        y = sum


# Question 16 : Compute the Greatest Common Divisor
def greatest_common_divisor():
    number_1 = int(input("Please enter the number 1: "))
    number_2 = int(input("Please enter the number 2: "))

    def gcd(smaller_num):
        for i in range((smaller_num // 2) + 1, 0, -1):
            if number_1 % i == 0 and number_2 % i == 0:
                print(f"{i} is the greatest common divisor")
                break

    if number_1 > number_2:
        gcd(number_2)
    else:
        gcd(number_1)


# Question 17 : Compute the least common multiple of two integers
def lcm():
    number_1 = int(input("Please enter the number 1: "))
    number_2 = int(input("Please enter the number 2: "))

    def factors(factor_list, n):

        # Print the number of two's that divide n
        while n % 2 == 0:
            factor_list.append(2)
            n = n / 2

        # n must be odd at this point
        # so a skip of 2 ( i = i + 2) can be used
        for a in range(3, int(n ** 1 / 2) + 1, 2):

            # while i divides n , print i and divide n
            while n % a == 0:
                factor_list.append(a)
                n = n / a

        # Condition if n is a prime
        # number greater than 2
        if n > 2:
            factor_list.append(n)

    factors_1 = []
    factors_2 = []
    factors(factors_1, number_1)
    factors(factors_2, number_2)

    common_factors = []
    uncommon_factors = []
    for i in range(0, len(factors_1)):
        if factors_1[i] in factors_2:
            common_factors.append(factors_1[i])
        else:
            uncommon_factors.append(factors_1[i])
    for i in range(0, len(factors_2)):
        if factors_2[i] in factors_1:
            continue
        else:
            uncommon_factors.append(factors_2[i])

    x = 1
    for i in range(0, len(common_factors)):
        x = x * common_factors[i]
    for i in range(0, len(uncommon_factors)):
        x = x * uncommon_factors[i]

    print(x)


# Question 18 : Count and display the number of vowels
def n_vowels():
    n = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    text = list(input("Please enter the text: "))
    for i in range(0, len(text)):
        if text[i].lower() in vowels:
            n += 1
    print(f'There are {n} vowels in this text')


# Question 19 : Count and display the number of consonants
def n_consonants():
    n = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    text = list(input("Please enter the text: "))
    for i in range(0, len(text)):
        if text[i].lower() not in vowels:
            n += 1
    print(f'There are {n} consonants in this text')


# Question 19 : Count and display the number of Upper Case and lower case characters
def n_upper_lower_case():
    n_lower = 0
    n_upper = 0
    text = list(input("Please enter the text: "))

    for i in range(0, len(text)):
        if text[i].islower():
            n_lower += 1
        elif text[i].isupper():
            n_upper += 1
    print(f'There are {n_lower} lowercase characters \nThere are {n_upper} upper case characters')


# Question 20 : Input a string and determine whether it is a palindrome or not
def palindrome_str():
    text = input("Please enter the text: ")
    if text == text[::-1]:
        print(f"{text} is a palindrome string")
    else:
        print(f"{text} is not a palindrome string")


# Question 21 : convert the case of characters in a string.
def case_conversion():
    text = list(input("Please enter the text: "))
    final_text = ""
    for i in range(0,len(text)):
        if text[i].isupper():
            final_text = final_text + text[i].lower()
        elif text[i].islower():
            final_text = final_text + text[i].upper()
    print(final_text)


# Question 22 : Find the largest/smallest number in a list/tuple
def largest_number_list():
    print("To stop the entering process , send any character")
    numbers = []
    while True:
        try:
            numbers.append(int(input("Please enter the number: ")))
        except ValueError:
            break
    numbers.sort()
    print(f'{numbers[0]} is the smallest numbers \n{numbers[len(numbers)-1]} is the biggest number')

