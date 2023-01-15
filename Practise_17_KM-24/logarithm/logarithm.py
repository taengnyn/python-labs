from math import log10, log as logarithm

def log(a, b):
    return round(logarithm(b, a), 3)


def ln(b):
    return round(logarithm(b), 3)


def lg(b):
    return round(log10(b), 3)

try:
    b = float(input("Enter the number: "))
    a = float(input("Enter the base of the number: "))
    if a > 0 and a != 1 and b > 0:
        print(log(a, b))  
        print(ln(b)) 
        print(lg(b)) 
    else:
        raise ValueError
except ValueError:
    print("Error, enter the data correctly.")