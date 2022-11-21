import sys

def boolop_test(a):
    result = a % 10
    result += (a // 10) % 10
    result += (a // 100) % 10

    if not (result % 3 == 0): #PM | type_kill=weakly args=[3910.26] | type_kill=strongly args=[3910.26]
        return 3

    elif result % 4 == 0:
        return 4

    elif not result % 5 == 0:
        return 5


if __name__ == "__main__":
    a = float(sys.argv[1:][0])
    print(boolop_test(a))
