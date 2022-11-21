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

    if (len(m) == 0 or len(m) < 1): #PM | type_kill=weakly args=[128, 127, -4699.08, -1987.42, 4719.66] | type_kill=strongly args=[128, 127, -4699.08, -1987.42, 4719.66] | type_kill=random args=[9196.371735691802, -8203.406926672005, 9536.298526413222, -7943.174224229077, -2965.6276838955064]
        return '*'
    else:
        return m[0] 


if __name__ == "__main__":
    A = sys.argv[1:][0]
    B = sys.argv[1:][1]
    C = sys.argv[1:][2]
    D = sys.argv[1:][3]
    E = sys.argv[1:][4]
    print(func(A,B,C,D,E))