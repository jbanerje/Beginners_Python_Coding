# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 22:04:04 2017

@author: jagan
"""
#Function to calculate sum
def sum(*sumofallnum):
    result=0
    for element in sumofallnum:
        result=result + element
        return(result)

    
def main():
    #input
    result=sum(1,2,3,4,5,6,7)
    print("Result:",result)

if __name__ == "__main__":
    main()

