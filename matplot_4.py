import random
import sys
import os
import matplotlib.pyplot as pt

#Multiple lines to a graph

x=[0,7,8,12]
y=[0,13,2,12]

x2=[0,4,7,12]
y2=[0,7,1,12]

x3=[0,4,6,12]
y3=[0,5,8,12]

fig = pt.figure()
rect = fig.patch
rect.set_facecolor('green')

graph1 = fig.add_subplot(1,1,1,axisbg='black')
graph1.plot(x,y,'red',linewidth=4)
graph1.plot(x2,y2,'yellow',linewidth=2.0)
graph1.plot(x3,y3,'orange',linewidth=6.0)

graph1.tick_params(axis="x",color="white")
graph1.tick_params(axis="y",color="white")

graph1.spines["top"].set_color('w')
graph1.spines["bottom"].set_color('w')
graph1.spines["left"].set_color('w')
graph1.spines["right"].set_color('w')
graph1.set_title('Random Graph', color="white")
graph1.set_xlabel('This is X axis',color="white")
graph1.set_ylabel('This is Y axis',color="white")
pt.show()