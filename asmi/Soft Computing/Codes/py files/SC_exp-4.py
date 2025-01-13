import numpy as np
import pandas as pd
import sys

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
  result = [0, 0, 0, 0]
  j = 0
  old_error = sys.maxsize
  while True:
    j += 1
    print("\nEpoch {0}:".format(j))
    i = 0
    for input in input_vector:
        x1, x2, x3, x4 = input
        print("\nInput {0}:".format(i+1), input)
        t = target[i]
        print("Target =", t)
        net = round(x1*w1 + x2*w2 + x3*w3 + x4*w4, 3)
        result[i] = net
        y = round(activation(net), 3)
        grad_y = round(0.5 * (1 - y**2), 3)
        print("Net = {0}\nOutput = {1}\nf'(net) = {2}".format(net, y, grad_y))
        d_w1 = round(lr * (t-y) * grad_y * x1, 3)
        d_w2 = round(lr * (t-y) * grad_y * x2, 3)
        d_w3 = round(lr * (t-y) * grad_y * x3, 3)
        d_w4 = round(lr * (t-y) * grad_y * x4, 3)
        print("d(w1) = {1}\td(w2) = {2}\td(w3) = {3}\td(w4) = {4}".format(i, d_w1, d_w2, d_w3, d_w4))
        w1 = round(w1 + d_w1, 3)
        w2 = round(w2 + d_w2, 3)
        w3 = round(w3 + d_w3, 3)
        w4 = round(w4 + d_w4, 3)
        i += 1
        print("Updated weights after input {0}:\nw1 = {1}\tw2 = {2}\tw3 = {3}\tw4 = {4}".format(i, w1, w2, w3, w4))

    # Error calculation
    error = 0
    for i in range(len(input_vector)):
      error += (1/2) * (target[i] - result[i]) ** 2
    print("\nError =", error)

    # old_weights = w1, w2, w3, w4    # for 1 epoch
    # break                           # for 1 epoch

    if error > old_error:
      break

    old_weights = w1, w2, w3, w4
    old_error = error

  fw1, fw2, fw3, fw4 = old_weights
  print("\nFinal weights for minimum error:\nw1 = {1}\tw2 = {2}\tw3 = {3}\tw4 = {4}".format(i, fw1, fw2, fw3, fw4))
  print("Total epochs needed =", j, end = "\n\n")

  return old_weights

def test(input_vector, weights):
  predict = [0] * len(input_vector)
  w1, w2, w3, w4 = weights
  i = 0
  for input in input_vector:
    x1, x2, x3, x4 = input
    net = round(x1*w1 + x2*w2 + x3*w3 + x4*w4, 3)
    y = round(activation(net), 3)
    predict[i] = y
    i += 1
  return predict

def displayTable(input_vector, target, prediction):
  column_names = pd.DataFrame([["Input", "x1"],
                              ["Input", "x2"],
                              ["Input", "x3"],
                              ["Input", "x4"],
                              ["Target", "t"],
                              ["Predicted", ""],
                              ["Sign", ""],
                              ["Class", ""]],
                              columns=["", ""])

  rows = []
  for i, input in enumerate(input_vector):
    row = []
    x1, x2, x3, x4 = input
    if prediction[i] > 0:
      sign = '+'
      class_no = 1
    else:
      sign = '-'
      class_no = 2
    row.extend([x1, x2, x3, x4, target[i], prediction[i], sign, class_no])
    rows.append(row)

  columns = pd.MultiIndex.from_frame(column_names)

  df = pd.DataFrame(rows, columns=columns)
  return df

x_1 = [1, -2, 0, -1]
x_2 = [0, 1.5, -0.5, -1]
x_3 = [-1, 1, 0.5, -1]
input_vector = []
input_vector.extend([x_1, x_2, x_3])
target = [-1, -1, 1]
weights = deltaRule(input_vector, target)
prediction = test(input_vector, weights)
df = displayTable(input_vector, target, prediction)
print(df)