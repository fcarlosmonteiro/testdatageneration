import sys

def boolop_test(a):
    result = a % 10
    result += (a // 10) % 10
    result += (a // 100) % 10

    if result % 3 == 0:
        return 3

    elif not (result % 4 == 0): #PM | type_kill=weakly args=[80.65] | type_kill=strongly args=[80.65] | type_kill=random args=[-9045.769679752913]
        return 4

    elif not result % 5 == 0:
        return 5


if __name__ == "__main__":
    a = float(sys.argv[1:][0])
    print(boolop_test(a))
