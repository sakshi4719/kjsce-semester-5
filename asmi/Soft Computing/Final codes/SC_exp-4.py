import numpy as np

# Activation function
def activation(net):
  return 2 / (1 + np.exp(-1*net)) - 1

def deltaRule(input_vector, target):
    # Initialization
    lr = 0.1
    weight = (1, -1, 0, 0.5)
    w1, w2, w3, w4 = weight
    print("Learning Rate =", lr)
    print("Initial weights:\nw1 = {0}\t\tw2 = {1}\t\tw3 = {2}\t\tw4 = {3}".format(w1, w2, w3, w4))

    # Delta Learning Rule
    table = []
    i = 0
    result = [0, 0, 0, 0]
    for input in input_vector:
        row = []
        x1, x2, x3, x4 = input
        t = target[i]
        net = round(x1*w1 + x2*w2 + x3*w3 + x4*w4, 3)
        result[i] = net
        y = round(activation(net), 3)
        grad_y = round(0.5 * (1 - y**2), 3)
        w1 = round(w1 + lr * (t-y) * grad_y * x1, 3)
        w2 = round(w2 + lr * (t-y) * grad_y * x2, 3)
        w3 = round(w3 + lr * (t-y) * grad_y * x3, 3)
        w4 = round(w4 + lr * (t-y) * grad_y * x4, 3)
        i += 1
        row.extend([net, y, grad_y])
        row.append([w1, w2, w3, w4])
        table.append(row)
    printTable(table)
    error = 0
    for i in range(len(input_vector)):
      error += (target[i] - result[i]) ** 2
    error /= len(input_vector)
    print("Error = %5.3f" % error)
    return

def printTable(table):
    print("----------------------------------------------------------------------------------------------------")
    print("net\t\t | o\t\t\t | f'(net)\t\t | Updated weights")
    print("----------------------------------------------------------------------------------------------------")
    for row in table:
        for value in row[:-1]:
            print("%5.3f" % value, end = "\t\t | ")
        print(row[-1])
    print("----------------------------------------------------------------------------------------------------")

# Make a list of all inputs to be given to the network
x_1 = [1, -2, 0, -1]
x_2 = [0, 1.5, -0.5, -1]
x_3 = [-1, 1, 0.5, -1]
input_vector = []
input_vector.extend([x_1, x_2, x_3])
target = [-1, -1, 1]                    # Expected target outputs
deltaRule(input_vector, target)         # Supply the input and expected output to the network