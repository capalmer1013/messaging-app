# Echo client program
import socket

HOST = '54.218.251.198'    # The remote host
PORT = 50007              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
try:
    while True:
        newMessage = raw_input(">>>")
        s.sendall(">>>"+str(newMessage))
        data = s.recv(1024)
except KeyboardInterrupt:
    s.close()
print 'Received', repr(data)
