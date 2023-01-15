def root2(n):
    return n ** (1/2)


def root3(n):
    return n ** (1/3)


try:
    n = float(input('Enter a positive number: '))
    if n > 0:
        print(root2(n))
        print(root3(n))
    else:
        raise ValueError
except ValueError:
        print('wrong')