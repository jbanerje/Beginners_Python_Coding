# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 21:11:36 2017

@author: jagan
"""
import matplotlib.pyplot as plt

#Creation of axis
x=[1,2,3,4]
y=[1,2,3,4]
y2=[1,4,9,16]
y3=[1,8,27,64]

#Plotting axis
#plt.axis([0, 4, 0, 10])

#plotting x & y
plt.plot(x,y,'r--',linewidth=2,label='red line')
plt.plot(x,y2,'g--',linewidth=2,label='green line')
plt.plot(x,y3,'y--',linewidth=2,label='yellow line')

#label axis
plt.title("Matplot Class - First Graph") # Adds title to graph
plt.xlabel("Year")
plt.ylabel("Income")
plt.legend()

#launch the graph
plt.show()


