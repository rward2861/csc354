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
/* Filename:          socket_communication.py
/* Purpose:           To write a server that will communicate with a client (which will also be a server) via client/server communication
/************************************************************/
"""
import socket
import sys, os 

def Main():
    ipaddress = "127.0.0.1"
    IPaddr = socket.gethostbyname(ipaddress) #translate hostname to ip address
    message = "TEST"
    bufferSize = 1024
    port = 4444
    serverInfo = ((IPaddr, port)) 
    
    try: #Attempt to connect to server
        clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        clientSocket.connect(serverInfo)
        print ('You have successfully connected')
    except socket.error as err:
        print('Socket connection error:', err)
        sys.exit()
        
    try:
        status = clientSocket.recv(bufferSize) #attempt to receive wait message 
        status = status.decode()
    except socket.error as msg:
        print ('Unable to receive message from server: ' + str(msg[0]))
    
    connection = True 
    while connection:
        try:
             final = clientSocket.recv(4) #Receieve GO from server
             final = final.decode() 
        except Exception as s:
            print ('Unable to send client input and READY message: ', s)
            sys.exit(0)
        if (final == "TEST"):
            cInput(clientSocket)
            connection = False
            clientSocket.close()         

if __name__ == '__main__': #ensures in current module Main 
    Main()
else:
    sys.exit(0)