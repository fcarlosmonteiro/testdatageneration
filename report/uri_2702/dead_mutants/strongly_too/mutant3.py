import sys

def func(item1,item2,item3,item4,item5,item6):
    a,b,c,d,e,f = [float(item1),float(item2),float(item3),float(item4),float(item5),float(item6)]
    r = 0

    if int(a) < int(d):
        r += int(d) - int(a)

    if int(b) < int(e):
        r += int(e) - int(b)

    if not (int(c) < int(f)): #PM | type_kill=weakly args=[2776.55, 2057.34, -9401.47, -3249.99, -5696.06, 2598.68] | type_kill=strongly args=[2776.55, 2057.34, -9401.47, -3249.99, -5696.06, 2598.68]
        r += int(f) - int(c)

    return r


if __name__ == "__main__":
    item1 = float(sys.argv[1:][0])
    item2 = float(sys.argv[1:][1])
    item3 = float(sys.argv[1:][2])
    item4 = float(sys.argv[1:][3])
    item5 = float(sys.argv[1:][4])
    item6 = float(sys.argv[1:][5])
    print(func(item1,item2,item3,item4,item5,item6))