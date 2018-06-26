#Matplotlib - Line plot

import matplotlib.pyplot as plt

x = [1,2,3,4]
y = [1,4,9,16]
z = [1,8,27,64]

plt.plot(x, y,'r--',label='red line')
plt.plot(x, z,'g--',label='green line')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Test -  Line Plot')
plt.legend() #Loc=2
plt.show()
