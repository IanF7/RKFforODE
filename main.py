# Ian Fletcher
# CST-305
# 2/5/2022
# Using RKF to solve ODEs

# imports numpy, scipy odeint package, and matplotlib
import numpy as np
from scipy.integrate import odeint
from matplotlib import pyplot as plt


# n: number of steps
n = 1000
# y0: initial y value
y0 = 1
# x0: initial x value
x0 = 2
# h: step size
h = 0.3
x_vals = [x0]
y_vals = [y0]
count = 0


# function f containing the equation and returns dy_dx
def f(y, x):
    # sets dy_dx equal to the equation given
    # dy_dx = -y + np.log(x)
    # returns dy_dx
    return -y + np.log(x)


# for loop that uses RKF formula to solve for the next x and y values
for i in range(n):
    # sets k1 equal to the results of f given x0 and y0
    k1 = f(y0, x0)
    # sets k2 equal to the results of f given x0 + (h/2) and y0 + (h/2) * k1
    k2 = f((y0 + ((h/2) * k1)), (x0 + (h/2)))
    # sets k3 equal to the results of f given x0 + (h/2) and y0 + (h/2) * k2
    k3 = f((y0 + ((h/2) * k2)), (x0 + (h/2)))
    # sets k4 equal to the results of f given x0 + h and y0 + (h * k3)
    k4 = f((y0 + (h * k3)), (x0 + h))
    # sets y0 equal to the new value of y using RKF formula
    y0 = y0 + (h * (1/6) * (k1 + (2 * k2) + (2 * k3) + k4))
    # sets x0 equal to the new value of x
    x0 = round(x0 + h, 2)
    # adds values to x and y arrays
    x_vals.append(x0)
    y_vals.append(y0)
    # checks if count is less than 5
    if count < 5:
        # prints out step number, new x value, and new y value
        print("x: " + str(x0), "y: " + str(y0))
    # increments count
    count += 1

# plots results
plt.title("Equation Solved With RKF")
plt.plot(x_vals, y_vals, 'b--', linewidth=1)
plt.xlabel('X')
plt.ylabel('Y')
plt.show()


# resets y0
y0 = 1
# sets y equal to results
result = odeint(f, y0, x_vals)
# prints first 5 values
for i in range(6):
    print("x: " + str(x_vals[i]), "y: " + str(result[i]))
# plots results
plt.plot(x_vals, result, 'r--', linewidth=1)
plt.title("Equation Solved With odeint")
plt.xlabel('X')
plt.ylabel('Y')
plt.show()


# plots both graphs
plt.plot(x_vals, y_vals, 'b-', linewidth=1, label="RKF")
plt.plot(x_vals, result, 'r--', linewidth=1, label="odeint")
plt.title("RKF Formula Compared to odeint")
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()
