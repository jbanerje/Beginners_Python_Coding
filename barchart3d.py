from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

fig=plt.figure()
# Multiple 3D Bar Chart
chart = fig.add_subplot(1,1,1,projection='3d')

x=[1,2,3,4,5,6,7,8,9,10]
y=[2,3,4,5,1,6,2,1,7,2]
z=[0,0,0,0,0,0,0,0,0,0]

dx=np.ones(10)
dy=np.ones(10)
dz=[1,2,3,4,5,6,7,8,9,10]

chart.bar3d(x,y,z,dx,dy,dz,color='cyan')
chart.set_xlabel('x axis')
chart.set_ylabel('y axis')
chart.set_zlabel('z axis')

plt.show()
