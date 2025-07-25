x = 2
y = 3


def abc():
    """    This function modifies the global variable x and defines a local variable y."""
    global x  # Declare x as a global variable
    x = 5
    y = 3


abc()
print(x, y)
