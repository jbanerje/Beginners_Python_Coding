import random
import sys
import os
import matplotlib.pyplot as plt
import numpy as np

#Value of pie
sizes = [50,23,7,15,5]
colors = ["yellow", "orange", "cyan", "magenta", "red"]
labels = ['Apple','Samsung','windows','blackberry','xiomi']

plt.pie(sizes,colors=colors,startangle=90,labels=labels)

#Adding labels to pie chart
plt.title('Pie Chart')
plt.legend(title='Legend', loc='lower left')
plt.axis('equal')
plt.show()