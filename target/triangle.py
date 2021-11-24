def triangle(a, b, c):
    longest = 0
    m = 0
    n = 0

    if (a > b):
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
