# Question 1 : WAP to calculate the area and circumference of a circle if radius is given
def area_circumference_circle():
    radius = float(input("Please enter the radius: "))
    print(f'Area is {3.14*radius*radius}, circumference is {2*3.14*radius}')
''' 
OUTPUT:

Please enter the radius: 6.5
Area is 132.665, circumference is 40.82

'''

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
'''
OUTPUT:

Enter the number 1: 7
Enter the number 2: 3
Please enter the operation you want to do: *
7 * 3 = 21

'''

# Question 3 : You are driving a little too fast and the police officer stops you and issues a ticker. Write code to compute the result encoded as an integer value: 0 = no ticket, 1 = small ticket and 2= big ticket.
# If speed is 60 or less, the result is 0. If speed is between 61 and 80 inclusive, the result is 1. If speed is 81 or more, the result is 2. Unless its your birthday, on that day, your speed can be 5 higher in all cases. WAP to model the above scenario
def speeding_ticket():
    speed = int(input("Please enter the speed: "))
    bday = input("Was it his/her bday today(y/n): ")
    if bday.startswith("y"):
        speed = speed - 5
    ticket = 0
    if speed < 60:
        ticket = 0
    elif 80 >= speed >= 60:
        ticket = 1
    elif speed >= 81:
        ticket = 2
    
    if ticket == 0:
        print("no ticket")
    elif ticket == 1:
        print("Small ticket")
    elif ticket == 2:
        print("Big ticket")
'''
OUTPUT:

Please enter the speed: 82
Was it his/her bday today(y/n): y
Small ticket

'''

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
OUTPUT:

How many lines of this pattern do you want? 7
*
**
***
****
*****
******
*******

'''

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

'''
OUTPUT:

How many lines of this pattern do you want? 9
          *
         **
        ***
       ****
      *****
     ******
    *******
   ********
  *********

'''


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
'''
OUTPUT:

Enter number: 2389471
204

'''

# Question 6: Write a program which will find all such numbers which are divisible by 7 and are not multiple of 5, between
def question_6():
    for i in range(2000,3201):
        if i%7==0 and i%5 != 0:
            print(i,end=", ")

'''
OUTPUT:

2002, 2009, 2016, 2023, 2037, 2044, 2051, 2058, 2072, 2079, 2086, 2093, 2107, 2114, 2121, 2128, 2142, 2149, 2156, 2163, 2177, 2184, 2191, 2198, 2212, 2219, 2226, 2233, 2247, 2254, 2261, 2268, 2282, 2289, 2296, 2303, 2317, 2324, 2331, 2338, 2352, 2359, 2366, 2373, 2387, 2394, 2401, 2408, 2422, 
2429, 2436, 2443, 2457, 2464, 2471, 2478, 2492, 2499, 2506, 2513, 2527, 2534, 2541, 2548, 2562, 2569, 2576, 2583, 2597, 2604, 2611, 2618, 2632, 2639, 2646, 2653, 2667, 2674, 2681, 2688, 2702, 2709, 2716, 2723, 2737, 2744, 2751, 2758, 2772, 2779, 2786, 2793, 2807, 2814, 2821, 2828, 2842, 2849, 
2856, 2863, 2877, 2884, 2891, 2898, 2912, 2919, 2926, 2933, 2947, 2954, 2961, 2968, 2982, 2989, 2996, 3003, 3017, 3024, 3031, 3038, 3052, 3059, 3066, 3073, 3087, 3094, 3101, 3108, 3122, 3129, 3136, 3143, 3157, 3164, 3171, 3178, 3192, 3199,

'''

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

'''
OUTPUT:

Number of students? 5
Enter the age of student 1: 17
Enter the age of student 2: 16
Enter the age of student 3: 15
Enter the age of student 4: 14
Enter the age of student 5: 13
Group A :  12yrs and above but less than 15 yrs - 2
 Group B :  15yrs and above but less than 17 yrs - 2
 Group C :  17yrs and above but less than 19 yrs - 1
 Group D : Lesser than 12 yrs - 0

'''


# Question 8 : WAP to find if a number entered is a palindrome or not
def palindrome_number():
    number = input("Please enter the number: ")
    if number == number[::-1]:
        print(f"{number} is a palindrome number")
    else:
        print(f"{number} is not a palindrome number")
'''
OUTPUT:

Please enter the number: 1234321
1234321 is a palindrome number

