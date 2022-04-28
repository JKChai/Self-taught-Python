import csv
import time
import socket

### received data
path = 'C:\\Users\\chai8\\Downloads\\TweepyWork\\'
barstream = path + 'user_geo_political.csv'
mlstream = path + 'mltest.csv'

### established server side socket
host = 'localhost'
port = 3090

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
print(f'[SERVER] Established at {host}:{port}')

s.listen(1) ## only have 1 connection, not supporting more than 1 client
conn, addr = s.accept()
print(f'[SERVER] Connected by {addr}')

with open(barstream, 'r', encoding='UTF-8') as file:
    obj = csv.reader(file)
    for line in obj:
                
        ## user & location
        user = line[0]
        location = line[1]

        ## join list into string
        line = ' '.join(line[2:])
        # line = line.replace('\n', '')

        ## must have \r\n as new line for windows 
        ## bc of TextStream method
        line = user + '::::' + location + '::::' + line + '\r\n'

        conn.send(bytes(line, "utf-8"))
        print(f'[SERVER] Sending --> {bytes(line, "utf-8")}')
        time.sleep(0.1)

## close connection
conn.close()
print(f'[SERVER] Close Connection')