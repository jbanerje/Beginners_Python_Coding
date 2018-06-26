# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 21:27:00 2017
Pie Chart
@author: jagan
"""

#Import Library
import matplotlib.pyplot as plt

#Main Function
def main():
    gases=['nitrogen','oxygen','argon','hydrogen']
    sizes=[15,30,45,10]
    explode=(0,0.1,0,0.1)
    
    plt.pie(sizes,explode=explode, labels=gases, autopct='%1.1f%%',shadow=True,startangle=90,counterclock=False)
    #plt.pie(sizes,labels=gases, autopct='%1.1f%%',shadow=True,startangle=90)
    plt.axis('equal')
    plt.show()
    
if __name__=="__main__":
    main()