import socket


#soc creation
s = socket.socket()

print("socket creation successful")
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('localhost',10800))

#3 connection allowed
s.listen(3)
print("waiting for connections")

while True:
    c, addr = s.accept()

    print ("connected with" , addr) #connection
    name =c.recv(1024).decode()
    print("client name:", name) #connect with who
    #server message
    c.send(bytes("welcome to ProHash",'utf-8'))
    
    c.close()
    



    