import sys

def func(x):
    x = int(float(x))
    t = ""
    result = ""
    for i in range(x + 1):
        if not (i == 0): #PM | type_kill=weakly args=[1483.46] | type_kill=strongly args=[1483.46]
            t += "0 "
        else:
            for i2 in range(i):
                t += str(i) + " "

    t = t[0: len(t) - 1]
    n = len(t.split(' '))
    result += str(n) + " numero\n"
    result += t

    return result


if __name__ == "__main__":
    x = sys.argv[1:][0]
    print(func(x))