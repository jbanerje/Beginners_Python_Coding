#Matplotlib Template

import numpy as np
import matplotlib.pyplot as plt

# Make an array of x values
x = [1, 2, 3, 4, 5]
# Make an array of y values for each x value
y = [1, 4, 9, 16, 25]
# Make an array of Z values for each x value
z = [2, 4, 6, 8, 10]

# use pylab to plot x and y
plt.plot(x, y, linewidth=3,label='sin(x)',c='#FF4500') #Red
plt.plot(x, z,  label='cos(x)', c='#4682B4',) #Blue
# show the plot on the screen
plt.legend(loc='best')
plt.show()
