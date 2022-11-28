import matplotlib.pyplot as plt

x1 = [6,2,1]
y1 = [3,6,4]
plt.plot(x1, y1, label = "line 1")

x2 = [4,2,4]
y2 = [7,2,1]
plt.plot(x2, y2, label = "line 2")

x3 = [2,5,7]
y3 = [4,3,1]
plt.plot(x3, y3, label = "line 3")

x4 = [6,1,7]
y4 = [7,3,5]
plt.plot(x4, y4, label = "line 4")

x5 = [6,5,3]
y5 = [7,4,4]
plt.plot(x5, y5, label = "line 5")

x6 = [3,4,5]
y6 = [6,2,1]
plt.plot(x6, y6, label = "line 6")

plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('6 lines together')

plt.legend()
plt.show()