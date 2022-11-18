'''
Created on 2014.9.1

@author: Garvin Li
'''

import sys

def insert_sort(item1,item2,item3,item4,item5):
    list=[item1,item2,item3,item4,item5]
   
    for i in range(1,len(list)):
        key=list[i]
        j=i-1
        while (j > 0 and key < list[j]): #PM | type_kill=weakly args=[2038.07, -2657.29, 5792.23, -7785.11, -6426.6] | type_kill=strongly args=[2038.07, -2657.29, 5792.23, -7785.11, -6426.6]
            list[j+1]=list[j]
            j-=1
        list[j+1]=key
    return list           


if __name__ == '__main__':
    item1 = float(sys.argv[1:][0])
    item2 = float(sys.argv[1:][1])
    item3 = float(sys.argv[1:][2])
    item4 = float(sys.argv[1:][3])
    item5 = float(sys.argv[1:][4])
    print(insert_sort(item1,item2,item3,item4,item5))
    