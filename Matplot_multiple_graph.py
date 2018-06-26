import matplotlib.pyplot as plt
fig = plt.figure()
rect= fig.patch
rect.set_facecolor('green')


x=[1,2,3,4]
y=[1,2,3,4]
y2=[1,4,9,16]
y3=[1,8,27,64]

#Graph1
graph1 = fig.add_subplot(3,3,1,axisbg='black')  #Subplot - row,column,graph#
graph1.plot(x,y,'r--',lw=2)
graph1.tick_params(axis="x",color='w')
graph1.tick_params(axis="y",color='w')

graph1.set_title("Graph-1") # Adds title to graph
graph1.set_xlabel("X") # Adds X axis label
graph1.set_ylabel("Y=X") # Adds Y axis label

#Graph2
graph2 = fig.add_subplot(3,3,2,axisbg='black')
graph2.plot(x,y2,'g--',lw=2)
graph2.tick_params(axis="x",color='w')
graph2.tick_params(axis="y",color='w')

graph2.set_title("Graph-2") # Adds title to graph
graph2.set_xlabel("X") # Adds X axis label
graph2.set_ylabel("Y=X^2") # Adds Y axis label


#Graph3
graph3 = fig.add_subplot(3,3,3,axisbg='black')
graph3.plot(x,y3,'b--',lw=2)
graph3.tick_params(axis="x",color='w')
graph3.tick_params(axis="y",color='w')

graph3.set_title("Graph-3") # Adds title to graph
graph3.set_xlabel("X") # Adds X axis label
graph3.set_ylabel("Y=X^3") # Adds Y axis label

plt.show()