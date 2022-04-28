import csv
import time
import socket

### received data
path = 'C:\\Users\\chai8\\Downloads\\TweepyWork\\'
data = path + 'dingyi.csv'

### established server side socket

host = 'localhost'
port = 3090

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
print(f'[SERVER] Established at {host}:{port}')

s.listen(1) ## only have 1 connection, not supporting more than 1 client
conn, addr = s.accept()
print(f'[SERVER] Connected by {addr}')

## TCP handshake
while True:
    
    try:

        ## PROCESSED DATA

        with open(data, 'r', encoding='UTF-8') as file:
            lines = csv.reader(file)
            # print(lines)

            for idx, line in enumerate(lines):
                
                ## user & location
                user = line[0]
                location = line[1]

                ## join list into string
                line = ' '.join(line[2:])
                line = line.replace('\n', '')

                # line = line.encode(encoding = 'UTF-8')

                data = conn.recv(1024)

                if not data:
                    print(f'[SERVER] Client Closed Connection - Break loop')
                    break

                print(f'[SERVER] Received from CLIENT : \n\t {repr(data)}')

                conn.send(bytes(line, 'utf-8'))
                print(f'[SERVER] Send Data :: line {idx}')

                ## slow the process
                time.sleep(1)

        ## last handshake from server to client before breaking
        data = conn.recv(1024)

        if not data:
            print(f'[SERVER] Client Closed Connection - Break loop')
            break

        print(f'[SERVER] Received from CLIENT : \n\t {repr(data)}')

        break ## end this loop for client b''

#############################################################
        # with open(clean_media, 'rb') as file:
        #     lines = file.readlines()

        #     for line in lines:
        #         data = conn.recv(1024) ## received data from client
        #         print(f'Received from Client:\n{data}')

        #         conn.sendall(line) ## send data to client
            
        # ## second last handshake
        # data = conn.recv(1024) ## received data from client
        # print(f'Received from Client: Data Finished Sending \n{data}')
        # conn.sendall(b'END') ## send empty data

        # ## last handshake
        # ## receive close connection
        # if not data:
        #     break ## stop the socket by closing it
#############################################################

    except socket.error as err:
        print(f'[SERVER] Error Occured:\n{err}')
        break

conn.close()
print(f'[SERVER] Close Connection')
