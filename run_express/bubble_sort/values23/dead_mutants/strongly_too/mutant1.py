'''
Created on 2014.9.3

@author: Garvin
'''

import sys

def bubble_sort(item1,item2,item3,item4,item5):
    list=[item1,item2,item3,item4,item5]
    dist=len(list)
    for j in range(0,dist):
        for i in range(0,dist-1):
            if not (list[i] > list[i + 1]): #PM | type_kill=weakly args=[5875.91, 3196.06, 152.33, -8777.52, 9156.24] | type_kill=strongly args=[5875.91, 3196.06, 152.33, -8777.52, 9156.24]
                t=list[i]
                list[i]=list[i+1]
                list[i+1]=t
    return list

if __name__ == '__main__':
    item1 = float(sys.argv[1:][0])
    item2 = float(sys.argv[1:][1])
    item3 = float(sys.argv[1:][2])
    item4 = float(sys.argv[1:][3])
    item5 = float(sys.argv[1:][4])
    print(bubble_sort(item1,item2,item3,item4,item5))