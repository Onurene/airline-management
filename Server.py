from socket import *
from _thread import *
host = ''
port = 7020
sock = socket()
sock.bind((host, port))  
sock.listen(5)
clients = []
tickets = 500
code = {"AI":"Air India","BA":"British Airways","LF":"Luftansa"}
tree = {"flights":{"Air India":{"AI102":[5,[]],"AI105":[5,[]]},"British Airways":{"BA102":[5,[]],"BA105":[5,[]]},"Luftansa":{"LF102":[5,[]],"LF105":[5,[]]}}}
def check(inp):
     global tree
     global code
     # inp is in the form of 0:name 1:flno
     if(inp[1][:2] in code):
          print(1)
          
          if(inp[1] in tree["flights"][code[inp[1][:2]]]):
             print(2)
             if(tree["flights"][code[inp[1][:2]]][inp[1]][0]>0):
                  print(3)
                  tree["flights"][code[inp[1][:2]]][inp[1]][0] -= 1
                  tree["flights"][code[inp[1][:2]]][inp[1]][1].append(inp[0])
                  return True
     return False
def clientthread(conn):
     c=1
     
     clients.append(conn)
     while True:
         if c:
             conn.send('Connected to server'.encode())
             c=0
         data = conn.recv(1024)
         print (data.decode())
         try:
             li = eval(data.decode())
             print(li[0],", you booked in flight ",li[1])
             if(check(li)):
                 conn.send("Thanks for Booking...".encode())
                 conn.send(str(tree).encode())
             else:
                 conn.send("Invalid input or tickets got over...".encode())
                 conn.send("Please try again!".encode())
         except Exception as e:
             print(e)
             pass
            
while True:
    conn, addr = sock.accept()
    start_new_thread(clientthread,(conn,))
conn.close()
sock.close()
