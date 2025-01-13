from threading import Thread
from random import random, randint
import time

# Shared Memory
CAPACITY = 3
buffer = []

# Semaphores
semaphores = {
    'mutex' : 1,
    'amt_full' : 0,
    'amt_empty' : CAPACITY
}

def wait(S):
    global semaphores
    value = semaphores[S]
    if value > 0:
        semaphores[S] = value - 1
        return False
    else:
        return True

def signal(S):
    global semaphores
    value = semaphores[S]
    semaphores[S] = value + 1
    return

# Producer Thread
def Producer():
    print("Producer: Running")
    global buffer, semaphores
    items_produced = 0
    while items_produced < 10:
        while wait('mutex'):
            pass
        while wait('amt_empty'):
            pass
        time.sleep(random())
        item = items_produced + 1
        buffer.append(item)
        items_produced += 1
        print("Producer produced item:", item)
        signal('amt_full')
        signal('mutex')
        if randint(0,2):
            time.sleep(randint(1,2))
    print("Producer: Done")
    return

# Consumer Thread
def Consumer():
    print("Consumer: Running")
    global buffer, semaphores
    items_consumed = 0
    while items_consumed < 10:
        while wait('mutex'):
            pass
        while wait('amt_full'):
            pass
        time.sleep(random())
        if len(buffer) != 0:
            item = buffer[0]
            del buffer[0]
            items_consumed += 1
            print("Consumer consumed:", item)
            signal('amt_empty')
            signal('mutex')
            if randint(0,2):
                time.sleep(randint(1,3))
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