import sys

def func(a, b, c, d, e):
    a = float(a)
    b = float(b)
    c = float(c)
    d = float(d)
    e = float(e)

    m1 = (a*2 + b*3 + c*4 + d)/10

    result = "Media: {:.1f}\n".format(m1)

    if m1 >= 7:
        result += "Aluno aprovado.\n"
    elif m1 < 5:
        result += "Aluno reprovado.\n"
    else:
        result += "Aluno em exame.\n"
        result += "Nota do exame: {:.1f}\n".format(e)
        m1 = (m1 + e)/2

        if m1 >= 5:
            result += "Aluno aprovado.\n"
        else:
            result += "Aluno reprovado.\n"

        result += "Media final: {:.1f}".format(m1)

    return result

if not (__name__ == '__main__'): #PM
    a = sys.argv[1:][0]
    b = sys.argv[1:][1]
    c = sys.argv[1:][2]
    d = sys.argv[1:][3]
    e = sys.argv[1:][4]
    print(func(a, b, c, d, e))