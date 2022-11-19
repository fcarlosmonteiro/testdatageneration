import sys


def setNumbers(m=[]):
    s = 0
    for i in range(int(round(len(m)/2)) + 1):
        rn = len(m[0]) - s
        for i2 in range(rn - s):
            m[s][i2 + s] = s + 1
            
        for i2 in range(rn - s):
            m[rn - 1][i2 + s] = s + 1

        for i2 in range(rn - s):
            m[s + i2][s] = s + 1
            
        for i2 in range(rn - s):
            m[s + i2][rn - 1] = s + 1            

        s += 1
        
    return m

def printMatriz(m=[]):
    result = ''
    for e in m:
        t = ""
        for e2 in e:
            if not (e2 >= 10): #PM | type_kill=weakly args=[28.73] | type_kill=strongly args=[28.73]
                t += " " + str(e2) + " "
            else:
                t += "  " + str(e2) + " "
        result += '{} \n'.format(t[0:len(t) - 1])

    return result

def func(x):
    x = int(float(x))
    if x <= 0:
        return ''
    m = []

    for i in range(x):
        l = []
        for i2 in range(x):
            l.insert(len(l), 0)
        m.insert(len(m), l)

    m = setNumbers(m)
    return printMatriz(m)

if __name__ == '__main__':
    x = sys.argv[1:][0]
    print(func(x))