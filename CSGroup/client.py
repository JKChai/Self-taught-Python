from msilib.schema import Binary
import socket

host = socket.gethostname()
port = 3090

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

counter = 0
while True:

    s.sendall(b'[CLIENT] Data Sent :: Loop ' + str(counter).encode('ascii')) ## send data to server

    data = s.recv(1024) ## received data from server
    print(f'[CLIENT] Data Received: \n{repr(data)}')

    counter += 1

    if not data:
        # s.sendall() ## send data to server
        print(f'[CLIENT] No data - Break while loop')
        break

s.close() ## send close connection to server
print(f'[CLIENT] Close Connection')