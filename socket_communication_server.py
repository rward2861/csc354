#!/usr/bin/env python3

"""
/************************************************************/
/* Author(s):         3JRS - Janeel, Jennie, Jess, Richie, Steph
/* Major:             Information Technology
/* Compiler:          Python 3.6                  
/* Creation Date:     4/29/18
/* Due Date:          12/12/18
/* Course:            CSC354-020
/* Professor Name:    Prof. Demarco
/* Assignment:        Software Engineering Project (Prototype)
/* Filename:          socket_communication_server.py
/* Purpose:           To write a server that will communicate with a client (which will also be a server) via client/server communication
/************************************************************/
"""
import socket
import sys, os 

def Main():
    ipaddress = "127.0.0.1"
    connections = [] #create list for client connections 
    bufferSize = 1024 
    port = 4444
    
    try:
        serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #create a server socket 
    except OSError as e:
        print ('Socket creation was a failure: ' + e)
    try:
        serverSocket.bind((socket.gethostname(), port)) #attempt to bind server socket with hostname and port inputted from client 
    except socket.error as msg:
        print('Bind attempt was a failure.  Error code is as follows: ' + str(msg[0]) + ' Message ' + msg[1])
        sys.exit(0)
        
    while True:
        serverSocket.listen(1) #listen for incoming connections 
       
        try:
            clientConn = serverSocket.accept() #attempt to accept first connection 
            connections.append(clientConn) #if success, append to clientConn 
        except socket.error as e:
            print ('Unable to accept incoming client: ' % format(err.errno, err.strerr))
            sys.exit(0)
        try:
            user1 = connections[0][0].recv(bufferSize) 
            user1 = user1.decode() 
        except Exception:
            print ('Unable to decode message')
        
        else: #execute if both sent READY message 
            final_message = 'TEST'
            connections[0][0].send(final_message.encode()) 
           
    serverSocket.close() #close socket 
        
if __name__ == '__main__': #ensure using main module 
    Main()
else:
    sys.exit(0) 