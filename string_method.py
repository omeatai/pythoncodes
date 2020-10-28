#The capitalize() method returns a string where the first character is upper case.
# txt = "hello, welcome to python!"
# x = txt.capitalize()
# print (x)

# The casefold() method returns a string where all the characters are lower case.
# This method is similar to the lower() method, but the casefold() method is stronger and
# more aggressive, meaning that it will convert more characters into lower case.
# txt = "HELLO, Welcome To Python!"
# x = txt.casefold()
# print(x)

#The center() method will center align the string, 
#using a specified character (space is default) as the fill character.
# txt = "banana"
# x = txt.center(20)
# print(x)
# txt = "banana"
# x = txt.center(20, "O")
# print(x)

#The count() method returns the number of times a specified value appears in the string.
#Return the number of times the value "apple" appears in the string:
# txt = "I love apples, good apples. apples are my favorite fruit"
# x = txt.count("apple")
# print(x)
#Search from position 10 to 24:
# txt = "I love apples, apple are my favorite fruit"
# x = txt.count("apple", 10, 24)
# print(x)

#The encode() method encodes the string, using the specified encoding. 
#If no encoding is specified, UTF-8 will be used.
# txt = "My name is Ståle"
# x = txt.encode()
# print(x) 

#The endswith() method returns True if the string ends with the specified value, otherwise False.
#Check if the string ends with a punctuation sign (.):
# txt = "Hello, welcome to my world."
# x = txt.endswith(".")
# print(x) 
#Check if the string ends with the phrase "my world.":
# txt = "Hello, welcome to my world."
# x = txt.endswith("my world.")
# print(x) 
#Check if position 5 to 11 ends with the phrase "my world.":
# txt = "Hello, welcome to my world."
# x = txt.endswith("my world.", 5, 11)
# print(x) 

