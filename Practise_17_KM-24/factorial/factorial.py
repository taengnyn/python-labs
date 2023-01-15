def fact(n):
    if n == 1: 
        return 1 
    else:
        res = n * fact(n-1) 
        return res

try:
    n = int(input('Enter the number: '))    
    print(fact(n))
except ValueError:
    print('wrong')