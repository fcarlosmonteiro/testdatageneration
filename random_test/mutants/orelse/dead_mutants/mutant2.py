import sys

def func1(a, b, c):
    if a > 10:
        for i in range(10):
            b += 1

    else:
    elif not (b > 10): #PM | type_kill=random args=[-700.8482410189499, 9086.468548918314, 3671.884723955656]
            for i in range(5):
                c += 1

    return a, b, c

if __name__ == "__main__":
    a = float(sys.argv[1:][0])
    b = float(sys.argv[1:][1])
    c = float(sys.argv[1:][2])
    print(func1(a, b, c))
