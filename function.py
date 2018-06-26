# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 21:20:35 2017

@author: jagan
"""
#Defining the function
def _sum(a,b):
    return(a+b,a-b,a*b,a/b)
    
#main
def main():
    summ,diff,mul,div=sum(10,5)
    print("Summ:",summ,"\n","diff:",diff)

#Main Function Call
if __name__ == "__main__":
    main()


    
