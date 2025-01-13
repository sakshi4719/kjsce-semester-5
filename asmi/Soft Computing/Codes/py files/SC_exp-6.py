import math
import random
import sys
import pandas as pd

# Activation function
def activation(net):
    return 1 / (1 + math.exp(-1*net))

def calc_net(inputs, weights):
    x1, x2 = inputs
    w1, w2, w0 = weights
    net = x1*w1 + x2*w2 + w0
    return net

def neuron(net):
    output = activation(net)
    return output

def errorBackPropogation(input_vector, target, max_error):
    # Initialization
    lr = 0.7
    w30 = -1
    w40 = -1
    w50 = -1
    w31 = random.uniform(-1, 1)
    w41 = random.uniform(-1, 1)
    w32 = random.uniform(-1, 1)
    w42 = random.uniform(-1, 1)
    w53 = random.uniform(-1, 1)
    w54 = random.uniform(-1, 1)
    initial_weights = w50, w53, w54, w30, w31, w32, w40, w41, w42
    initial_weights = map(lambda x: round(x, 3), initial_weights)
    w50, w53, w54, w30, w31, w32, w40, w41, w42 = initial_weights
    print("Learning Rate =", lr)
    print("Initial weights:\n \
    w50 = {0}\t\tw53 = {1}\t\tw54 = {2}\n \
    w30 = {3}\t\tw31 = {4}\t\tw32 = {5}\n \
    w40 = {6}\t\tw41 = {7}\t\tw42 = {8}\n \
    ".format(w50, w53, w54, w30, w31, w32, w40, w41, w42))
    cycle_error = sys.maxsize
    steps = 0
    while cycle_error > max_error:
        i = 0
        cycle_error = 0
        for input_ in input_vector:
            o1, o2 = input_
            # Forward pass
            # Neuron #3
            weight = [w31, w32, w30]
            net = calc_net(input_, weight)
            o3 = neuron(net)
            # Neuron #4
            weight = [w41, w42, w40]
            net = calc_net(input_, weight)
            o4 = neuron(net)
            # Neuron #5
            weight = [w53, w54, w50]
            input_ = [o3, o4]
            net = calc_net(input_, weight)
            o5 = neuron(net)
            # Reverse pass
            # Calculate error and error signals
            error = target[i] - o5
            cycle_error += (1/2) * ((error) ** 2)
            d5 = error * o5 * (1 - o5)
            d3 = d5 * w53 * o3 * (1 - o3)
            d4 = d5 * w54 * o4 * (1 - o4)
            # Adjust weights
            w50 += lr * d5
            w53 += lr * d5 * o3
            w54 += lr * d5 * o4
            w30 += lr * d3
            w31 += lr * d3 * o1
            w32 += lr * d3 * o2
            w40 += lr * d4
            w41 += lr * d4 * o1
            w42 += lr * d4 * o2
            i += 1
            steps += 1
    final_weights = w50, w53, w54, w30, w31, w32, w40, w41, w42
    final_weights = map(lambda x: round(x, 3), final_weights)
    w50, w53, w54, w30, w31, w32, w40, w41, w42 = final_weights
    final_weights = w50, w53, w54, w30, w31, w32, w40, w41, w42
    print("Final weights:\n \
    w50 = {0}\t\tw53 = {1}\t\tw54 = {2}\n \
    w30 = {3}\t\tw31 = {4}\t\tw32 = {5}\n \
    w40 = {6}\t\tw41 = {7}\t\tw42 = {8}\n \
    ".format(w50, w53, w54, w30, w31, w32, w40, w41, w42))
    print("Number of iterations required =", steps, end = "\n\n")
    return final_weights

def test(input_vector, weights):
    predict = [0] * len(input_vector)
    w50, w53, w54, w30, w31, w32, w40, w41, w42 = weights
    i = 0
    for input_ in input_vector:
        weight = [w31, w32, w30]
        net = calc_net(input_, weight)
        o3 = neuron(net)
        # Neuron #4
        weight = [w41, w42, w40]
        net = calc_net(input_, weight)
        o4 = neuron(net)
        # Neuron #5
        weight = [w53, w54, w50]
        input_ = [o3, o4]
        net = calc_net(input_, weight)
        o5 = neuron(net)
        if o5 > 0.5:
            predict[i] = 1
        else:
            predict[i] = 0
        i += 1
    return predict

def displayOutputTable(input_vector, target, prediction):
    column_names = pd.DataFrame([["Input", "x1"],
                                ["Input", "x2"],
                                ["Target", "t"],
                                ["Predicted", ""],
                                ["Class", ""]],
                                columns=["", ""])

    rows = []
    for i, input_ in enumerate(input_vector):
        row = []
        x1, x2 = input_
        if prediction[i] > 0.5:
            class_no = 1
        else:
            class_no = 2
        row.extend([x1, x2, target[i], prediction[i], class_no])
        rows.append(row)

    columns = pd.MultiIndex.from_frame(column_names)

    df = pd.DataFrame(rows, columns=columns)
    return df

x_1 = [0, 0, 1, 1]
x_2 = [0, 1, 0, 1]
input_vector = []
input_vector.extend(list(zip(x_1, x_2)))
target = [0, 1, 1, 0]
max_error = 0.1
weights = errorBackPropogation(input_vector, target, max_error)
prediction = test(input_vector, weights)
df = displayOutputTable(input_vector, target, prediction)
print(df)