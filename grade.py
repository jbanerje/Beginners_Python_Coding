# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 16:19:28 2017

@author: jagan
"""

input_eng = int(input("Enter a english:"))
input_math = int(input("Enter a math:"))
input_sci = int(input("Enter a science:"))

average= (input_eng + input_math + input_sci) // 3
if ( average >= 80 ):
    print("grade = 4")
    
elif ( average > 60 ) and ( average < 80 ) :
    print("grade = 3")
    
else:
    print("grade = 2")