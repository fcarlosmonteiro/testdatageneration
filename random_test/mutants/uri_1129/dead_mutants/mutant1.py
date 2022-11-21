import sys

def func(A, B, C, D, E):
    A = float(A)
    B = float(B)
    C = float(C)
    D = float(D)
    E = float(E)

    m = []

    if not (int(A) <= 127): #PM | type_kill=weakly args=[127, 8414.36, -4699.08, -1987.42, 4719.66] | type_kill=strongly args=[128, 128, 128, -1987.42, 4719.66] | type_kill=random args=[3474.568286751388, 9773.680331300504, 10.926080687086142, 2781.4187618467768, 5130.406305171515]
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


if __name__ == "__main__":
    A = sys.argv[1:][0]
    B = sys.argv[1:][1]
    C = sys.argv[1:][2]
    D = sys.argv[1:][3]
    E = sys.argv[1:][4]
    print(func(A,B,C,D,E))