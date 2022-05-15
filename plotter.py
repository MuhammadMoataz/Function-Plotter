# importing the required module
import matplotlib.pyplot as plt
import numpy as np

# x axis values
x = np.arange(-10, 10, 0.1)
# corresponding y axis values
# y = input("Enter the equation: ")
y = 5*x

# plotting the points
plt.plot(x, y, label = "first line")



# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')

# giving a title to my graph
plt.title('My first graph!')

#show legend
plt.legend()
# function to show the plot
plt.show()