'''

#Question 9 : According to a study, the approzimate level of intelligence of a person can be caluclated using the following formula i =2(y+05.x). Write a program, which produces a table of values of i, y and x . Where y varies from 1 to 6 and for each value of y, x varies from 5.5 to 12.5 in steps of 0.5
def question_9():
    for y in range(1,7):
        for x in range(55, 130,5):
            l=x/10
            i = 2*(y+(0.5*l))
            print(i,y,l,sep="|")


'''
OUTPUT:

7.5|1|5.5
8.0|1|6.0
8.5|1|6.5
9.0|1|7.0
9.5|1|7.5
10.0|1|8.0
10.5|1|8.5
11.0|1|9.0
11.5|1|9.5
12.0|1|10.0
12.5|1|10.5
13.0|1|11.0
13.5|1|11.5
14.0|1|12.0
14.5|1|12.5
9.5|2|5.5
10.0|2|6.0
10.5|2|6.5
11.0|2|7.0
11.5|2|7.5
12.0|2|8.0
12.5|2|8.5
13.0|2|9.0
13.5|2|9.5
14.0|2|10.0
14.5|2|10.5
15.0|2|11.0
15.5|2|11.5
16.0|2|12.0
16.5|2|12.5
11.5|3|5.5
12.0|3|6.0
12.5|3|6.5
13.0|3|7.0
13.5|3|7.5
14.0|3|8.0
14.5|3|8.5
15.0|3|9.0
15.5|3|9.5
16.0|3|10.0
16.5|3|10.5
17.0|3|11.0
17.5|3|11.5
18.0|3|12.0
18.5|3|12.5
13.5|4|5.5
14.0|4|6.0
14.5|4|6.5
15.0|4|7.0
15.5|4|7.5
16.0|4|8.0
16.5|4|8.5
17.0|4|9.0
17.5|4|9.5
18.0|4|10.0
18.5|4|10.5
19.0|4|11.0
19.5|4|11.5
20.0|4|12.0
20.5|4|12.5
15.5|5|5.5
16.0|5|6.0
16.5|5|6.5
17.0|5|7.0
17.5|5|7.5
18.0|5|8.0
18.5|5|8.5
19.0|5|9.0
19.5|5|9.5
20.0|5|10.0
20.5|5|10.5
21.0|5|11.0
21.5|5|11.5
22.0|5|12.0
22.5|5|12.5
17.5|6|5.5
18.0|6|6.0
18.5|6|6.5
19.0|6|7.0
19.5|6|7.5
20.0|6|8.0
20.5|6|8.5
21.0|6|9.0
21.5|6|9.5
22.0|6|10.0
22.5|6|10.5
23.0|6|11.0
23.5|6|11.5
24.0|6|12.0
24.5|6|12.5

'''

# Question 10(A) : WAP to print the result of the sequence x + x^2/2 + x^3/3 ... x^n/n
def question_10A():
    x = int(input("Enter value of x: "))
    n = int(input("Enter value of n: "))
    sum = 0
    for i in range(1,n+1):
        sum+= (x**n)/n
    print(sum)

'''
OUTPUT:

Enter value of x: 5
Enter value of n: 7
78125.00000000001

'''

# Question 10(B) : WAP to print the result of the sequence 1/sqrt(2) + 2/sqrt(3) ... n/(sqrt(n+1))
def question_10B():
    n = int(input("Enter value of n: "))
    sum = 0
    for i in range(1,n+1):
        sum+= i/(i**(1/2))
    print(sum)

'''
OUTPUT:

Enter value of n: 9

19.30600052603572

'''


# Practical Exam Questions
# Q 1 
def question_1():
    number_of_days_late = int(input("Enter how late was the book returned"))
    fine = 0 
    if number_of_days_late <= 5:
        fine = 2*number_of_days_late
    elif number_of_days_late < 11:
        fine = 10 + 3*(number_of_days_late-5)
    elif number_of_days_late < 16:
        fine = 25 + 4*(number_of_days_late-10)
    else:
        fine = 45 + 5*(number_of_days_late-15)
    print(f"The fine is {fine}")

# Question 2 
def question_2():
    n = int(input("Enter the number of terms: "))
    x = int(input("Enter the value of x: "))
    sum = 0 
    for i in range(1,n+1):
        s = 1
        for j in range(1,i+1):
            s =  s + (x ** j)
        sum +=s

    print(sum) 
