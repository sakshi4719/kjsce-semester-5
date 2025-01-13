import numpy as np
import matplotlib.pyplot as plt

# Identity Function
x = np.arange(0, 11, 1)
y = x
plt.axvline(x=0, c="black")
plt.axhline(y=0, c="black")
plt.plot(x, y, label = "f(x) = x")
plt.grid(linestyle = '--', linewidth = 0.5)
plt.title("Identity Function")
plt.xlabel("net")
plt.ylabel("y = f(net)")
plt.legend()
plt.show()

# Binary Threshold Function
def binaryStep(values, threshold):
  y = []
  for x in values:
    if x < threshold:
      y.append(0)
    elif x >= threshold:
      y.append(1)
  return y

x = np.arange(0, 5, 0.001)
t = 2
y = binaryStep(x, t)
plt.axvline(x=0, c="black")
plt.axhline(y=0, c="black")
plt.plot(x, y, label = "f(x) = 1 if x >= 2 \nf(x) = 0 if x < 2")
plt.grid(linestyle = '--', linewidth = 0.5)
plt.title("Binary Step Function\nThreshold = 2")
plt.xlabel("net")
plt.ylabel("y = f(net)")
plt.legend()
plt.show()

# Sigmoid Function
x = np.linspace(-10, 10, 100)
y = 1/(1 + np.exp(-2*x))
plt.axvline(x=0, c="black")
plt.axhline(y=0, c="black")
plt.plot(x, y, label = "f(x) = 1/(1 + e^(-2*x))")
plt.grid(linestyle = '--', linewidth = 0.5)
plt.title("Sigmoid Function")
plt.xlabel("net")
plt.ylabel("y = f(net)")
plt.legend()
plt.show()

# Bipolar Sigmoid / Tangent Function
x = np.linspace(-10, 10, 100)
y = 2 / (1 + np.exp(-0.5*x)) - 1
plt.axvline(x=0, c="black")
plt.axhline(y=0, c="black")
plt.plot(x, y, label = "f(x) = 2/(1 + e^(-2*x)) - 1")
plt.grid(linestyle = '--', linewidth = 0.5)
plt.title("Bipolar Sigmoid Function")
plt.xlabel("net")
plt.ylabel("y = f(net)")
plt.legend()
plt.show()

# Ramp Function
def ramp(values, threshold1, threshold2):
  y = []
  for x in values:
    if x <= threshold1:
      y.append(0)
    elif threshold1 < x < threshold2:
      y.append(x-threshold1)
    elif x >= threshold2:
      y.append(threshold2-threshold1)
  return y

x = np.arange(0, 10, 0.001)
t1 = 3
t2 = 6
y = ramp(x, t1, t2)
plt.axvline(x=0, c="black")
plt.axhline(y=0, c="black")
plt.plot(x, y, label = "f(x) = 0    if x <= 3 \nf(x) = x-3 if 3 < x < 6 \nf(x) = 3    if x >= 6")
plt.grid(linestyle = '--', linewidth = 0.5)
plt.title("Ramp Function")
plt.xlabel("net")
plt.ylabel("y = f(net)")
plt.legend()
plt.show()

# ReLU Function
def relu(values):
  y = []
  for x in values:
    if x <= 0:
      y.append(0)
    else:
      y.append(x)
  return y

x = np.linspace(-10, 10, 100)
y = relu(x)
plt.axvline(x=0, c="black")
plt.axhline(y=0, c="black")
plt.plot(x, y, label = "f(x) = 0 if x <= 0 \nf(x) = x if x > 0")
plt.grid(linestyle = '--', linewidth = 0.5)
plt.title("ReLU Function")
plt.xlabel("net")
plt.ylabel("y = f(net)")
plt.legend()
plt.show()

# SoftMax Function
def softmax(values):
    y = []
    denominator = sum([np.exp(x) for x in values])
    for x in values:
        numerator = np.exp(x)
        result = numerator / denominator
        y.append(result)
    return y
x = np.arange(0, 11, 1)
y = softmax(x)
plt.axvline(x=0, c="black")
plt.axhline(y=0, c="black")
plt.plot(x, y, label = "softmax")
plt.grid(linestyle = '--', linewidth = 0.5)
plt.title("SoftMax Function")
plt.xlabel("net")
plt.ylabel("y = f(net)")
plt.legend()
plt.show()