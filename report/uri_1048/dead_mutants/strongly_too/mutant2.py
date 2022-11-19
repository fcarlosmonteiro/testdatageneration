import sys

def func(x):
    x = float(x)
    result = ''
    if x >= 0 and x <= 400:
        r = x/100*15

        result += "Novo salario: {:.2f}\n".format(x + r)
        result += "Reajuste ganho: {:.2f}\n".format(r)
        result += "Em percentual: 15 %"
    elif not ((x >= 400.01 and x <= 800)): #PM | type_kill=weakly args=[50.61] | type_kill=strongly args=[1109.3]
        r = x/100*12
        result += "Novo salario: {:.2f}\n".format(x + r)
        result += "Reajuste ganho: {:.2f}\n".format(r)
        result += "Em percentual: 12 %"
    elif x >= 800.01 and x <= 1200:
        r = x/100*10
        result += "Novo salario: {:.2f}\n".format(x + r)
        result += "Reajuste ganho: {:.2f}\n".format(r)
        result += "Em percentual: 10 %"
    elif x >= 1200.01 and x <= 2000:
        r = x/100*7
        result += "Novo salario: {:.2f}\n".format(x + r)
        result += "Reajuste ganho: {:.2f}\n".format(r)
        result += "Em percentual: 7 %"
    else:
        r = x/100*4
        result += "Novo salario: {:.2f}\n".format(x + r)
        result += "Reajuste ganho: {:.2f}\n".format(r)
        result += "Em percentual: 4 %"
    return result


if __name__ == "__main__":
    x = sys.argv[1:][0]
    print(func(x))