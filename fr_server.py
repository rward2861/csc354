''' Facial Recognition Server and power to servo '''

import socket, select
import sys, os
import RPi.GPIO as IO
import time

#Servo Configurations
IO.setwarnings(False)
IO.setmode(IO.BCM)
IO.setup(19,IO.OUT)
p=IO.PWM(19,50)
p.start(7.5)

#Socket Configurations
host = '169.254.208.93'
connections = []
bufferSize = 1024
port = 35300
try:
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #create a server socket
except OSError as e:
    print ('Socket creation was a failure: ' + e)
    
try:
    serverSocket.bind((host, port)) #attempt to bind server socket with hostname and port inputted from client
except socket.error as msg:
    print('Bind attempt was a failure.  Error code is as follows: ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit(0)
while True:
    serverSocket.listen(1) #listen for incoming connections

    try:
        print ('socket not created yet')
        clientConn = serverSocket.accept() #attempt to accept first connection
        connections.append(clientConn) #if success, append to clientConn
        print ('socket created!!')
    except socket.error as e:
        print ('Unable to accept incoming client: ' % format(err.errno, err.strerr))
        sys.exit(0)
    user1 = connections[0][0].recv(bufferSize) #READY message brought in from client
    user1 = user1.decode()
    while user1:
        p.ChangeDutyCycle(7.5)
        time.sleep(5)
        break

    while p.ChangeDutyCycle:
        if p.ChangeDutyCycle is 7.5 or 2.5:
            p.ChangeDutyCycle(12.5)
            p.ChangeDutyCycle(2.5)
            time.sleep(1)
            break
        else:
            p.Change
            break
                
                
serverSocket.close()
    
