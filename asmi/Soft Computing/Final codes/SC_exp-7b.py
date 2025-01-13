import matplotlib.pyplot as plt
import numpy as np
from tabulate import tabulate

# TRIANGULAR membership function
def triangular_member(x, a, b, c):
    """Triangular membership function"""
    if x <= a:
        return 0.0
    elif a < x <= b:
        return (x - a) / (b - a)
    elif b < x <= c:
        return (c - x) / (c - b)
    else:
        return 0.0

# Define parameters
a_values = [0, 5, 10, 15]
b_values = [4, 11, 18, 22]
c_values = [10, 15, 25, 30]
parameters = parameters = list(zip(a_values, b_values, c_values))

# Calculate membership values for different ranges
table = []                      # To store results
input_values = [7, 12, 19, 23]  # Input values

for x in input_values:
    row = [f"x = {x}"]
    for a, b, c in parameters:
        result = triangular_member(x, a, b, c)
        row.append(round(result, 3))
    table.append(row)

headers = ["Input Value"] + [f"Range [{a}, {c}]" for a, b, c in parameters]
print("\nTriangular Membership")
print(tabulate(table, headers, tablefmt="grid"))

# Create plots for each triangular membership function
x_values = np.linspace(0, 30, 500)
for a, b, c in zip(a_values, b_values, c_values):
    y_values = [triangular_member(x, a, b, c) for x in x_values]
    plt.plot(x_values, y_values, label=f'({a}, {b}, {c})')

plt.xlabel('X-axis')
plt.ylabel('Degree of Belonging')
plt.title('Triangular Membership Functions')
plt.legend()
plt.show()

# TRAPEZOIDAL membership function
def trapezoidal_member(x, a, b, c, d):
    """Trapezoidal membership function"""
    if x <= a:
        return 0.0
    elif a < x < b:
        return (x - a) / (b - a)
    elif b <= x <= c:
        return 1.0
    elif c < x < d:
        return (d - x) / (d - c)
    else:
        return 0.0

# Define parameters
a_values = [0, 5, 10, 15]
b_values = [3, 8, 15, 21]
c_values = [7, 11, 20, 25]
d_values = [10, 15, 25, 30]
parameters = list(zip(a_values, b_values, c_values, d_values))

# Calculate membership values for different ranges
table = []                      # To store results
input_values = [6, 12, 14, 23]  # Input values

for x in input_values:
    row = [f"x = {x}"]
    for a, b, c, d in parameters:
        result = trapezoidal_member(x, a, b, c, d)
        row.append(round(result, 3))
    table.append(row)

headers = ["Input Value"] + [f"Range [{a}, {d}]" for a, b, c, d in parameters]
print("\nTrapezoidal Membership")
print(tabulate(table, headers, tablefmt="grid"))

# Create plots for each trapezoidal membership function
x_values = np.linspace(0, 30, 500)
for a, b, c, d in zip(a_values, b_values, c_values, d_values):
    y_values = [trapezoidal_member(x, a, b, c, d) for x in x_values]
    plt.plot(x_values, y_values, label=f'({a}, {b}, {c}, {d})')

plt.xlabel('X-axis')
plt.ylabel('Degree of Belonging')
plt.title('Trapezoidal Membership Functions')
plt.legend()
plt.show()

# GAUSSIAN membership function
def gaussian_member(x, center, sd):
    """Gaussian membership function"""
    return np.exp(-0.5 * ((x - center) / sd) ** 2)

# Define parameters
center = 7
std_dev = 2
parameters = [(center, std_dev)]

# Create plot for gaussian membership function
x_values = np.linspace(0, 15, 500)
for center, sd in parameters:
    y_values = [gaussian_member(x, center, sd) for x in x_values]
    plt.plot(x_values, y_values, label=f'Center={center}, SD={sd}')

plt.xlabel('X-axis')
plt.ylabel('Degree of Belonging')
plt.title('Gaussian Membership Functions')
plt.legend()
plt.show()

# GENERALIZED membership function
def generalized_member(x, sd, mean, center):
    """Generalized membership function"""
    return 1 / (1 + np.abs((x - center) / sd) ** (2 * mean))

# Define parameters
std_dev = 2
mean = 3
center = 7
parameters = [(std_dev, mean, center)]

# Create plot for generalized membership function
x_values = np.linspace(0, 15, 500)
for sd, mean, center in parameters:
    y_values = [generalized_member(x, sd, mean, center) for x in x_values]
    plt.plot(x_values, y_values, label=f'SD={sd}, Mean={mean}, Center={center}')

plt.xlabel('X-axis')
plt.ylabel('Degree of Belonging')
plt.title('Generalized Membership Functions')
plt.legend()
plt.show()

# SIGMOIDAL membership function
def sigmoidal_member(x, a, b):
    """Sigmoidal membership function"""
    return 1 / (1 + np.exp(-a * (x - b)))

# Define parameters
a = 1
b = 0
parameters = [(a, b)]

# Create plot for generalized membership function
x_values = np.linspace(-10, 10, 500)
for a, b in parameters:
    y_values = [sigmoidal_member(x, a, b) for x in x_values]
    plt.plot(x_values, y_values, label=f'a={a}, b={b}')

plt.xlabel('X-axis')
plt.ylabel('Degree of Belonging')
plt.title('Sigmoidal Membership Functions')
plt.legend()
plt.show()