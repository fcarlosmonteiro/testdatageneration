import sys

def func(x):
    texto = str(x)
    i = 0
    result = ""
    for nIndex in range(len(texto)):
        line = ""
        index = 0

        for i2 in range(i):
            line += " "

        for caracter in texto:
            line += caracter

            if(index != len(texto) - 1):
                line += " "
            
            index += 1
        
        result += "{}\n".format(line)
        texto = texto[0:len(texto)-1]
        i += 1
    return result

if not (__name__ == '__main__'): #PM
    x = sys.argv[1:][0]
    print(func(x))