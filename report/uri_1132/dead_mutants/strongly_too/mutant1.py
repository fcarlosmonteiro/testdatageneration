import sys


def func(x, y):
    z = 0

    if not (x > y): #PM | type_kill=weakly args=[7382.43, 1943.97] | type_kill=strongly args=[7382.43, 1943.97]
        z = x
        x = y
        y = z

    s = 0

    while y >= x:
        if x % 13 != 0:
            s += x
        x+=1
        
    return s

if __name__ == '__main__':
    x = float(sys.argv[1:][0])
    y = float(sys.argv[1:][1])
    print(func(x, y))