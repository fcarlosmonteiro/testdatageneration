import sys

def func(item1,item2,item3,item4,item5,item6,item7,item8,item9,item10,item11):
    n2 = int(float(item1))
    ns = [
        float(item2),
        float(item3),
        float(item4),
        float(item5),
        float(item6),
        float(item7),
        float(item8),
        float(item9),
        float(item10),
        float(item11),
    ]
    ni = []

    for na in ns:
        na = int(na)
        if na % 2 < 0: #PM | type_kill=weakly args=[-4529.37, -9368.02, 9023.84, 7166.16, -1482.87, 767.3, 9290.93, 368.13, -3327.6, -8857.57, -1668.24] | type_kill=strongly args=[-4529.37, -9368.02, 9023.84, 7166.16, -1482.87, 767.3, 9290.93, 368.13, -3327.6, -8857.57, -1668.24] | type_kill=random args=[2354.7164714194823, 1935.2311501096501, 2861.500986548548, 4226.959672447947, 8027.740770935707, -8035.217387464814, 8415.846425490956, -3095.2458013105424, 951.2129319477117, 7059.214002398043, 1314.4933955005017]
            ni.insert(len(ni), na)
    
    t = ''
    l = len(ni)

    ni = sorted(ni, reverse = True)
    n2 = 0
    n3 = 0

    while n3 != l:
        t += str(ni[n2])
        n3 += 1

        if n3 != l:
            t += ' '
            t += str(ni[l - 1 - n2])
            n3 += 1
        
        if n3 != l:
            n2 += 1    
            t += ' '
    
    return t


if __name__ == "__main__":
    item1 = sys.argv[1:][0]
    item2 = sys.argv[1:][1]
    item3 = sys.argv[1:][2]
    item4 = sys.argv[1:][3]
    item5 = sys.argv[1:][4]
    item6 = sys.argv[1:][5]
    item7 = sys.argv[1:][6]
    item8 = sys.argv[1:][7]
    item9 = sys.argv[1:][8]
    item10 = sys.argv[1:][9]
    item11 = sys.argv[1:][10]
    print(func(item1,item2,item3,item4,item5,item6,item7,item8,item9,item10,item11))