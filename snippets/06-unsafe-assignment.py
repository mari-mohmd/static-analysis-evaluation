
"""
Most commonly used static analysis tools for Python such as Pytype, Pylint, Pyright, and Mypy are unable to detect the issue in the following code:
"""
y: list[int] = [1,2,3]
y.pop()  # Removes last element from the list. y now is [1,2]
x: int = y[2]  # IndexError: list index out of range
