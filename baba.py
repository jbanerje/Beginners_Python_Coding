# -*- coding: utf-8 -*-
"""
Created on Sun May  7 17:55:48 2017
#working with list

@author: jagan
"""
list1= ['a', 'hello', 1.5, 5.6, 2, 0]
print (len(list1))

list1.reverse()
print (list1)

list3=list1.copy()
print (list3)

print (list1 [2:5])

print (list1 * 3)

list1.append ("world")
print (list1)