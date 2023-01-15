def exp2(n):
    return n**2

def exp3(n):
    return n**3

try:
    n = float(input('Enter a number: '))
    print(exp2(n))
    print(exp3(n))
except ValueError:
    print('wrong')