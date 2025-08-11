def multiply(x: int | str, y: int) -> int | str: # The return type has been specified here
    return x * y

x: int = 5 # Added type annotation
y: int = input("enter y") # Added type annotation - This will fail becasue the return type of input() is string
multiply(x, y) # The intention here is to multiply int by int
multiply("a", 3) # The intention here is to multiply str by int

"""
# -------------- PyType execution Results: ---------------
pytype test4.py 
Computing dependencies
Analyzing 1 sources with 0 local dependencies
ninja: Entering directory `.pytype'
[1/1] check test
FAILED: test4.py:95:1: error: in <module>: Type annotation for y does not match type of assignment [annotation-type-mismatch]
  Annotation: int
  Assignment: str

y : int = input("enter y") # String
~

For more details, see https://google.github.io/pytype/errors.html#annotation-type-mismatch
ninja: build stopped: subcommand failed.
Leaving directory '.pytype'
"""
