import numpy as np
import matplotlib.pyplot as plt

def fuzzy_complement(setA):
    complement = []
    for value in setA:
        complement.append(round(1-value, 3))        
    return complement

def fuzzy_intersection(setA, setB):
    intersection = []
    for value in list(zip(setA, setB)):
        intersection.append(min(value))
    return intersection

def fuzzy_union(setA, setB):
    union = []
    for value in list(zip(setA, setB)):
        union.append(max(value))
    return union

def fuzzy_product(setA, setB):
    product = []
    for value1, value2 in list(zip(setA, setB)):
        product.append(round(value1 * value2, 3))
    return product

def fuzzy_crisp_multiplication(setA, crisp):
    multiplication = []
    for value in setA:
        multiplication.append(round(value * crisp,3))
    return multiplication


set_A = (0.7, 0.3, 0.9, 0.1)
set_B = (0.2, 0.5, 0.7, 0.4)
set_C = (0.1, 0.2, 0.3, 0.4)
set_D = (0.5, 0.7, 0.8, 0.9)

print("Set 1 =", set_A, sep = "\t")
print("set 2 =", set_B, sep = "\t")
print("Complement =", fuzzy_complement(set_A), sep = "\t")
print("Intersection =", fuzzy_intersection(set_A, set_B), sep = "\t")
print("Union =", fuzzy_union(set_A, set_B), sep = "\t\t")
print()
print("Set 3 =", set_C, sep = "\t")
print("set 4 =", set_D, sep = "\t")
print("Product =", fuzzy_product(set_C, set_D), sep = "\t")
print("Multiplication=", fuzzy_crisp_multiplication(set_C, 0.2))

# VISUALIZATIONS

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

# Plot the membership functions and operations
x_values = np.linspace(0, 10, 500)

# Function 1 (Triangular)
a, b, c = 3, 4, 5
y_values_triangular = [triangular_member(x, a, b, c) for x in x_values]
plt.plot(x_values, y_values_triangular, 'g', label=f'T({a}, {b}, {c})')

# Function 2 (Trapezoidal)
a, b, c, d = 4, 5, 8, 9
y_values_trapezoidal = [trapezoidal_member(x, a, b, c, d) for x in x_values]
plt.plot(x_values, y_values_trapezoidal, 'r', label=f'Tr({a}, {b}, {c}, {d})')

# Union
union_values = fuzzy_union(y_values_triangular, y_values_trapezoidal)
plt.plot(x_values, union_values, 'blue', label='Union')
plt.title('Union (OR) Operator')
plt.xlabel('X-axis')
plt.ylabel('Membership Value')
plt.legend()
plt.show()

# Intersection
intersection_values = fuzzy_intersection(y_values_triangular, y_values_trapezoidal)
plt.plot(x_values, intersection_values, 'yellow', label='Intersection')
plt.title('Intersection (AND) Operator')
plt.xlabel('X-axis')
plt.ylabel('Membership Value')
plt.legend()
plt.show()

# Complement
complement_values = fuzzy_complement(y_values_trapezoidal)
plt.plot(x_values, complement_values, 'black', label='Complement')
plt.title('Complement (NOT) Operator')
plt.xlabel('X-axis')
plt.ylabel('Membership Value')
plt.legend()
plt.show()