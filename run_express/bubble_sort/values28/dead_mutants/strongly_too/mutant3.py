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
            if list[i] < list[i + 1]: #PM | type_kill=weakly args=[-1685.76, -5180.7, -4310.5, -6901.81, 869.3] | type_kill=strongly args=[-1685.76, -5180.7, -4310.5, -6901.81, 869.3]
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