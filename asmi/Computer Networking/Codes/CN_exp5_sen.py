import time, socket
import numpy as np
import multiprocessing as mp

def my_timer(time_queue, nextSeqNum):
    print(f"Started {nextSeqNum}")
    time.sleep(5)
    print(f"Timeout {nextSeqNum}")
    time_queue.put(f"Timeout {nextSeqNum}")

if __name__ == '__main__':
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        print("Socket successfully created!")
    except socket.error as err: 
        print("socket creation failed with error %s" %(err))
        exit()

    host = socket.gethostname()
    ip = socket.gethostbyname(host)
    print(host, "(", ip, ")\n")
    port = 12345
    s.bind((host, port))
    print ("Socket binded to %s" %(port)) 
            
    s.listen(3)
    print ("Listening for incoming connections...") 

    conn, addr = s.accept()
    print("Received connection from ", addr[0], "(", addr[1], ")\n")

    client = conn.recv(1024)
    client = client.decode()
    print(client, "is connected!")
    conn.send(host.encode())

    frames = int(input("Enter number of frames to be sent: "))
    N = int(input("Enter size of sender window: "))

    sendBase = 0
    nextSeqNum = 0

    timers = []
    time_queue = mp.Queue()

    while True:
        window = [i for i in range(sendBase, sendBase + N) if i < frames]
        print("\nSender window:", window)
        if nextSeqNum in window:
            print("Sending packet", nextSeqNum)
            message = f"Packet {nextSeqNum}"
            time.sleep(2)
            conn.send(message.encode())
            timer = mp.Process(target=my_timer, args=(time_queue, nextSeqNum))
            timer.start()
            timers.append(timer)
            nextSeqNum += 1
        
        try:
            conn.settimeout(5)
            ack = conn.recv(1024)
            ack = ack.decode()
            ack_no = int(ack[-1])
            if np.random.choice([0,1], p = [0.25, 0.75]):   # ACK received?              
                print(f"ACK {ack_no}")
                if ack_no == sendBase + 1:
                    sendBase += 1
                    timers[0].terminate()
            else:
                print(f"Ack {ack_no} lost")
        except TimeoutError:
            pass
        
        print(time_queue.qsize())
        while not time_queue.empty():
            timeout_msg = time_queue.get()
            for timer in timers:
                timer.terminate()                
            timers = []
            nextSeqNum = sendBase
        
        if sendBase == frames - 1 and timers == []:
            break

    print("Closing connection.")
    s.close()