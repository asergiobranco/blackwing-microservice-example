import socket 
from msgpack import packb, unpackb
import time 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(("localhost", 5000))

for _ in range(30):
    s.sendall(packb(10))
    print(unpackb(s.recv(1024)))
    time.sleep(3)