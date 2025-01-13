import pandas as pd
import random

# Activation function
def activation(net, threshold):
  if net >= threshold:
    return 1
  else:
    return -1
  
  # Perceptron Training Algorithm

def perceptron(input_vector):

    # Initial setup
    threshold = random.randrange(0,5)
    w1 = random.randrange(-2,3)
    w2 = random.randrange(-2,3)
    wb = random.randrange(-2,3)
    print("\nThreshold = {0}\n".format(threshold))
    print("Initial weights:\nw1 = {0}\tw2 = {1}\twb = {2}\n".format(w1, w2, wb))

    # Algorithm
    repeat = True
    result = [0, 0, 0, 0]
    firstRunWts = ()
    j = 0
    while repeat:
        j += 1
        print("Iteration {0}".format(j))
        i = 0
        firstIteration = True
        for input in input_vector:
            x1, x2 = input
            t = target[i]
            net = x1*w1 + x2*w2 + wb
            y = activation(net, threshold)
            result[i] = y
            if y != t:
                w1 = w1 + (t-y) * x1
                w2 = w2 + (t-y) * x2
                wb = wb + (t-y)
            i += 1
            if firstIteration == True:
                firstRunWts = (w1, w2, wb)
            firstIteration = False
            print("Weights after input ({0}, {1}):\tw1 = {2}\tw2 = {3}\twb = {4}".format(x1, x2, w1, w2, wb))
        print("Iteration complete.")
        print("Updated weights:\nw1 = {0}\tw2 = {1}\twb = {2}\n".format(w1, w2, wb))
        lastRunWts = (w1, w2, wb)
        if lastRunWts == firstRunWts or result == target:
            repeat = False
    print("Final weights:\nw1 = {0}\tw2 = {1}\twb = {2}\n".format(w1, w2, wb))
    return result

def displayLogic(input_vector, target, result):
    column_names = pd.DataFrame([["Input Vector", "x1"],
                                ["Input Vector", "x2"],
                                ["Target", "Output"],
                                ["Predicted", "Output"]],
                                columns=["", ""])

    rows = []
    for i, input in enumerate(input_vector):
        x1, x2 = input
        row = []
        row.extend([x1, x2, target[i], result[i]])
        rows.append(row)

    columns = pd.MultiIndex.from_frame(column_names)

    df = pd.DataFrame(rows, columns=columns)
    return df

# AND Gate
x_1 = [-1, -1, 1, 1]
x_2 = [-1, 1, -1, 1]
input_vector = list(zip(x_1, x_2))
target = [-1, -1, -1, 1]
print("\nAND Gate")
result = perceptron(input_vector)
df_and = displayLogic(input_vector, target, result)
print(df_and)

# OR Gate
x_1 = [-1, -1, 1, 1]
x_2 = [-1, 1, -1, 1]
input_vector = list(zip(x_1, x_2))
target = [-1, 1, 1, 1]
print("\nOR Gate")
result = perceptron(input_vector)
df_or = displayLogic(input_vector, target, result)
print(df_or)

# NOR Gate
x_1 = [-1, -1, 1, 1]
x_2 = [-1, 1, -1, 1]
input_vector = list(zip(x_1, x_2))
target = [1, -1, -1, -1]
print("\nNOR Gate")
result = perceptron(input_vector)
df_nor = displayLogic(input_vector, target, result)
print(df_nor)

# NAND Gate
x_1 = [-1, -1, 1, 1]
x_2 = [-1, 1, -1, 1]
input_vector = list(zip(x_1, x_2))
target = [1, 1, 1, -1]
print("\nNAND Gate")
result = perceptron(input_vector)
df_nand = displayLogic(input_vector, target, result)
print(df_nand)