import socket

# host = socket.gethostname()
host = "localhost"
port = 3090

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

counter = 0
while True:

    s.sendall(b'[CLIENT] Data Sent :: Loop ' + str(counter).encode('ascii')) ## send data to server

    data = s.recv(1024) ## received data from server
    human_readable = str(data, "utf-8")
    print(f'[CLIENT] Data Received: \n{human_readable}')

    #######################################

    ## process data

    #######################################

    counter += 1

    if not data:
        # s.sendall() ## send data to server
        print(f'[CLIENT] No data - Break while loop')
        break

s.close() ## send close connection to server
print(f'[CLIENT] Close Connection')