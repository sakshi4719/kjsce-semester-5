import numpy as np

# Activation function
def activation(net, mode):
    if mode == 'discrete':
        if net >= 0:
            return 1
        else:
            return -1
    elif mode == 'continuous':
        return 2 / (1 + np.exp(-1*net)) - 1

def hebbianRule(input_vector, AF_mode):
    # Initialization
    lr = 1
    weight = (1, -1, 0, 0.5)
    w1, w2, w3, w4 = weight
    print("\nHebbian model with", AF_mode, "activation function")
    print("Learning Rate =", lr)
    print("Initial weights:\nw1 = {0}\t\tw2 = {1}\t\tw3 = {2}\t\tw4 = {3}".format(w1, w2, w3, w4))

    # Hebbian Learning Rule
    table = []
    for input in input_vector:
        row = []
        x1, x2, x3, x4 = input
        net = round(x1*w1 + x2*w2 + x3*w3 + x4*w4, 3)
        y = round(activation(net, AF_mode), 3)
        w1 = round(w1 + y * x1, 3)
        w2 = round(w2 + y * x2, 3)
        w3 = round(w3 + y * x3, 3)
        w4 = round(w4 + y * x4, 3)
        row.extend([net, y])
        row.append([w1, w2, w3, w4])
        table.append(row)
    printTable(table)
    return

def printTable(table):
    i = 0
    print("-----------------------------------------------------------------------------")
    print("net\t\t | f(net)\t\t | Updated weights")
    print("-----------------------------------------------------------------------------")
    for row in table:
        for value in row[:-1]:
            print("%5.3f" % value, end = "\t\t | ")
        print(row[-1])
    print("-----------------------------------------------------------------------------")

x_1 = [1, -2, 1.5, 0]
x_2 = [1, -0.5, -2, -1.5]
x_3 = [0, 1, -1, 1.5]
input_vector = []
input_vector.extend([x_1, x_2, x_3])
hebbianRule(input_vector, 'discrete')
hebbianRule(input_vector, 'continuous')