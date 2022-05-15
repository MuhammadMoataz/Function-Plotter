# importing the required module
import matplotlib.pyplot as plt
import numpy as np

# x axis values
x_min = np.double(input("x min: "))
x_max = np.double(input("x max: "))
x = np.arange(x_min, x_max, 0.01)
# corresponding y axis values
# y = input("Enter the equation: ")
# y : np.ndarray
y = 5*x**2 + 3*x
# y = np.ndarray(input("Enter the equation: "))

# plotting the points
plt.plot(x, y)



# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')

# giving a title to my graph
plt.title('Function Plotter!')

#show legend
# plt.legend()
# function to show the plot
plt.show()
