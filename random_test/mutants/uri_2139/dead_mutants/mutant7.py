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
    elif s != 360: #PM | type_kill=weakly args=[-6382.21, 5672.92] | type_kill=strongly args=[-6382.21, 5672.92] | type_kill=random args=[-6521.951991563214, 3766.4962520706085]
        return "E natal!"
    elif s < 360:
        return "Faltam " + str(360 - s) + " dias para o natal!"
    elif s > 360:
        return "Ja passou!"

if __name__ == '__main__':
    x = float(sys.argv[1:][0])
    y = float(sys.argv[1:][1])
    print(func(x, y))