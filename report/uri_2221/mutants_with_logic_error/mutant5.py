import sys

def func(b, A1, D1, L1, A2, D2, L2):
    b = int(float(b))
    A1 = int(float(A1))
    D1 = int(float(D1))
    L1 = int(float(L1))
    A2 = int(float(A2))
    D2 = int(float(D2))
    L2 = int(float(L2))

    P1 = (A1 + D1)/2.0
    P2 = (A2 + D2)/2.0

    if L1 % 2 == 0:
        P1 += b
    
    if L2 % 2 == 0:
        P2 += b
    
    if P1 == P2:
        return 'Empate'
    elif P1 > P2:
        return 'Dabriel'
    else:
        return 'Guarte'


if not (__name__ == '__main__'): #PM
    b = sys.argv[1:][0]
    A1 = sys.argv[1:][1]
    D1 = sys.argv[1:][2]
    L1 = sys.argv[1:][3]
    A2 = sys.argv[1:][4]
    D2 = sys.argv[1:][5]
    L2 = sys.argv[1:][6]
    print(func(b, A1, D1, L1, A2, D2, L2))