import matplotlib.pyplot as plt
cylinders = 200

def fcfs(requests, start):
    algo_name = "FCFS"
    head = start
    serviceOrder = []
    for req in requests:
        reqPos = req
        tracks = abs(reqPos - head)
        service = (head, reqPos, tracks)
        serviceOrder.append(service)
        head = reqPos
    printTable(serviceOrder, algo_name)
    plotGraph(serviceOrder, algo_name)
    return

def sstf(requests, start):
    requests = requests[:]
    algo_name = "SSTF"
    head = start
    serviceOrder = []
    while requests:
        seektime = [abs(req - head) for req in requests]
        min_seektime = min(seektime)
        index = seektime.index(min_seektime)
        reqPos = requests[index]
        tracks = abs(reqPos - head)
        service = (head, reqPos, tracks)
        serviceOrder.append(service)
        requests.remove(reqPos)
        head = reqPos
    printTable(serviceOrder, algo_name)
    plotGraph(serviceOrder, algo_name)
    return

def scan(requests, start):
    algo_name = "SCAN"
    head = start
    reqPos = 0
    serviceOrder = []; serviceOrderL = []; serviceOrderR = []
    L = [x for x in requests if x < start]
    L.sort(reverse = True)
    R = [x for x in requests if x >= start]
    R.sort()
    for reqPos in R:
        tracks = abs(reqPos - head)
        service = (head, reqPos, tracks)
        serviceOrderR.append(service)
        head = reqPos
    # Go to end of right direction
    reqPos = cylinders - 1
    tracks = abs(reqPos - head)
    service = (head, reqPos, tracks)
    serviceOrderL.append(service)
    head = reqPos
    for reqPos in L:
        tracks = abs(reqPos - head)
        service = (head, reqPos, tracks)
        serviceOrderL.append(service)
        head = reqPos
    serviceOrder = serviceOrderR + serviceOrderL
    printTable(serviceOrder, algo_name)
    plotGraph(serviceOrder, algo_name)
    return

def cscan(requests, start):
    algo_name = "Circular SCAN"
    head = start
    reqPos = 0
    serviceOrder = []; serviceOrderL = []; serviceOrderR = []
    L = [x for x in requests if x < start]
    L.sort()
    R = [x for x in requests if x >= start]
    R.sort()
    for reqPos in R:
        tracks = abs(reqPos - head)
        service = (head, reqPos, tracks)
        serviceOrderR.append(service)
        head = reqPos
    # Go to end of right direction
    reqPos = cylinders - 1
    tracks = abs(reqPos - head)
    service = (head, reqPos, tracks)
    serviceOrderL.append(service)
    head = reqPos
    # Go to extreme left end
    reqPos = 0
    tracks = abs(reqPos - head)
    service = (head, reqPos, tracks)
    serviceOrderL.append(service)
    head = reqPos
    for reqPos in L:
        tracks = abs(reqPos - head)
        service = (head, reqPos, tracks)
        serviceOrderL.append(service)
        head = reqPos
    serviceOrder = serviceOrderR + serviceOrderL
    printTable(serviceOrder, algo_name)
    plotGraph(serviceOrder, algo_name)
    return

def look(requests, start):
    algo_name = "LOOK"
    head = start
    reqPos = 0
    serviceOrder = []; serviceOrderL = []; serviceOrderR = []
    L = [x for x in requests if x < start]
    L.sort(reverse = True)
    R = [x for x in requests if x >= start]
    R.sort()
    for reqPos in R:
        tracks = abs(reqPos - head)
        service = (head, reqPos, tracks)
        serviceOrderR.append(service)
        head = reqPos
    for reqPos in L:
        tracks = abs(reqPos - head)
        service = (head, reqPos, tracks)
        serviceOrderL.append(service)
        head = reqPos
    serviceOrder = serviceOrderR + serviceOrderL
    printTable(serviceOrder, algo_name)
    plotGraph(serviceOrder, algo_name)
    return

def printTable(serviceOrder, name):
    print(name, end = "\n\n")
    print("Current\t\tDestination\tNumber of")
    print("Position\tPosition\tTracks Covered")
    for service in serviceOrder:
        for value in service:
            print(value, end = "\t\t")
        print()
    print("\nTotal head movement =", sum([x[2] for x in serviceOrder]))
    return

def plotGraph(serviceOrder, name):
    x_values = [x[0] for x in serviceOrder]
    x_values.append(serviceOrder[-1][1])
    y_values = [-x for x in range(len(x_values))]
    plt.plot(x_values, y_values, marker = '.')
    plt.xticks(x_values)
    ax = plt.gca()
    ax.xaxis.tick_top()
    ax.get_yaxis().set_visible(False)
    plt.title(name)
    plt.show()


requests = [98, 183, 37, 122, 14, 127, 65, 70]
start_head_pointer = 50

# n = int(input("Enter number of requests: "))
# for i in range(n):
#     req = int(input(f"Positon {i + 1}: "))
#     requests.append(req)
    
fcfs(requests, start_head_pointer)
sstf(requests, start_head_pointer)
scan(requests, start_head_pointer)
cscan(requests, start_head_pointer)
look(requests, start_head_pointer)