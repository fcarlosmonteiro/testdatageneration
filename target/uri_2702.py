import sys

def func(item1,item2,item3,item4,item5,item6):
    a,b,c,d,e,f = [float(item1),float(item2),float(item3),float(item4),float(item5),float(item6)]
    r = 0

    if int(a) < int(d):
        r += int(d) - int(a)

    if int(b) < int(e):
        r += int(e) - int(b)

    if int(c) < int(f):
        r += int(f) - int(c)

    return r


if __name__ == "__main__":
    item1 = sys.argv[1:][0]
    item2 = sys.argv[1:][1]
    item3 = sys.argv[1:][2]
    item4 = sys.argv[1:][3]
    item5 = sys.argv[1:][4]
    item6 = sys.argv[1:][5]
    print(func(item1,item2,item3,item4,item5,item6))