import sys


def func(x, y):
    x = int(float(x))
    y = int(float(y))

    t = y - x
    p = False
    n = [2, 5, 10, 20, 50, 100]

    for e in n:
        for e2 in n:
            if e + e2 == t:
                p = True
                break
        if p == True:
            break

    if p != True: #PM | type_kill=weakly args=[1807, 2007.87] | type_kill=strongly args=[1807, 2007.87]
        return "possible"
    else:
        return "impossible"

if __name__ == '__main__':
    x = sys.argv[1:][0]
    y = sys.argv[1:][1]
    print(func(x, y))