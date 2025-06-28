import socket

#create soc
c = socket.socket()

#connection
c.connect(('localhost',10800))

#client input
name = input("enter your name : ")
c.send(bytes(name, 'utf-8'))

#server message
print (c.recv(1024).decode())