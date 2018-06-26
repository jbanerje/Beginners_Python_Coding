"""
Created on Tue Nov 28 21:27:00 2017
Scatter Plot
@author: jagan
"""

#Import Library
import matplotlib.pyplot as plt

#Main Function
def main():
    #Creation of axis
    x=[1,2,3,4,5,6,7,8,9,10,11,12]
    y=[2,4,6,2,6,12,4,3,6,5,3,2]
    z=[4,2,2,6,4,3,5,6,7,8,2,3]

    #plotting x & y
    plt.scatter(x,y,c='red',label='Chicken Pox')
    plt.scatter(x,z,c='green',label='Measels')

    #label axis
    plt.title("Matplot Class - Scatter Plot") # Adds title to graph
    plt.xlabel("X Axis")
    plt.ylabel("Y Axis")
    plt.legend()
    plt.show()
    
if __name__=="__main__":
    main()