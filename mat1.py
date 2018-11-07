import numpy as np
import matplotlib.pyplot as plt


x1 = np.random.rand(100)*0.5
y1 = np.random.rand(100)*0.5

x2 = np.random.rand(100)*0.5 + 0.5
y2 = np.random.rand(100)*0.5

x3 = np.random.rand(100)*0.5
y3 = np.random.rand(100)*0.5 + 0.5

x4 = np.random.rand(100)*0.5 + 0.5
y4 = np.random.rand(100)*0.5 + 0.5

fig = plt.figure()

ax = fig.add_subplot(1,1,1)

ax.scatter(x1,y1, c='red', label='group1')
ax.scatter(x2,y2, c='blue', label='group2')
ax.scatter(x3,y3, c='green', label='group3')
ax.scatter(x4,y4, c='yellow', label='group4')

ax.set_title("Our lady's Area")
ax.set_xlabel('x')
ax.set_ylabel('y')

ax.grid(True)

ax.legend(loc='upper left')
plt.show()
