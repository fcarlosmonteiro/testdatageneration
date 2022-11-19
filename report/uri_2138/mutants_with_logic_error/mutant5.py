import sys

def func(x):
    x = str(int(float(x)))
    digitos = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    digitosValue = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    digitoMaior = 0
    nDigito = 0

    for digito in x:
        digitosValue[digitos.index(digito)] += 1
    
    for index in range(10):
        digitoValue = digitosValue[index]
        if nDigito <= digitoValue:
            digitoMaior = index
            nDigito = digitoValue 
    
    return digitoMaior


if __name__ != '__main__': #PM
    x = sys.argv[1:][0]
    print(func(x))