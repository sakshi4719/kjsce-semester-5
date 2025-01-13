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

# def func1(x_values):
#     output = []
#     for x in x_values:
#         if x <= 3:
#             output.append(0)
#         elif 3 < x < 5:
#             output.append((x-3)/2)
#         elif 5 <= x <= 8:
#             output.append(1)
#         elif 8 < x < 10:
#             output.append((10-x)/2)
#         elif x >= 10:
#             output.append(0)
#     return output

# x = [x for x in range(1, 13)]
# y = func1(x)
# y_bar = fuzzy_complement(y)
# plt.plot(x,y, color='r', label="Function 1")
# plt.plot(x, y_bar, color='b', label="Complement")
# plt.title()
# plt.legend()
# plt.show()