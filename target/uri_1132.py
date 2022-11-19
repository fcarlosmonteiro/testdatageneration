import sys


def func(x, y):
    x = float(x)
    y = float(y)
    z = 0

    if x > y:
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
    x = sys.argv[1:][0]
    y = sys.argv[1:][1]
    print(func(x, y))