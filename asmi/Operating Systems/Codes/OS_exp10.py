import sys

def nextFit(memory, processes):
    processNames = list(processes.keys())
    allocation = { k : "" for k in processNames}
    memoryBlocks = [list(x) for x in zip(memory.items(), [True] * (len(memory)))]
    i = 0
    for process, requirement in processes.items():
        for j in range(4):
            (block, size), avail = memoryBlocks[i]
            if size >= requirement and avail:
                allocation[process] = block
                memoryBlocks[i][1] = False
                break
            i = (i + 1) % 4
        else:
            allocation[process] = 'No memory available'
    print("Memory Allocation according to Next Fit:")
    printTable(allocation)
    return

def bestFit(memory, processes):
    processNames = list(processes.keys())
    allocation = { k : "" for k in processNames}
    for process, requirement in processes.items():
        memoryBlocks = list(memory.keys())
        holeSize = { k : sys.maxsize for k in memoryBlocks}
        for block, size in memory.items():
            if size >= requirement:
                holeSize[block] = size - requirement
        minHoleSize = min(holeSize.values())
        try:
            block = [key for key in holeSize if holeSize[key] == minHoleSize][0]
            allocation[process] = block
            del memory[block]
        except IndexError:
            allocation[process] = 'No memory available'
    print("Memory Allocation according to Best Fit:")
    printTable(allocation)
    return

def printTable(allocationTable):
    for process, block in allocationTable.items():
        print(process, block, sep = '  :  ')
    print()

# memoryBlocks = {
#     'Block A' : 100,
#     'Block B' : 50,
#     'Block C' : 200,
#     'Block D' : 75
# }

# processRequirement = {
#     'Process 1' : 80,
#     'Process 2' : 100,
#     'Process 3' : 25,
#     'Process 4' : 50
# }

memoryBlocks = {
    'Block A' : 200,
    'Block B' : 300,
    'Block C' : 150,
    'Block D' : 400,
    'Block E' : 100
}

processRequirement = {
    'Process 1' : 250,
    'Process 2' : 150,
    'Process 3' : 200,
    'Process 4' : 300
}

print("Initial memory blocks:")
printTable(memoryBlocks)
print("Process requirements:")
printTable(processRequirement)
nextFit(memoryBlocks, processRequirement)
bestFit(memoryBlocks, processRequirement)