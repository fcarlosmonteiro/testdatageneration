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

    if p == True:
        return "possible"
    else:
        return "impossible"

if not (__name__ == '__main__'): #PM | type_kill=random args=[874.2551440435691, 8898.451514665983]
    x = sys.argv[1:][0]
    y = sys.argv[1:][1]
    print(func(x, y))