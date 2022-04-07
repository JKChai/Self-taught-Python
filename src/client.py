## build client side socket

## SEQUENCE OF Socket API calls & Data Flows for TCP

'''
+--------+
| Server |
+--------+

  Socket
    |
    V

   bind
    |
    V
                                            socket
  listen                                      |
    |                                         V   
    V

  accept
    |
    |
    |
    V

  listen
    |
    |
    |
    V


'''

## client starts to establish 3-ways handshake connection during connect method
## THEN it will be the loop of client sending data server receiving data then server sending data client receivinf data
## this loop breaks when client closes and server receiving close messages
##
## SERVER: Socket -> bind -> listen -> accept ------>  recv <--> send --> recv -> close
##                                              |       to       from      to
##                                              |       |         |         |
##                                              |      from       to      from
## CLIENT:                        socket -> connect -> send <--> recv --> close
import socket

## use the same port and address as the server does
HOST = "127.0.0.1" ## localhost standard loopback interface address
PORT = "3900" ## non-privilege hosts are > 1023

## initialize socket object using context-manager
## use IPV4 address & TCP to connect
with socket.socket(family=socket.AF_INET, SocketKind=socket.SOCK_STREAM) as s:
    ## connect to the servers and calls
    s.connect((HOST, PORT)) ## IPV4 needed 2-tuple

    ## send messages from the client side
    s.sendall("Calling from the Client side... HI!")
    data = s.recv(1024)
    
print(f'Received {data!r}')