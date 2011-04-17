'''
Created on 2011 4 17

@author: cihancimen
'''
import sys
from threading import Thread
import socket

class ClientReader(Thread):
    def __init__(self, socket):
        Thread.__init__(self)
        self.socket = socket;
        self.end = False;
    def run(self):
        while(not self.end):
            str = self.socket.recv(10000)
            print str
            print '-------------------------'
            
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
    
    
    reader = ClientReader(s)
    reader.start()
    while(True):
        str = raw_input()
        reader.send(str)
        
        

    
        