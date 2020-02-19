import pdb


def myfunc(a, b):
    pdb.set_trace()
    print("my func")
    print("my func")
    print("my func")


myfunc(1, 2)

"""

Commands:
c: continue execution
w: shows the context of the current line it is executing.
a: print the argument list of the current function
s: Execute the current line and stop at the first possible occasion.
n: Continue execution until the next line in the current function is reached or it returns.

The difference between (n) next and (s) step is that step stops inside a called function, while next executes called 
functions at (nearly) full speed, only stopping at the next line in the current function.

another method is
$ python -m pdb my_script.py
"""