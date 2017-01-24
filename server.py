# Echo server program
import socket
import threading

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()

class listenForConnectionsThread(threading.Thread):
    def __init__(self):
        self.connectionList = []
        pass

    def run(self):
        pass
print 'Connected by', addr
while 1:
    data = conn.recv(1024)
    conn.sendall(data)

