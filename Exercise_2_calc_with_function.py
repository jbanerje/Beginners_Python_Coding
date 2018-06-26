# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 21:52:07 2017

@author: jagan
"""


def sum(num1,num2):
    result = (num1 + num2)
    return(result)


def diff(num1,num2):
    result = (num1 - num2)
    return(result)

    
def main():
    #input
    num1=float(input("First Number:"))
    num2=float(input("Second Number:"))
    
    #Calculation
    result_sum = sum(num1,num2)
    result_diff = diff(num1,num2)
    #result_mul = (num1 * num2)
    #result_divide = (num1 / num2)
    
    #Print Result
    print("Sum-",result_sum)
    print("Dif-",result_diff)
    #print("Mul-",result_mul)
    #print("Div-",result_divide)
    

if __name__ == "__main__":
    main()