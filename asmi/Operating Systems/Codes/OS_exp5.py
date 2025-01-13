from threading import Thread
from random import random, randint
import time

# Shared Memory
buffer = []

# Semaphores
mutex = 1

def wait():
    global mutex
    if mutex > 0:
        mutex -= 1
        return False
    else:
        return True

def signal():
    global mutex
    mutex += 1
    return

# Producer Thread
def Producer():
    print("Producer: Running")
    time.sleep(0.1)
    global buffer, mutex
    items_produced = 0
    while items_produced < 10:
        while wait():
            pass
        item = items_produced + 1
        buffer.append(item)
        items_produced += 1
        print("Producer produced item:", item)
        signal()
        if randint(0,2):
            time.sleep(randint(1,3))
    print("Producer: Done")
    return

# Consumer Thread
def Consumer():
    print("Consumer: Running")
    time.sleep(0.1)
    global buffer, mutex
    items_consumed = 0
    while items_consumed < 10:
        while wait():
            pass
        if len(buffer) != 0:
            item = buffer[0]
            del buffer[0]
            items_consumed += 1
            print("Consumer consumed:", item)
            signal()
            if randint(0,2):
                time.sleep(randint(1,3))
        else:
            signal()
            time.sleep(1)
    print("Consumer: Done")
    return
   
producerThread = Thread(target = Producer)
consumerThread = Thread(target = Consumer)

# start threads
producerThread.start()
consumerThread.start()

# wait for threads to finish
producerThread.join()
consumerThread.join()