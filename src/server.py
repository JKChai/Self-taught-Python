## build a server for client side

import socket

HOST = "127.0.0.1" ## localhost standard loopback interface address
PORT = "3900" ## non-privilege hosts are > 1023

## initialize socket object using context-manager
## use IPV4 address & TCP to connect
with socket.socket(family=socket.AF_INET, SocketKind=socket.SOCK_STREAM) as s:
    ## intialize socket based on the type of family address
    s.bind((HOST, PORT)) ## IPV4 needed 2-tuple
    
    ## listen method has backlog parameter
    ## by specifying number of unaccepted connections that the system
    ## will allow before refusing new connections
    ## if servers received a lot of conncetion requests simultaneously
    ## increasing backlogs might help by setting max length of queue for pending connections
    s.listen() ## make server to accept connection
    conn, addr = s.accept() ## block execution and waits for an incoming connection

    ## run client socket objects
    with conn:
        print(f'Connected by {addr}')
        print(f'Object Received: \n{conn}\n')

        while True:
            data = conn.recv(1024) ## receive data send from clients as byte objects
            
            ## if there is no data break the loop
            ## indicates that the clients closed the objects
            if not data:
                break
            else:
                print(f'{"#"*50}\n{data}\n{"#"*50}')
                conn.sendall(data) ## reads data and show the data

