import sys

def func(item1,item2,item3,item4,item5):
    x=[item1,item2,item3,item4,item5]
    m2 = 0
    m3 = 0
    m4 = 0
    m5 = 0

    for y in x:
        y = int(y)
        if y % 2 != 0: #PM | type_kill=weakly args=[-7038.25, 3277.83, -8251.13, 8511.23, -3857.47] | type_kill=strongly args=[-7038.25, 3277.83, -8251.13, 8511.23, -3857.47]
            m2 += 1
        if y % 3 == 0:
            m3 += 1
        if y % 4 == 0:
            m4 += 1
        if y % 5 == 0:
            m5 += 1
    valor = str(m2) + " Multiplo(s) de 2, "
    valor += str(m3) + " Multiplo(s) de 3, "
    valor += str(m4) + " Multiplo(s) de 4 e "
    valor += str(m5) + " Multiplo(s) de 5"
    
    return valor

if __name__ == '__main__':
    item1 = float(sys.argv[1:][0])
    item2 = float(sys.argv[1:][1])
    item3 = float(sys.argv[1:][2])
    item4 = float(sys.argv[1:][3])
    item5 = float(sys.argv[1:][4])
    print(func(item1,item2,item3,item4,item5))