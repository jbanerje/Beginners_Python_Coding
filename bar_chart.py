# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 21:18:31 2017

@author: jagan
"""

#Import Library
import matplotlib.pyplot as plt
import numpy as np

#Main Function
def main():
    N= 5
    width = 0.35
    
    #Data for the bar chart
    men_score=(75,70,98,62,55)
    wom_score=(65,77,98,85,63)
    
    ind = np.arange(N)
    
    p1=plt.bar(ind,men_score,width)
    p2=plt.bar(ind,wom_score,width)
    
    #label axis
    plt.title("Matplot Class - Bar Chart") # Adds title to graph
    plt.xlabel("Number")
    plt.ylabel("Score")
    plt.legend((p1[0],p2[0]),('Men','Women'))
    plt.show()
    
if __name__=="__main__":
    main()