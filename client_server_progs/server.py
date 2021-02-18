import socket 
host = socket.gethostname() 
port = 12345 
s = socket.socket() 
s.bind((host, port)) 
s.listen(5) 
conn, addr = s.accept() 
print('Got connection from ',addr[0], '(', addr[1], ')') 
print('Thank you for connecting') 
print('Welcome to the IOT 2nd Lab internals')
print('MSIS')
while True:  
   data = conn.recv(1024)    
   if not data: break    
   conn.sendall(data) 
conn.close()