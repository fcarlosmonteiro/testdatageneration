import sys


def func(x, y):
    m = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31,30, 31]

    x = int(x)
    y = int(y)
    s = 0

    for i in range(x - 1):
        s += m[i]

    s += y

    if s == 359:
        return "E vespera de natal!"
    elif s == 360:
        return "E natal!"
    elif s > 360: #PM | type_kill=weakly args=[-2982.05, 360] | type_kill=strongly args=[-2982.05, 361]
        return "Faltam " + str(360 - s) + " dias para o natal!"
    elif s > 360:
        return "Ja passou!"

if __name__ == '__main__':
    x = float(sys.argv[1:][0])
    y = float(sys.argv[1:][1])
    print(func(x, y))