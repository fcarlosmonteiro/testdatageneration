import sys

def triangle(a, b, c):
    longest = 0
    m = 0
    n = 0

    if a >= b: #PM
        if (a > c):
            longest = a
            m, n = b, c

        else:
            longest = c
            m, n = a, b

    else:
        if (b > c):
            longest = b
            m, n = a, c
        else:
            longest = c
            m, n = a, b

    if longest < (m + n):
        return True

    return False


if __name__ == "__main__":
    a = float(sys.argv[1:][0])
    b = float(sys.argv[1:][1])
    c = float(sys.argv[1:][2])
    print(triangle(a, b, c))