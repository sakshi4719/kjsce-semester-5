import numpy as np
import matplotlib.pyplot as plt

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

# TRAPEZOIDAL membership function
def trapezoidal_member(x, a, b, c, d, height):
    """Trapezoidal membership function"""
    if x <= a:
        return 0.0
    elif a < x < b:
        return ((x - a) / (b - a)) * height
    elif b <= x <= c:
        return height
    elif c < x < d:
        return ((d - x) / (d - c)) * height
    else:
        return 0.0
    
def fuzzy_union(setA, setB, setC):
    union = []
    for value in list(zip(setA, setB, setC)):
        union.append(max(value))
    return union

def fuzzy_product(setA, setB):
    product = []
    for value1, value2 in list(zip(setA, setB)):
        product.append(round(value1 * value2, 3))
    return product

# Plot the membership functions and operations
x_values = np.linspace(0, 10, 500)

# Function 1
a, b, c, d, h = 0, 3, 6, 8, 0.5
y_values_func1 = [trapezoidal_member(x, a, b, c, d, h) for x in x_values]

# Function 2
a, b, c = 6, 8, 10
y_values_func2 = [triangular_member(x, a, b, c) for x in x_values]

# Fuzzy set (obtained by taking union of functions defined above)
plt.plot(x_values, y_values_func1, 'blue')
plt.plot(x_values, y_values_func2, 'blue')
plt.title('Center of Sums Method')
plt.xlabel('X-axis')
plt.ylabel('Membership Value')

def centerOfSums(x_values, func1, func2):
    A1 = np.trapz(func1, x_values)
    X1 = np.trapz(fuzzy_product(func1, x_values), x_values) / np.trapz(func1, x_values)
    A2 = np.trapz(func2, x_values)
    X2 = np.trapz(fuzzy_product(func2, x_values), x_values) / np.trapz(func2, x_values)
    crisp_value = (A1 * X1 + A2 * X2) / (A1 + A2)
    crisp_value = round(crisp_value, 3)
    plt.axvline(x=crisp_value, color='r', linestyle='--', label=f'x = {crisp_value}')
    plt.axhline(y=0, color='black')
    plt.legend()
    plt.show()

centerOfSums(x_values, y_values_func1, y_values_func2)