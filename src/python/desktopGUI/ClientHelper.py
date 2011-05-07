# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="ozgur"
__date__ ="$May 6, 2011 12:25:30 AM$"

class ClientHelper():
    def __init__(self, game):
        '''
        GUI constructor
        '''
        #TO-DO
        
        self.game= game
        self.cards = []
        self.teritories = {}
        self.continents = []
        self.player = None
        self.socket = 3

    def place(self, army = None, terr = None):
        if(not army):
            self.socket.send('Place ' + terr)
            str = self.socket.recv(1024)
            str = str.strip()
            if(str.split(' ')[0] == 'Territory'):
                #updateList(str)
                return
            else:
                #updateList(str)
                return
        else:
            self.socket.send('Place ' + terr + ' ' + str(army))
