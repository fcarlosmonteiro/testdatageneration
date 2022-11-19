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

            if not (index != len(texto) - 1): #PM | type_kill=weakly args=[2206.37] | type_kill=strongly args=[2206.37]
                line += " "
            
            index += 1
        
        result += "{}\n".format(line)
        texto = texto[0:len(texto)-1]
        i += 1
    return result

if __name__ == '__main__':
    x = sys.argv[1:][0]
    print(func(x))