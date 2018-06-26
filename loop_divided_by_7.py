# -*- coding: utf-8 -*-
"""
Created on Sun Jul 16 16:58:40 2017

Write a Python program to find those numbers which are 
divisible by 7 between 1 and 100 (both included)

@author: jagan
"""
list1=[] 

for counter in range(1500,2700, 1):
    if (counter % 7) == 0 and (counter % 5) == 0:
        list1.append(counter)
print(list1)

for item in list1: 
    if item == 2275:
        print("\nfound the item")
