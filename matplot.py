# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 18:19:04 2017

@author: jagan
"""

import matplotlib.pyplot as plt
#plt.plot([1,2,3], [1,4,9], 'rs',  label='line 2')
#plt.plot([1,2,3], [1,2,3], 'go-', label='line 1', linewidth=2)
x = [1,2,3,4,5]
y = [1,4,9,16,25]

#plt.plot(x, y)        # plot x and y using default line style and color
plt.plot(x, y, 'b-')  # plot x and y using blue circle markers
#plt.plot(x,y, 'b+')     # ditto, but with red plusses
plt.xlabel('number')
plt.ylabel('square of numbe')
plt.axis([0, 6, 0, 30])

import numpy as np
import matplotlib.pyplot as plt

# evenly sampled time at 200ms intervals
x = [0,1,2,3,4,5]
y = [0,1,4,9,16,25]
z = [0,1,8,27,64,125]

plt.xlabel('number')
plt.ylabel('Multiple of number')
plt.axis([0, 5, 0, 125])
plt.title('Simple plot')
plt.legend([x,y], ["line 2", "line 1"])
# red dashes, blue squares and green triangles
plt.plot(x, x, 'r--', x, y, 'b', x, z, 'g')
plt.show()


import numpy as np
import matplotlib.pyplot as plt

x = [0,1,2,3,4,5]
y = [0,1,4,9,16,25]
z = [0,1,8,27,64,125]

#plt.figure(1)
plt.subplot(111)
plt.plot(x,y, 'bo')
plt.xlabel('number')
plt.ylabel('Multiple of number')
plt.axis([0, 5, 0, 125])

plt.subplot(212)
plt.plot(x,z, 'ro')
plt.xlabel('number')
plt.ylabel('Multiple of number')
plt.axis([0, 5, 0, 125])

plt.show()


