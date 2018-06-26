# -*- coding: utf-8 -*-
"""
Created on Sun Jul 16 16:33:47 2017

@author: jagan
"""
list1 = ['apple','orange','banana','grapes','kiwi']

list2 = []

for item in list1:
    if (item =='orange'):
        print ("I found it!")
        list2.append(item)
print(list2)
    #else:
        #print("couldn't find")