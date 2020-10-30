"""
Challenge #9:

Write a function that creates a dictionary with each (key, value) pair being
the (lower case, upper case) versions of a letter, respectively.

Examples:
- mapping(["p", "s"]) ➞ { "p": "P", "s": "S" }
- mapping(["a", "b", "c"]) ➞ { "a": "A", "b": "B", "c": "C" }
- mapping(["a", "v", "y", "z"]) ➞ { "a": "A", "v": "V", "y": "Y", "z": "Z" }

Notes:
- All of the letters in the input list will always be lowercase.
"""
def mapping(letters):
    """
    a function that creates a dictionary with each (key, value) pair being
    the (lower case, upper case) versions of a letter, respectively.
    """
    # loop through list and make every letter an uppercase key with the letter value assigned to it.

     
    new_dictionary = dict(zip(letters, [letter.upper() for letter in letters]))

    return new_dictionary
        

print(mapping(["p", "s"]))
print(mapping(["a", "b", "c"]))
print(mapping(["a", "v", "y", "z"]))