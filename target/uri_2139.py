import sys


def func(x, y):
    m = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31,30, 31]

    x = int(float(x))
    y = int(float(y))
    s = 0

    for i in range(x - 1):
        s += m[i]

    s += y

    if s == 359:
        return "E vespera de natal!"
    elif s == 360:
        return "E natal!"
    elif s < 360:
        return "Faltam " + str(360 - s) + " dias para o natal!"
    elif s > 360:
        return "Ja passou!"

if __name__ == '__main__':
    x = sys.argv[1:][0]
    y = sys.argv[1:][1]
    print(func(x, y))