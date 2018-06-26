import random
import sys
import os
import matplotlib.pyplot as plt
import numpy as np

names = ['Jag', 'aaa', 'bbb', 'ccc', 'ddd', 'eee']
pos = np.arange(6) + 0.5

#horizontal bar chart
plt.barh(pos,(4,8,12,3,17,6),align='center',color='red')

#labeling the graph
plt.xlabel('Height in Inches',color='red')
plt.ylabel('Students',color='red')
plt.title('Height of students',color='blue')
plt.tick_params(axis="x",color="white")
plt.tick_params(axis="y",color="white")
plt.yticks(pos,names)
plt.show()