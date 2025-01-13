# Given snapshot of system
processes = [0, 1, 2, 3, 4]
available = [3, 3, 2]
maximum = [[7, 5, 3 ], [3, 2, 2 ], [ 9, 0, 2 ], [2, 2, 2], [4, 3, 3]]
allocated = [[0, 1, 0 ], [ 2, 0, 0 ], [3, 0, 2 ], [2, 1, 1] , [ 0, 0, 2]]

P = len(processes)
R = len(available)

def calculateNeed(maximum, allocated):
    need = [[0 for j in range(R)] for i in range(P)]
    for i in range(len(maximum)):
        for j in range(len(maximum[0])):
            need[i][j] = maximum[i][j] - allocated[i][j]
    return need

def BankerAlgorithm(processes, available, maximum, allocated):
    safeSequence = []
    need = calculateNeed(maximum, allocated)
    while processes:
        found = False
        finished = []
        for j in range(len(need)):
            processNeed = need[j]
            i = 0
            for resource in processNeed:
                if resource > available[i]:
                    break
                i += 1
            else:
                found = True
                safeSequence.append(processes[j])
                finished.insert(0, j)
                i = 0
                for resource in allocated[j]:
                    available[i] += resource
                    i += 1
        for process in finished:
            del processes[process]
            del need[process]
            del maximum[process]
            del allocated[process]
        if found == False:
            print("System is not in safe state.")
            return
    else:
        print("System is in safe state.")
        print("Safe sequence:", safeSequence)
        return

BankerAlgorithm(processes, available, maximum, allocated)
