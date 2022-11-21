import sys

def func(item1,item2,item3,item4,item5):
    list = [float(item1),float(item2),float(item3),float(item4),float(item5)]
    even=0
    odd=0
    positive=0
    negative=0
    for i in range(5):
        if(list[i] % 2 == 0):
            even = even+1
        else:
            odd =odd+1
        if (list[i] > 0):
            positive =positive+1
        elif (list[i] < 0):
            negative =negative+1

    result = "{} valor(es) par(es), ".format(even)
    result += "{} valor(es) impar(es), ".format(odd)
    result += "{} valor(es) positivo(s) e ".format(positive)
    result += "{} valor(es) negativo(s)".format(negative)

    return result


if not (__name__ == '__main__'): #PM
    item1 = float(sys.argv[1:][0])
    item2 = float(sys.argv[1:][1])
    item3 = float(sys.argv[1:][2])
    item4 = float(sys.argv[1:][3])
    item5 = float(sys.argv[1:][4])
    print(func(item1,item2,item3,item4,item5))