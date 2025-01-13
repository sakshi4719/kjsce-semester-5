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
    
def fuzzy_union(setA, setB):
    union = []
    for value in list(zip(setA, setB)):
        union.append(max(value))
    return union

# Plot the membership functions and operations
x_values = np.linspace(0, 10, 500)

# Function 1 (Triangular)
a, b, c = 2, 4, 6
y_values_triangular = [triangular_member(x, a, b, c) for x in x_values]

# Function 2 (Trapezoidal)
a, b, c, d, h = 4, 5, 6, 7, 0.5
y_values_trapezoidal = [trapezoidal_member(x, a, b, c, d, h) for x in x_values]

# Fuzzy set (obtained by taking union of functions defined above)
fuzzy_values = fuzzy_union(y_values_triangular, y_values_trapezoidal)
plt.plot(x_values, fuzzy_values, 'blue', label='Fuzzy Set')
plt.title('Max Membership Method')
plt.xlabel('X-axis')
plt.ylabel('Membership Value')

def max_membership(x_values, fuzzy_values):
    # values = zip(x_values, fuzzy_values)
    index = fuzzy_values.index(max(fuzzy_values))
    crisp_value = int(x_values[index])
    plt.axvline(x=4, color='r', linestyle='--', label=f'x = {crisp_value}')
    plt.legend()
    plt.show()

max_membership(x_values, fuzzy_values)