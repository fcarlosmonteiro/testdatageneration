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

if not (__name__ == '__main__'): #PM | type_kill=random args=[-706.0418171585261, 3027.0537059985745, -6873.7026148830355, -5708.200350725401, 3909.462213074221]
    a = sys.argv[1:][0]
    b = sys.argv[1:][1]
    c = sys.argv[1:][2]
    d = sys.argv[1:][3]
    e = sys.argv[1:][4]
    print(func(a,b,c,d,e))