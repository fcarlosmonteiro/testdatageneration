import sys

def func(a,b,c,d,e):
    a = int(float(a))
    b = int(float(b))
    c = int(float(c))
    d = int(float(d))
    e = int(float(e))

    if (e == 1 and d != 1): #PM | type_kill=weakly args=[-4245.67, -1527.76, -2525, 8709.8, 9839.88]
        return "Jogador 2 ganha!"
    elif d == 1:
        return "Jogador 1 ganha!"
    else:
        if (b + c) % 2 == 0:
            if a == 1:
                return "Jogador 1 ganha!"
            else:
                return "Jogador 2 ganha!"
        else:
            if a == 0:
                return "Jogador 1 ganha!"
            else:
                return "Jogador 2 ganha!" 

if __name__ == '__main__':
    a = sys.argv[1:][0]
    b = sys.argv[1:][1]
    c = sys.argv[1:][2]
    d = sys.argv[1:][3]
    e = sys.argv[1:][4]
    print(func(a,b,c,d,e))