# -*- coding: utf-8 -*-
"""
Created on Sun May 28 12:15:50 2017

@author: jagan
"""

inp_num_1 = int(input("Enter number:"))
remainder = ( inp_num_1 % 2 )

if (remainder == 0):
    print("Even Number:", inp_num_1)
else:
    print("Odd Number:", inp_num_1)