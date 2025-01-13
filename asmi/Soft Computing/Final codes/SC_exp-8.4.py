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
    
def fuzzy_union(setA, setB):
    union = []
    for value in list(zip(setA, setB)):
        union.append(max(value))
    return union

# Plot the membership functions and operations
x_values = np.linspace(0, 10, 500)

# Function 1
a, b, c, d, h = 0, 2, 4, 6, 0.7
y_values_func1 = [trapezoidal_member(x, a, b, c, d, h) for x in x_values]

# Function 2
a, b, c, d, h = 2, 5, 8, 10, 1
y_values_func2 = [trapezoidal_member(x, a, b, c, d, h) for x in x_values]

# Fuzzy set (obtained by taking union of functions defined above)
fuzzy_values = fuzzy_union(y_values_func1, y_values_func2)
plt.plot(x_values, fuzzy_values, 'blue', label='Fuzzy Set')
plt.title('Mean of Maxima Method')
plt.xlabel('X-axis')
plt.ylabel('Membership Value')

def meanOfMaxima(x_values, fuzzy_values):
    maxima = max(fuzzy_values)
    maxima_index = [i for i, x in enumerate(fuzzy_values) if x == maxima]
    maxima_values = [x_values[x] for x in maxima_index]
    crisp_value = np.mean(maxima_values)
    crisp_value = round(crisp_value, 3)
    plt.axvline(x=crisp_value, color='r', linestyle='--', label=f'x = {crisp_value}')
    plt.legend()
    plt.show()

meanOfMaxima(x_values, fuzzy_values)