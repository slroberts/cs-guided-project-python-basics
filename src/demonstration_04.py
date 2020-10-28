"""
Challenge #4:

Create a function that takes length and width and finds the perimeter of a rectangle.

to get the perimeter of a rectangle we could use either (L * 2 + W * 2) or (L + W) * 2
Examples:
- find_perimeter(6, 7) ➞ 26
- find_perimeter(20, 10) ➞ 60
- find_perimeter(2, 9) ➞ 22
"""
def find_perimeter(length, width):
    """
    a function that takes length and width and finds the perimeter of a rectangle.
    """
    # return the value of the expression (length + Width) * 2 to the caller
    return (length + width) * 2

print(find_perimeter(6,7))
print(find_perimeter(20,10))
print(find_perimeter(2,9))