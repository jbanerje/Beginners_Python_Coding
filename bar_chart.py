import numpy as np
import matplotlib.pyplot as plt

ind = np.array(['Tom', 'Dan', 'Harry'])   # the x locations for the groups
width = 0.25       # the width of the bars: can also be len(x) sequence
menMeans = (20, 35, 30)

p1 = plt.bar(ind, menMeans, width)

plt.xlabel('Name')
plt.ylabel('Scores')
plt.title('Scores by group and gender')

plt.legend('Name')
plt.show()
