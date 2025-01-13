import math

def getIPClass(ip):
  ip_bytes = ip.split(".")
  x = int(ip_bytes[0])
  if 1 <= x <= 127:
    return 'A'
  elif 128 <= x <= 191:
    return 'B'
  elif 192 <= x <= 223:
    return 'C'

def binaryCount(pad):
  count = 0
  increment = 1
  while True:
    res = bin(count)[2:]
    yield '0' * (pad - len(res)) + res
    count += increment

def makeSubnet(ip, n):
  if '/' not in ip:
    ipClass = getIPClass(ip)
    print("IP belongs to class", ipClass)
    if ipClass == 'A':
      mask = 8
    elif ipClass == 'B':
      mask = 16
    elif ipClass == 'C':
      mask = 24
  else:
    mask = int(ip[ip.index('/') + 1 : ])
    ip = ip[ : ip.index('/')]
  ip_bytes = ip.split(".")
  constant_bytes = mask // 8
  IP_prefix = ".".join(ip_bytes[ : constant_bytes])
  borrowed_bits = math.ceil(math.log(n, 2))
  bits_for_host_ID = 32 - (mask + borrowed_bits)
  net_ID = bin(int(ip_bytes[constant_bytes]))[2:]
  variable_subnet_IP =  '0' * (8 - len(net_ID)) + net_ID + '0' * 8 * (3 - constant_bytes)
  borrowed_bits_position = mask % 8
  x = binaryCount(borrowed_bits)
  for i in range(n-1):
    print("\nSubnet", i+1)
    y = next(x)
    variable_subnet_IP = variable_subnet_IP[ : borrowed_bits_position] + y + (variable_subnet_IP[borrowed_bits_position + borrowed_bits : ].replace('1', '0'))
    IP_suffix = ".".join(map(lambda x : str(int(x, 2)), [variable_subnet_IP[i:i+8] for i in range(0, len(variable_subnet_IP), 8)]))
    first_subnet_IP = IP_prefix + '.' + IP_suffix
    print("First IP: {}".format(first_subnet_IP))
    variable_subnet_IP = variable_subnet_IP[ : borrowed_bits_position] + y + (variable_subnet_IP[borrowed_bits_position + borrowed_bits : ].replace('0', '1'))
    IP_suffix = ".".join(map(lambda x : str(int(x, 2)), [variable_subnet_IP[i:i+8] for i in range(0, len(variable_subnet_IP), 8)]))
    last_subnet_IP = IP_prefix + '.' + IP_suffix
    print("Last IP: {}".format(last_subnet_IP))
  else:
    print("\nSubnet", n)
    y = next(x)
    variable_subnet_IP = variable_subnet_IP[ : borrowed_bits_position] + y + (variable_subnet_IP[borrowed_bits_position + borrowed_bits : ].replace('1', '0'))
    IP_suffix = ".".join(map(lambda x : str(int(x, 2)), [variable_subnet_IP[i:i+8] for i in range(0, len(variable_subnet_IP), 8)]))
    first_subnet_IP = IP_prefix + '.' + IP_suffix
    print("First IP: {}".format(first_subnet_IP))
    variable_subnet_IP = variable_subnet_IP[ : borrowed_bits_position] + '1' * borrowed_bits + (variable_subnet_IP[borrowed_bits_position + borrowed_bits : ].replace('0', '1'))
    IP_suffix = ".".join(map(lambda x : str(int(x, 2)), [variable_subnet_IP[i:i+8] for i in range(0, len(variable_subnet_IP), 8)]))
    last_subnet_IP = IP_prefix + '.' + IP_suffix
    print("Last IP: {}".format(last_subnet_IP))
  return

ip = input("Enter ip address: ")
# ip = "192.168.224.0/19"
getIPClass(ip)
n = int(input("Enter number of subnets: "))
makeSubnet(ip, n)