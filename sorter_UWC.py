# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import random

lst_1 = [number for number in range(1,91)]
lst_3 = [number for number in range(1,91)]
lst_2 = [number for number in range(1,91)]

rev_lst = np.zeros([9,30],dtype=int)

random.shuffle(lst_1)
random.shuffle(lst_2)
random.shuffle(lst_3)

for i in range(30):
    for u in range(3):
        rev_lst[u,i] = lst_1[i]
        rev_lst[1,i] = lst_2[i]
        rev_lst[2,i] = lst_3[i]
        j = i+30
        rev_lst[u+3,i] = lst_1[j]
        rev_lst[4,i] = lst_2[j]
        rev_lst[5,i] = lst_3[j]
        k = j+30
        rev_lst[u+6,i] = lst_1[k]
        rev_lst[7,i] = lst_2[k]
        rev_lst[8,i] = lst_3[k]
    
print(rev_lst)

num_col = 30*9
print(num_col)


def bubbleSort(arr): 
    n = 30 
  
    for l in range(9):
        for i in range(29): 
 
     
            for j in range(0, 30-i-1): 
      
                # traverse the array from 0 to n-i-1 
                # Swap if the element found is greater 
                # than the next element 
                if arr[l,j] > arr[l,j+1]: 
                    arr[l,j], arr[l,j+1] = arr[l,j+1], arr[l,j] 
                    
bubbleSort(rev_lst)



print(rev_lst)
        
b = 0

for k in range(1,91):
    bandera = 0
    for i in range(9):
        for j in range(30):
            if rev_lst[i,j] == k:
                bandera = bandera + 1
    if bandera > 3:
        print("ALERTA")
        b = b+1

print(b)

dicts = {}

for i in range(9):
    dicts[i] = rev_lst[i,:]
    

import xlsxwriter

workbook = xlsxwriter.Workbook('arrays.xlsx')
worksheet = workbook.add_worksheet()


row = 0

for col, data in enumerate(rev_lst):
    worksheet.write_column(row, col, data)

workbook.close()









    
