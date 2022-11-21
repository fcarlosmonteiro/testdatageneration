import sys

def func(A, B, C, D, E):
    A = float(A)
    B = float(B)
    C = float(C)
    D = float(D)
    E = float(E)

    m = []

    if int(A) <= 127:
        m.insert(len(m), 'A')

    if int(B) <= 127:
        m.insert(len(m), 'B')

    if int(C) <= 127:
        m.insert(len(m), 'C')

    if int(D) <= 127:
        m.insert(len(m), 'D')

    if int(E) <= 127:
        m.insert(len(m), 'E')

    if len(m) == 0 or len(m) > 1:
        return '*'
    else:
        return m[0] 


if not (__name__ == '__main__'): #PM | type_kill=random args=[5125.790378225334, 5980.874359316922, 7032.245519916389, -9592.475944889457, -2990.9546322882115]
    A = sys.argv[1:][0]
    B = sys.argv[1:][1]
    C = sys.argv[1:][2]
    D = sys.argv[1:][3]
    E = sys.argv[1:][4]
    print(func(A,B,C,D,E))