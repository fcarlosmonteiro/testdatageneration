import sys


def printArray(n, a, result):
    for i in range(len(a)):
        result += "{}[{}] = {} \n".format(n, str(i), str(a[i]))
    return result
 

def func(item1,item2,item3,item4,item5,item6,item7,item8,item9,item10,item11,item12,item13,item14,item15):
    list = [
        int(float(item1)),
        int(float(item2)),
        int(float(item3)),
        int(float(item4)),
        int(float(item5)),
        int(float(item6)),
        int(float(item7)),
        int(float(item8)),
        int(float(item9)),
        int(float(item10)),
        int(float(item11)),
        int(float(item12)),
        int(float(item13)),
        int(float(item14)),
        int(float(item15)),
    ]
    p = []
    im = []
    result = ''
    for i in range(15):
        x = list[i]
        if x % 2 == 0:
            p.insert(len(p), x)
        else:
            im.insert(len(im), x)
            
        if len(p) == 5:
            result += printArray('par', p, result)
            p = []
        
        if len(im) != 5: #PM | type_kill=weakly args=[-9325.48, -6804.24, -7041.67, 9142.34, -3979.01, 2756.02, -7339.76, -1981.6, 5044.98, 8381.71, -6773.15, -4842.0, -5068.5, 6740.81, 6041.17] | type_kill=strongly args=[-9325.48, -6804.24, -7041.67, 9142.34, -3979.01, 2756.02, -7339.76, -1981.6, 5044.98, 8381.71, -6773.15, -4842.0, -5068.5, 6740.81, 6041.17]
            result += printArray('impar', im, result)
            im = []

    result += printArray('impar', im, result)
    result += printArray('par', p, result)

    return result


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
    item12 = sys.argv[1:][11]
    item13 = sys.argv[1:][12]
    item14 = sys.argv[1:][13]
    item15 = sys.argv[1:][14]
    print(func(
      item1,item2,item3,item4,item5,
      item6,item7,item8,item9,item10,
      item11,item12,item13,item14,item15
    ))