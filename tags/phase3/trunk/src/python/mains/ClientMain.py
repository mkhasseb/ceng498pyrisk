'''
Created on 2011 4 17

@author: cihancimen
'''
import sys
from threading import Thread
import socket
import time

class SocketReader(Thread):
    def __init__(self, socket):
        Thread.__init__(self)
        self.socket = socket;
        self.end = False;
        self.setDaemon(True)
    def run(self):
        while(not self.end):
            str = self.socket.recv(10000)
            str = str.strip()
            if(str != ""):
                print str
                if(str == "Game is ending..."):
                    #f = open('<stdin>', 'w')
#                    sys.stdin.write('exit\n')
                    #f.write('\nexit\n')
                    #f.flush()
                    self.socket.send("exit")
                    self.end = True
                    return
                print '-------------------------'
        return
            
    def send(self, message):
        self.socket.send(message)

class ClientReader(Thread):
    def __init__(self, reader):
        Thread.__init__(self)
        self.end = False;
        self.reader = reader
        self.setDaemon(True)
    def run(self):
        while(not self.end):
            str = raw_input()
            str = str.strip()
            reader.send(str)
            if(str == 'exit'):
                reader.end = True;
        return
            
    def send(self, message):
        self.socket.send(message)
        
if __name__ == '__main__':
    argc = len(sys.argv)
    if(argc != 3):
        print 'takes exactly two arguments <host> <port>'
        sys.exit(0)
    host = sys.argv[1]
    port = int(sys.argv[2])
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    
    
    reader = SocketReader(s)
    client = ClientReader(reader)
    client.start()
    reader.start()
    while(not (client.end or reader.end)):
        time.sleep(1)
    client.end = True;
    reader.end = True;
    sys.exit()
        
        
        

    
        