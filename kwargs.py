# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 17:45:31 2017

@author: jagan
"""

def normal_function(var1,var2):
    print("var1:",var1)
    print("var2:",var2)

# ** is used to pass keyworded, variable length argument dictionary to a function
def learn_kwarg_function(**kwargs):
    print(kwargs)  # It will create a dictionary; underoredred

def learn_kwarg_function_1(**kwargs):
    for key,value in kwargs.items():
        print("The value of ",key,"is ",value)
    
#normal_function('hello','python')
#learn_kwarg_function(kwarg_1="Tuna",kwarg_2="Talapia",kwarg_3="Salmon")
learn_kwarg_function_1(kwarg_1="Tuna",kwarg_2="Talapia",kwarg_3="Salmon")