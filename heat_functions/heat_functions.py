# exponential fucntion generator
import numpy as np
def egene(a,b,c):
    return lambda x: a*np.exp(-b*x)+c
def constant(c):
    return lambda x: c
