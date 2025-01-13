import numpy as np
import matplotlib.pyplot as plt

# Triangular membership functions for each term
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

def createPlot(a_values, b_values, c_values, title):
    """Create plots for each triangular membership function"""
    x_values = np.linspace(0, 100, 500)
    for a, b, c in zip(a_values, b_values, c_values):
        y_values = [triangular_member(x, a, b, c) for x in x_values]
        plt.plot(x_values, y_values, label=f'({a}, {b}, {c})')

    plt.xlabel(title)
    plt.ylabel('Degree of Belonging')
    title = title + ' Membership Function'
    plt.title(title)
    plt.grid()
    plt.show()
        
# Define parameters - Dirt
a_values_d = [0, 20, 70]
b_values_d = [0, 50, 100]
c_values_d = [30, 80, 100]
createPlot(a_values_d, b_values_d, c_values_d, 'Dirt')

# Define parameters - Grease
a_values_g = [0, 20, 60]
b_values_g = [0, 50, 100]
c_values_g = [40, 80, 100]
createPlot(a_values_g, b_values_g, c_values_g, 'Grease')

# Define parameters - Wash Time
a_values_w = [0, 10, 30, 50, 80]
b_values_w = [0, 30, 50, 70, 100]
c_values_w = [20, 50, 70, 90, 100]
createPlot(a_values_w, b_values_w, c_values_w, 'Wash Time')

# Input: Dirt = 60, Grease = 70
input_value = 60
parameters_d = list(zip(a_values_d, b_values_d, c_values_d))
print("Dirt:")
print("Low\tMedium\tHigh")
for a, b, c in parameters_d:
    result = round(triangular_member(input_value, a, b, c), 3)
    print(result, end = "\t")
print()

input_value = 70
parameters_g = list(zip(a_values_g, b_values_g, c_values_g))
print("Grease:")
print("Low\tMedium\tHigh")
for a, b, c in parameters_d:
    result = round(triangular_member(input_value, a, b, c), 3)
    print(result, end = "\t")
print()

# TRAPEZOIDAL membership function
def trapezoidal_member(x, a, b, c, d, h = 1):
    """Trapezoidal membership function"""
    if x <= a:
        return 0.0
    elif a < x < b:
        return h * (x - a) / (b - a)
    elif b <= x <= c:
        return h
    elif c < x < d:
        return h * (d - x) / (d - c)
    else:
        return 0.0

x_values = np.linspace(0, 100, 500)
y_values = [trapezoidal_member(x, 30, 40, 60, 70, h = 0.333) for x in x_values]
plt.plot(x_values, y_values)
plt.grid()

def meanOfMaxima(x_values, fuzzy_values):
    maxima = max(fuzzy_values)
    maxima_index = [i for i, x in enumerate(fuzzy_values) if x == maxima]
    maxima_values = [x_values[x] for x in maxima_index]
    crisp_value = np.mean(maxima_values)
    crisp_value = round(crisp_value, 3)
    plt.axvline(x=crisp_value, color='r', linestyle='--', label=f'x = {crisp_value}')
    plt.legend()
    plt.show()

meanOfMaxima(x_values, y_values)