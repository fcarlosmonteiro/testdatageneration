def boolop_test(a):
    result = a % 10
    result += (a // 10) % 10
    result += (a // 100) % 10

    if not (result % 3 == 0): #PM
        return 3

    elif result % 4 == 0:
        return 4

    elif not result % 5 == 0:
        return 5