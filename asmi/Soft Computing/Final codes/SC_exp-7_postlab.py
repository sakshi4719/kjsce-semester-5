import numpy as np
import matplotlib.pyplot as plt

# Trapezoidal membership functions for each term
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
a_values = [0, 30, 45, 55, 65, 75, 85]
b_values = [0, 36, 48, 60, 72, 80, 92]
c_values = [30, 45, 57, 69, 78, 90, 100]
d_values = [40, 55, 65, 75, 85, 95, 100]
labels = ['Very bad', 'Bad', 'Poor', 'Average', 'Good', 'Very good', 'Excellent']
parameters = list(zip(a_values, b_values, c_values, d_values))

# Create plots for each trapezoidal membership function
x_values = np.linspace(0, 100, 500)
for a, b, c, d, label_ in zip(a_values, b_values, c_values, d_values, labels):
    y_values = [trapezoidal_member(x, a, b, c, d) for x in x_values]
    plt.plot(x_values, y_values, label=label_)

plt.xlabel('X-axis')
plt.ylabel('Degree of Belonging')
plt.title('Fuzzy Course Evaluation Set')
plt.legend()
plt.show()