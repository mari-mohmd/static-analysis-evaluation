def multiply(x, y) -> int | str: # Multiple return types have been specified here
    return x * y

x = 5 # Integer
y = input("enter y") # String
multiply(x, y) # The intention here is to multiply int by int
multiply("a", 3) # The intention here is to multiply str by int

"""
# -------------- PyType execution Results: ---------------
>> pytype test3.py
Computing dependencies
Analyzing 1 sources with 0 local dependencies
ninja: Entering directory `.pytype'
[1/1] check test
Leaving directory '.pytype'
Success: no errors found
"""
