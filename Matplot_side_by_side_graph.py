import numpy as np
import matplotlib.pyplot as plt

#Strategy-1
#The data
womenMeans = (25, 32, 34, 20, 25)
menMeans = (20, 35, 30, 35, 27)
indices = [5.5,6,7,8.5,8.9]

#Calculate optimal width
width = np.min(np.diff(indices))/3
plt.bar(indices-width,womenMeans,width,color='b',label='-Ymin')
plt.bar(indices,menMeans,width,color='r',label='Ymax')
plt.xlabel('Test histogram')
plt.show()

#Strategy-2
data = [[5., 25., 50., 20.],
  [4., 23., 51., 17.],
  [6., 22., 52., 19.]]

X = np.arange(4)
plt.bar(X + 0.00, data[0], color = 'b', width = 0.25)
plt.bar(X + 0.25, data[1], color = 'g', width = 0.25)
plt.bar(X + 0.50, data[2], color = 'r', width = 0.25)

plt.show()