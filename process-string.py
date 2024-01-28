# Application 1
# Given a string, you have to return a string in which each character (case-sensitive) is repeated once.

# Examples (Input -> Output):
# * "String"      -> "SSttrriinngg"
# * "Hello World" -> "HHeelllloo  WWoorrlldd"
# * "1234!_ "     -> "11223344!!__  "

# Apploication 1
input = input("Input String: ")
x=""
for i in range(len(input)):
    x = x + input[i]*2

print(x)


# Application 2
#  Given a string indicating a range of letters, return a string which includes all the letters in that range, including the last letter. Note that if the range is given in capital letters, return the string in capitals also!

# Examples
# "a-z" ➞ "abcdefghijklmnopqrstuvwxyz"
# "h-o" ➞ "hijklmno"
# "Q-Z" ➞ "QRSTUVWXYZ"
# "J-J" ➞ "J"
# Notes A hyphen will separate the two letters in the string.

# <<<<<<< HEAD
# #Application 2
# =======

# alphabet = "abcdefghijklmnopqrstuvwxyz"
# >>>>>>> 93130f284b9994d68d12d0ad5fe4c1726a826dbe
user_range = input("Enter a range of letters (e.g., a-z): ")
start, end = user_range.split('-')
result = ""
while start <= end:
        result += start
        start = chr(ord(start) + 1) 

print(result)


