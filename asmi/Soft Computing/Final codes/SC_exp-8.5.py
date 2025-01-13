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
    
# Plot the membership functions and operations
x_values = np.linspace(0, 8, 500)

# Function 1
a, b, c, d, h = 0, 1, 4, 5, 0.3
y_values_func1 = [trapezoidal_member(x, a, b, c, d, h) for x in x_values]
plt.plot(x_values, y_values_func1, 'blue')

# Function 2
a, b, c, d, h = 3, 4, 6, 7, 0.5
y_values_func2 = [trapezoidal_member(x, a, b, c, d, h) for x in x_values]
plt.plot(x_values, y_values_func2, 'blue')

# Function 3
a, b, c, d, h = 5, 6, 7, 8, 1
y_values_func3 = [trapezoidal_member(x, a, b, c, d, h) for x in x_values]
plt.plot(x_values, y_values_func3, 'blue')

# Fuzzy set (obtained by taking union of functions defined above)
plt.title('Weighted Average Method')
plt.xlabel('X-axis')
plt.ylabel('Membership Value')

def weightedAverage(x_values, y_values_func1, y_values_func2, y_values_func3):
    maxima1 = max(y_values_func1)
    maxima_index = [i for i, x in enumerate(y_values_func1) if x == maxima1]
    maxima_values = [x_values[x] for x in maxima_index]
    crisp1 = round(np.mean(maxima_values), 3)
    WA1 = crisp1 * maxima1
    plt.axvline(x=crisp1, color='g', linestyle='--', label=f'x = {crisp1}')

    maxima2 = max(y_values_func2)
    maxima_index = [i for i, x in enumerate(y_values_func2) if x == maxima2]
    maxima_values = [x_values[x] for x in maxima_index]
    crisp2 = round(np.mean(maxima_values), 3)
    WA2 = crisp2 * maxima2
    plt.axvline(x=crisp2, color='g', linestyle='--', label=f'x = {crisp2}')

    maxima3 = max(y_values_func3)
    maxima_index = [i for i, x in enumerate(y_values_func3) if x == maxima3]
    maxima_values = [x_values[x] for x in maxima_index]
    crisp3 = round(np.mean(maxima_values), 3)
    WA3 = crisp3 * maxima3
    plt.axvline(x=crisp3, color='g', linestyle='--', label=f'x = {crisp3}')

    crisp_value = (WA1 + WA2 + WA3) / (maxima1 + maxima2 + maxima3)
    crisp_value = round(crisp_value, 3)
    plt.axvline(x=crisp_value, color='r', linestyle='--', label=f'x = {crisp_value}')
    plt.legend()
    plt.show()

weightedAverage(x_values, y_values_func1, y_values_func2, y_values_func3)