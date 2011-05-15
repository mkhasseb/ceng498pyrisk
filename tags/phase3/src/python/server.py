'''
Created on 2011 4 14

@author: cihancimen
'''
import socket
from threading import Thread

class Client(Thread):
    def __init__(self, socket):
        Thread.__init__(self)
        self.socket = socket
    def run(self):
        while(True):
            str = self.socket.recv(100)
            self.socket.send('U said: ' + str)


if __name__ == '__main__':
    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print socket.gethostname()
    server.bind((socket.gethostname(), 8081))
    server.listen(5)
    while(True):
        print 'about to accept'
        cs = server.accept()
        c = Client(cs[0])
        c.start()
    

            