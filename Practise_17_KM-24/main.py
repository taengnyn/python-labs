from exp_root.exponentiation import exp2, exp3
from exp_root.root import root2, root3
from factorial.factorial import fact
from logarithm.logarithm import log, lg, ln


def main():
    menu ="""
    1) x^2
    2) x^3
    3) x^(1/2)
    4) x^(1/3)
    5) x!
    6) log x base a
    7) log x base 10
    8) log x base e
    """
    
    print(menu)
    while True:
        try:
            point = int(input('Enter the number of function: '))
            if point <= 5 or point>= 7:
                n = float(input('Enter a number: '))
                if point == 1:
                    print(exp2(n))
                elif point == 2:
                    print(exp3(n))
                elif point == 3:
                    if point < 0:
                        print('wrong value')
                    else:
                        print(root2(n))
                elif point == 4:
                    if point < 0:
                        print('wrong value')
                    else:
                        print(root3(n))
                elif point == 5:
                    print(fact(n))
                elif point == 7:
                    print(lg(n))
                elif point == 8:
                    print(ln(n))        
            elif point == 6:
                a = float(input('Enter a log base: '))
                if a<=0 or a == 1:
                    print('wrong value')
                else:
                    b = float(input('Enter a number: '))
                    if b <= 0:
                        print('wrong value')
                    else:
                        print(log(a, b))
        except ValueError:
            print('wrong value')

if __name__ == "__main__":
    main()