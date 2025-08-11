def multiply(x, y) -> int: # The return type has been specified here
    return x * y

x = 5 # Integer
y = input("enter y") # String
multiply(x, y) # The operation performed here is int * str

"""
# -------------- PyType execution Results: ---------------
>> pytype test2.py
Computing dependencies
Analyzing 1 sources with 0 local dependencies
ninja: Entering directory `.pytype'
[1/1] check test
FAILED: error: in multiply: bad return type [bad-return-type]
           Expected: int
  Actually returned: str

    return x * y
    ~~~~~~~~~~~~

Called from (traceback):
  line 96, in current file

For more details, see https://google.github.io/pytype/errors.html#bad-return-type
ninja: build stopped: subcommand failed.
Leaving directory '.pytype'
"""
