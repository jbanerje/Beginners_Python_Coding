from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt

fig=plt.figure()
# 3D Scatter module
chart = fig.add_subplot(1,1,1,projection='3d')
x,y,z=[1,2,3,4,5,6,7,8],[2,5,3,8,9,5,6,1],[3,6,2,7,5,4,5,6]
chart.scatter(x,y,z,c='red',marker='o')
chart.set_xlabel('x axis')
chart.set_ylabel('y axis')
chart.set_zlabel('z axis')
plt.show()
