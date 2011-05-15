'''
Created on 2011 4 14

@author: cihancimen
'''
import sys
from risk.command.CommandParser import ExitCommand, MapCommand, MapImageCommand
from risk.Connector import Connector
from threading import Thread
from Queue import Queue
from risk.command.CommandParser import ParseException
from risk.command.ListCommand import ListCommand
import socket

class MapSocketConnector(Connector):
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
        
    def set_env(self, game = None, player = None):
        self.game = game
        self.player = player
        self.listener = Listener(self.socket, self.cmds, game, player)
        self.listener.start()
        
    def send(self, mess):
        self.socket.send(mess+"\n")
    def receive(self):
        return self.cmds.get(True)
    def close(self):
        self.listener.socket.shutdown(socket.SHUT_RDWR)
        self.listener.socket.close()
        self.listener.live = False;
        
class Listener(Thread):
    def __init__(self, socket, queue, game, player):
        Thread.__init__(self)
        self.socket = socket
        self.game = game
        self.player = player
        self.queue = queue
        self.live = True;
        self.daemon = True
        self.setDaemon(True)
    def run(self):
        while(self.live):
            str = self.socket.recv(100)
            try:
                command = self.game.parser.parse(self.player, str)
                if(isinstance(command, ListCommand)):
                    self.socket.send(command.verbose+"\n")
                elif(isinstance(command, MapCommand)):
#                        self.game.locks[self.player].acquire()
                    print 'map request is taken'
                    self.socket.send(command.map)
                    self.socket.send("EOF")
                    print 'map is sent'
#                        self.game.locks[self.player].release()
                elif(isinstance(command, MapImageCommand)):
#                        self.game.lock.acquire()
                    self.socket.send(command.mapimg)
                    self.socket.send("EOF")
#                        self.game.locks[self.player].release()
            except ParseException as e:
                self.socket.send(e.mess)
            except Exception as e:
                self.socket.send('Some undesired condition occured, ressetting client buffers...')
                print e
                self.queue.empty()