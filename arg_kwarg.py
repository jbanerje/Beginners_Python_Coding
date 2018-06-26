# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 17:33:23 2017

@author: jagan
"""

#*arg(Simple Argument)   & **kwarg(Keyword Argument)
#* - Non Keyword variables ; args is idiom and not enforced

def normal_function(var1,var2):
    print("var1:",var1)
    print("var2:",var2)
    
def normal_funtion_one_var(var1,*arg):
    print("var1:",var1)
    for item in arg:
        print("Rest of the data:",item)

def normal_funtion_two_var(var1,var2,*arg):
    print("var1:",var1)
    print("var2:",var2)
    for item in arg:
        print("Rest of the data:",item)
        
def normal_funtion_arg_only(*arg):
    for item in arg:
        print("Rest of the data:",item)

#normal_function('hello','python')
#normal_funtion_one_var('hello','python','jagan','iot','mobile','ML')
#normal_funtion_two_var('hello','python','jagan','iot','mobile','ML')
normal_funtion_arg_only('hello','python','jagan','iot','mobile','ML')