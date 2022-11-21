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

    if not (L1 % 2 == 0): #PM | type_kill=weakly args=[-9580.75, -3200.64, 5640.88, -814, -9646.49, 4838.64, 5738.9] | type_kill=strongly args=[6013, 3141, 3213.85, -1315.13, -478.5, -5194.3, -1516.5] | type_kill=random args=[9739.971209908595, -1084.816169077394, 8168.162617454607, 9710.554951727594, -2290.287661317032, 7192.837120897013, -7290.169943407656]
        P1 += b
    
    if L2 % 2 == 0:
        P2 += b
    
    if P1 == P2:
        return 'Empate'
    elif P1 > P2:
        return 'Dabriel'
    else:
        return 'Guarte'


if __name__ == '__main__':
    b = sys.argv[1:][0]
    A1 = sys.argv[1:][1]
    D1 = sys.argv[1:][2]
    L1 = sys.argv[1:][3]
    A2 = sys.argv[1:][4]
    D2 = sys.argv[1:][5]
    L2 = sys.argv[1:][6]
    print(func(b, A1, D1, L1, A2, D2, L2))