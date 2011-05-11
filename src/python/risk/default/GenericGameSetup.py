'''
Created on 2011 5 7

@author: cihancimen
'''
from risk.Player import Player
import socket
from risk.connector.SocketConnector import SocketConnector
from risk.Game import Game
from risk.connector.MapSocketConnector import MapSocketConnector

class GenericGameSetup(object):
    '''
    classdocs
    '''


    def __init__(self,host, port, numPlayer):
        '''
        Constructor
        '''
        self.host = host
        self.port = port
        self.numPlayer = numPlayer
    def initGame(self, continents, cards, goals, p):
        colors = [Player.COLOR_BLACK, Player.COLOR_BLUE, Player.COLOR_GRAY, Player.COLOR_GREEN, Player.COLOR_RED, Player.COLOR_YELLOW]
        players = []
        mapServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mapServer.bind((self.host, self.port + 1))
        server.bind((self.host, self.port))
        server.listen(5)
        mapServer.listen(5)
        ss = []
        mss = []

        for i in range(self.numPlayer):
            cs  = server.accept()
            mcs = mapServer.accept()
            ss.append(cs[0])
            mss.append(mcs[0])
            p.log("Player %s connected to server." % (colors[i]))
            cs[0].send("Welcome Player %s. Gl Hf." % (colors[i]))
            for j in range(i):
                ss[j].send("Player %s connected to server.\n" % (colors[i]))
            if(not (self.numPlayer - 1 - i == 0)):
                p.log("Waiting %s players to start game." % (self.numPlayer - 1 - i))
                for j in range(i):
                    ss[j].send("Waiting %s players to start game.\n" % (self.numPlayer - 1 - i))

        p.log("Game starting...")
        
        '''Players'''
        for i in range(self.numPlayer):
            players.append(Player(colors[i], SocketConnector(ss[i]), MapSocketConnector(mss[i])))

        g = Game(continents, goals, cards, players, map = p.map, mapImage=p.mapImg);
    
        for j in range(self.numPlayer):
            ss[j].send("Game starting...\n")
        return g