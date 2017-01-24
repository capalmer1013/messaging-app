# Echo server program
import socket
import threading
import select

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)


class listenForConnectionsThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.connectionList = []
        self.loop = True

    def run(self):
        try:
            while self.loop:
                conn, addr = s.accept()
                print 'Connected by', addr
                self.connectionList.append(conn)
        except KeyboardInterrupt:
            self.loop = False
            exit()


clientThread = listenForConnectionsThread()
clientThread.start()
try:
    while 1:
        listOfMessages = []
        for connection in clientThread.connectionList:
            read, write, error = select.select([connection], [], [])
            if read:
                listOfMessages.append(connection.recv(1024))

        for connection in clientThread.connectionList:
            for message in listOfMessages:
                connection.sendall(message)
except KeyboardInterrupt:
    clientThread.loop = False
    print "shutting down"
    exit()


except Exception as e:
    print e
    clientThread.loop = False
    exit()
    

