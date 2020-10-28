"""
Challenge #6:
​
Create a function that takes a string, checks if it has the same number of "x"s
and "o"s and returns either True or False.
​
- Return a boolean value (True or False).
- The string can contain any character.
- When no x and no o are in the string, return True.
​
Examples:
- XO("ooxx") ➞ True
- XO("xooxx") ➞ False
- XO("ooxXm") ➞ True (Case insensitive)
- XO("zpzpzpp") ➞ True (Returns True if no x and o)
- XO("zzoo") ➞ False
​
set an o and x counter to zero
loop over each character in the string
do a check if it contains an "x"
    increment the x counter
do a check if it contains an "o"
    increment the o counter
​
check if x counter is equal to o counter
    return true to the caller
otherwise
    return false to the caller
"""
# def XO(txt:str) -> bool:
#     # Your code here
#     # set an o and x counter to zero
#     o_counter = 0
#     x_counter = 0
#     # loop over each character in the string
#     for char in txt:
#         # do a check if it contains an "x"
#         if char == "x":
#             # increment the x counter
#             x_counter += 1
#         # do a check if it contains an "X"
#         elif char == "X":
#             # increment the x counter
#             x_counter += 1
#         # do a check if it contains an "o"
#         elif char == "o":
#             # increment the o counter
#             o_counter += 1
#         # do a check if it contains an "O"
#         elif char == "O":
#             # increment the o counter
#             o_counter += 1

#     # check if x counter is equal to o counter
#     if x_counter == o_counter:
#         # return true to the caller
#         return True
#     # otherwise
#     else:
#         # return false to the caller
#         return False

# def XO(txt:str) -> bool:
#     # Your code here
#     # set an o and x counter to zero
#     o_counter = 0
#     x_counter = 0
#     # loop over each character in the string
#     for char in txt:
#         # do a check if it contains an "x"
#         if char == "x" or char == "X":
#             # increment the x counter
#             x_counter += 1
#         # do a check if it contains an "o"
#         elif char == "o" or char == "O":
#             # increment the o counter
#             o_counter += 1

#     # return x counter is equal to o counter as a boolean to the caller
#     return x_counter == o_counter

def XO(txt: str) -> bool:
    # lowercase the txt
    lower_txt = txt.lower()
    # return the count of lower txt using "x" as a parameter == the count of lower txt using "x" 
    # as a parameter as a boolean value to the caller 
    return lower_txt.count("o") == lower_txt.count("x")


print(XO("ooxx")) # ➞ True
print(XO("xooxx"))  # ➞ False
print(XO("ooxXm")) # ➞ True (Case insensitive)
print(XO("zpzpzpp")) # ➞ True (Returns True if no x and o)
print(XO("zzoo"))  #  ➞ False