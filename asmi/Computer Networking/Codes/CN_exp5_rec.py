import time, socket, os
import numpy as np

try: 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    print("Socket successfully created!")
except socket.error as err: 
    print("socket creation failed with error %s" %(err))
    exit()

host = socket.gethostname()
ip = socket.gethostbyname(host)
print(host, "(", ip, ")\n")

host = input(str("Enter server address: "))
port = 12345
print("\nTrying to connect to ", host, "(", port, ")\n")
time.sleep(1)
s.connect((host, port))
print("Connected...\n")

s.send(host.encode())
srv_name = s.recv(1024)
srv_name = srv_name.decode()
print(srv_name, "has joined.")

nextSeqNum = 0

while True:
    try:
        print("\nReceiver Window: ", nextSeqNum)
        s.settimeout(7)
        message = s.recv(1024)
        message = message.decode()
        time.sleep(2)
        if np.random.choice([0,1], p = [0.25, 0.75]):       # Frame reveived?
            frame_no = int(message[-1])
            print(f"Received frame {frame_no}")
            if frame_no == nextSeqNum:                      # Expected frame received?
                nextSeqNum += 1
                ack = f"ACK {nextSeqNum}"
                print(f"Sending ACK {nextSeqNum}")
                s.send(ack.encode())
            else:
                print("Frame discarded.")
        else:
            print("Frame lost")
    except TimeoutError:
        print("Conection closed.")
        s.close()
        # os._exit(0)
    except ConnectionResetError:
        print("Connection closed by server.")
        os._exit()