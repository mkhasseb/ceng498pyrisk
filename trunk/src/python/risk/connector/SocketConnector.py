'''
Created on 2011 4 14

@author: cihancimen
'''
from risk.Connector import Connector
from threading import Thread
from Queue import Queue
from risk.command.CommandParser import ParseException
from risk.command.ListCommand import ListCommand

class SocketConnector(Connector):
    '''
    classdocs
    '''


    def __init__(self, socket):
        '''
        Constructor
        '''
        ''''Initialize a thread to listen for commands'''
        self.socket = socket
        self.cmds = Queue()
        self.game = None
        
    def set_game(self, game):
        self.game = game
        self.listener = Listener(self.socket, self.cmds, game)
        self.listener.start()
        
    def send(self, mess):
        self.socket.send(mess+"\n")
    def receive(self):
        return self.cmds.get(True)
        
class Listener(Thread):
    def __init__(self, socket, queue, game):
        Thread.__init__(self)
        self.socket = socket
        self.game = game
        self.queue = queue
    def run(self):
        while(True):
            str = self.socket.recv(100)
            try:
                command = self.game.parser.parse(str)
                if(isinstance(command, ListCommand)):
                    self.socket.send(command.verbose+"\n")
                else:
                    self.queue.put(command.orig)
            except ParseException as e:
                self.socket.send(e.mess)
            except Exception:
                self.socket.send('Some undesired condition occured, ressetting client buffers...')
                self.queue.empty()
        