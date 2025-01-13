import numpy as np
import matplotlib.pyplot as plt

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
x_values = np.linspace(0, 8, 500)

# Function 1
a, b, c, d, h = 0, 1, 4, 5, 0.3
y_values_func1 = [trapezoidal_member(x, a, b, c, d, h) for x in x_values]

# Function 2
a, b, c, d, h = 3, 4, 6, 7, 0.5
y_values_func2 = [trapezoidal_member(x, a, b, c, d, h) for x in x_values]

# Function 3
a, b, c, d, h = 5, 6, 7, 8, 1
y_values_func3 = [trapezoidal_member(x, a, b, c, d, h) for x in x_values]

# Fuzzy set (obtained by taking union of functions defined above)
fuzzy_values = fuzzy_union(y_values_func1, y_values_func2, y_values_func3)
plt.plot(x_values, fuzzy_values, 'blue', label='Fuzzy Set')
plt.title('Centroid Method')
plt.xlabel('X-axis')
plt.ylabel('Membership Value')

def centroid(x_values, fuzzy_values):
    crisp_value = np.trapz(fuzzy_product(fuzzy_values, x_values), x_values) / np.trapz(fuzzy_values, x_values)
    crisp_value = round(crisp_value, 3)
    plt.axvline(x=crisp_value, color='r', linestyle='--', label=f'x = {crisp_value}')
    plt.legend()
    plt.show()

centroid(x_values, fuzzy_values)