"""
Exception Handling

Input: 2 numbers
Output: division and addition of those numbers

Throws error if there is a ValueError, ZeroDivisionError or any other
using try/Except

"""

try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    z = 10
    print("a/b = ", a/b)
    print("a+b = ", a+b)
    print("Successful")

except ValueError:
    print("Error: Not a Valid Number")

except ZeroDivisionError:
    print("Error: Can't divide by zero")

except:
    print("Something went wrong!!!")
    
