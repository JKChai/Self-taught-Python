import time
import socket

## path to data
path = 'C:\\Users\\chai8\\Downloads\\TweepyWork\\'
data = path + 'final_aggreData.csv'

### established server side socket

host = 'localhost'
port = 3090

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
print(f'[CLIENT] CONNECTION ESTABLISHED')

counter = 0
while True:
    with open(data) as file:
        for line in file:
            s.sendall(str.encode(line))
            time.sleep(0.1)
            counter += 1
            print(f'[CLIENT] {counter}-th DATA SENT')

