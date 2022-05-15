from sympy import *

def plotf(a,b,f):
    plot(f, xlim = (a,b))

fn = input("enter: ")

try:
    plotf(-10, 10, fn) # or plotf(0, 2, "x**2"), or (almost) whatever
except:
    print("Invalid input")