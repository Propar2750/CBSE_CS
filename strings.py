string = "Hello World"

print(len(string)) # This method returns the length of the string
# Output : 11


print(string.capitalize()) # This method returns the exact scopy of the string with the first letter in uppercase
# Output : Hello world


print(string.split(" ")) # split has two arguments (seperator, [maxsplit])
# Output : ['Hello', 'World']


print(string.replace("Hello","Bye")) # This function replaces all the occurences of the old string with the new string
# Arguments are (old,new)
# Output : Bye World


print(string.find("ee")) # Arguments are (sub,start,end) sub : Substring which needs to be searched . 
# This function is used to search the first occurence of the substring in the given string. The find() method returns the lowest index of the substring if it is found in the given string. if the substring is not found, it returns -1
# Output : -1

print(string.isalpha()) # This function checks for alphabets in an inputted string. It returns True if the string contains only letters, otherwise returns False.
# Output : False

print(string.isalnum()) # The isalnum() method returns True if all the characters are alphanumeric, i.e., alphabet letters(A-Z, a-z) and numbers (0,9)
# Output : False

print(string.isdigit()) # This functoin returns True if the string contains only digits, otherwise False
# Output : False

print(string.title()) # This function reutrns the strin gwith first letter of every word in the string in uppercase and rest in lowercase
# Output : Hello World

print(string.count("l")) # arguments (substring,start,end)
# This function returns the number of times substring str occurs in the given string if we do not give start index and end infex, then searching starts from index 0 and ends at length of string
# Output : 3

print(string.lower()) # this function converts all the uppercase letters in the string into lowercase
# Output : hello world

print(string.islower()) # This function returns True if all letters in the string are  in lowercase
#Output : False

print(string.upper()) # This function convertsw lowercase letters into uppercase letters
# Output : HELLO WORLD

print(string.isupper()) # This function returns True if the string is in uppercase 
# Output : False

print(string.lstrip('He')) # This function returns the string after removing the spaces or characters(argument) from th eleft of the string.
# Output : llo World

print(string.rstrip('ld'))# This function returns the string after removing the spaces or characters(argument) from the right of the string.
# Output : Hello Wor

print(string.strip()) # This function returns the string after removing the spaces both on the left and the right of the string
# Output : Hello World

print(string.isspace()) # This function returns True if the string contains only whitespace characters, otherwise returns False
# Output : False

print(string.istitle()) # This functions returns True if the string properly "title-cased"
# Output : True

print('-'.join(string)) # This function returns a string in which the string is joined by a string operator
# Output : H-e-l-l-o- -W-o-r-l-d

print(string.swapcase()) # This function converts and returns all the uppercase characters into lowercase and vice versa of the given string. 
# Output : hELLO wORLD

print(string.partition('lo')) # Partition function is used to split the given string using the specified seperator and returns a tuple with three parts
# Output : ('Hel', 'lo', ' World')

print(string.endswith('ld')) # This function returns True if the given string ends with the specified substring
# Output : True

print(string.startswith('ld')) # This function returns True if the given string starts with the specified substring
# Output : False
