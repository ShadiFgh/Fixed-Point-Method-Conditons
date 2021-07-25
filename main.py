import numpy as np

def find_fixed_point(f, x, itr):
    while itr:
         x = f(x)
         print(x)
         itr = itr - 1
    return x
