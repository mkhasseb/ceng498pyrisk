'''
Created on 2011 4 14

@author: cihancimen
'''
import sys
from risk.command.CommandParser import ExitCommand
from risk.Connector import Connector
from threading import Thread
from Queue import Queue
from risk.command.CommandParser import ParseException
from risk.command.ListCommand import ListCommand
import socket

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
            try:
                str = self.socket.recv(100)
                try:
                    command = self.game.parser.parse(self.player, str)
                    if(isinstance(command, ListCommand)):
                        self.socket.send(command.verbose+"\n")
                    ##In phase 2 this is left as if so all list commands are outputting duplicate 
                    elif(isinstance(command, ExitCommand)):
                        self.game.broadcast("%s has left the game" % (self.player.color))
                        self.game.exit()
                    else:
                        self.queue.put(command.orig)
                except ParseException as e:
                    self.socket.send(e.mess)
                except Exception as e:
                    self.socket.send('Some undesired condition occured, ressetting client buffers...')
                    print e
                    self.queue.empty()
            except Exception as e:
                print 'Connector for player %s is terminated: %s' % (self.player.color, e)
                self.game.exit()
                return