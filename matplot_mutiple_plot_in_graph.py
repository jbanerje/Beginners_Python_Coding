# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 20:41:49 2017

@author: jagan
"""

import matplotlib.pyplot as plt
plt.plot([1,2,3,4],[1,2,3,4],'g',lw=5)
plt.axis([0, 6, 0, 30])
#Options with Plot - r,r+,b+,r--,g^,ro,bo#

plt.title("Matplot Class - First Graph") # Adds title to graph
plt.xlabel("This is X axis") # Adds X axis label
plt.ylabel("This is X axis") # Adds Y axis label
plt.show()

import matplotlib.pyplot as plt
fig = plt.figure()
rect= fig.patch
rect.set_facecolor('green')
graph1 = fig.add_subplot(1,1,1,axisbg='black')

x=[1,2,3,4]
y=[1,2,3,4]
y2=[1,4,9,16]
y3=[1,8,27,64]


graph1.plot(x,y,'r--',lw=2)
graph1.plot(x,y2,'g--',lw=2)
graph1.plot(x,y3,'b--',lw=2)

graph1.tick_params(axis="x",color='w')
graph1.tick_params(axis="y",color='w')

graph1.spines["top"].set_color='w'
graph1.spines["bottom"].set_color='w'
graph1.spines["left"].set_color='w'
graph1.spines["right"].set_color='w'
plt.title("Matplot Class - First Graph") # Adds title to graph
plt.xlabel("This is X axis") # Adds X axis label
plt.ylabel("This is Y axis") # Adds Y axis label


plt.show()