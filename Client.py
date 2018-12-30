from socket import *
 
host = 'localhost'
port = 7020
sock = socket()
sock.connect((host, port))
c=1
while True:
    if c:
        sock.send('Connected to client'.encode())
        c=0
        data = sock.recv(1024)
    inp =input("Book tickets? ")
    if inp.lower()=='y':
        while(True):
            try:
                name = input("Enter name: ")
                fno = input("Enter flight number: ")
                sock.send(str([name,fno]).encode())
                print(sock.recv(1024).decode())
                data1 = sock.recv(1024)
                data1 = eval(data1.decode())
                print("Data: ",data1)
            except:
                data1 = str(data1.decode())
                print(data1)
            
sock.close()
