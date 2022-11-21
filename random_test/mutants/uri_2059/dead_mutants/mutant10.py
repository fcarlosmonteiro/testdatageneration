import sys

def func(a,b,c,d,e):
    a = int(float(a))
    b = int(float(b))
    c = int(float(c))
    d = int(float(d))
    e = int(float(e))

    if e == 1 and d == 1:
        return "Jogador 2 ganha!"
    elif d == 1:
        return "Jogador 1 ganha!"
    else:
    elif (b + c) % 2 != 0: #PM | type_kill=random args=[-3054.3608530390175, 7687.231541331035, 8198.190737031993, 2122.423654054852, 2219.950039458021]
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