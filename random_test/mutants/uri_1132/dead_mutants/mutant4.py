import sys


def func(x, y):
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

if not (__name__ == '__main__'): #PM | type_kill=random args=[9865.96095962252, 5005.5249507689405]
    x = float(sys.argv[1:][0])
    y = float(sys.argv[1:][1])
    print(func(x, y))