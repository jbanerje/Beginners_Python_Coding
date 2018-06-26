# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 21:37:13 2017
Basic Calculator with 2 inputs and it will print sum,diff,multiplication,division
without a function
@author: jagan
"""

def main():
    #input
    num1=float(input("First Number:"))
    num2=float(input("Second Number:"))
    
    #Calculation
    result_sum = (num1 + num2)
    result_diff = (num1 - num2)
    result_mul = (num1 * num2)
    result_divide = (num1 / num2)
    
    #Print Result
    print("Sum-",result_sum)
    print("Dif-",result_diff)
    print("Mul-",result_mul)
    print("Div-",result_divide)
    

if __name__ == "__main__":
    main()