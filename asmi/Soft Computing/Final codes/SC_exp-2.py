import numpy as np

input_vector = [(0,0), (0,1), (1,0), (1,1)]
bias = -1/2

# TLU 1
w1 = -2
w2 = 1
o1_vector = []
for input in input_vector:
  x1, x2 = tuple(input)
  net = x1*w1 + x2*w2 + bias
  o1 = int(np.sign(net))
  o1_vector.append(o1)

# TLU 2
w1 = 1
w2 = -1
o2_vector = []
for input in input_vector:
  x1, x2 = tuple(input)
  net = x1*w1 + x2*w2 + bias
  o2 = int(np.sign(net))
  o2_vector.append(o2)

# TLU 3
w1 = 1
w2 = 1
bias = 1
o3_vector = []
class_vector = []
for i in range(len(input_vector)):
  o1 = o1_vector[i]
  o2 = o2_vector[i]
  net = o1*w1 + o2*w2 + bias
  o3 = int(np.sign(net))
  o3_vector.append(o3)
  if o3 > 0:
    class_vector.append(1)
  else:
    class_vector.append(2)

x1_vector = [i[0] for i in input_vector]
x2_vector = [i[1] for i in input_vector]
output = list(zip(x1_vector, x2_vector, o1_vector,o2_vector,o3_vector, class_vector))

print("------------------------------------------------------------------")
print("Pattern Space\t |  Image Space\t | Output Space\t |  Class\t |")
print("x1\t | x2 \t |  o1\t | o2 \t |  o3 \t\t |  Number \t |")
print("------------------------------------------------------------------")

for record in output:
    for value in record[:4]:
        print(value, end = '\t |  ')
    for value in record[4:]:
        print(value, end = '\t\t |  ')
    print()
print("------------------------------------------------------------------")