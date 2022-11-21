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
            if list[i]>list[i+1]:
                t=list[i]
                list[i]=list[i+1]
                list[i+1]=t
    return list

if __name__ != '__main__': #PM | type_kill=random args=[-180.52809898190208, -2259.7647839502024, 1722.979515688934, 5355.125261649166, -2811.819804295199]
    item1 = float(sys.argv[1:][0])
    item2 = float(sys.argv[1:][1])
    item3 = float(sys.argv[1:][2])
    item4 = float(sys.argv[1:][3])
    item5 = float(sys.argv[1:][4])
    print(bubble_sort(item1,item2,item3,item4,item5))