import sys


def func(a, b):
    a = int(float(a))
    b = int(float(b))
    g = 0
    v1 = 0
    v2 = 0
    e = 0

    g+=1

    result = ""

    if(a > b):
        v1 += 1
    elif a == b:
        e += 1
    else:
        v2 += 1

    result += "{} grenais\n".format(str(g))
    result += "Inter: {}\n".format(str(v1))
    result += "Gremio: {}\n".format(str(v2))
    result += "Empates: {}\n".format(str(e))

    if v1 > v2:
        result += "Inter venceu mais"
    elif v1 == v2:
        result += "Nao houve vencedor"
    else:
        result += "Gremio venceu mais"

    return result
    

if __name__ != '__main__': #PM
    a = sys.argv[1:][0]
    b = sys.argv[1:][1]
    print(func(a, b))