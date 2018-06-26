# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 22:04:04 2017

@author: jagan
"""
#Function to calculate sum
def sum(num1,num2):
    result = (num1 + num2)
    return(result)

def diff(num1,num2):
    result = (num1 - num2)
    return(result)

def mul(num1,num2):
    result = (num1 * num2)
    return(result)

def div(num1,num2):
    result = (num1 / num2)
    return(result)
    
def main():
    #input
    
    num1=float(input("First Number:"))
    num2=float(input("Second Number:"))
    user_choice_operator = input("Please enter an operator:")
    
    if (user_choice_operator == '+'):
        result = sum(num1,num2)
        
    elif (user_choice_operator == '-'):
        result = diff(num1,num2)


    elif (user_choice_operator == '*'):
        result = mul(num1,num2)
        
    elif (user_choice_operator == '/'):
        result = div(num1,num2)
        
    else:
        result="Incorrect Choice"
    
    #Calculation
    print("Result;",result)
    

if __name__ == "__main__":
    main()