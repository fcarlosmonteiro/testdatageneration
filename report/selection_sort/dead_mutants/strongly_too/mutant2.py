'''
Created on 2014.9.3

@author: Garvin
'''

import sys
  
def selection_sort(item1,item2,item3,item4,item5):
    list=[item1,item2,item3,item4,item5]
    i=0
    j=0
    while i>=0 and i<=(len(list)-1):
        while not ((j >= i and j <= len(list) - 1)): #PM | type_kill=weakly args=[-8065.69, -5176.6, 2542.86, -8596.88, -4756.22] | type_kill=strongly args=[-8065.69, -5176.6, 2542.86, -8596.88, -4756.22]
            if list[i]>list[j]:
                t=list[i]
                list[i]=list[j]
                list[j]=t
            j+=1
        i+=1
        j=i      
    return list
  
if __name__ == '__main__':
    item1 = float(sys.argv[1:][0])
    item2 = float(sys.argv[1:][1])
    item3 = float(sys.argv[1:][2])
    item4 = float(sys.argv[1:][3])
    item5 = float(sys.argv[1:][4])
    print(selection_sort(item1,item2,item3,item4,item5))   
               
          