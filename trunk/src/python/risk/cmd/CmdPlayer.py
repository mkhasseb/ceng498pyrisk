'''
Created on 2011 4 1

@author: cihancimen
'''
from risk.Player import Player
from risk.command.CommandParser import ParseException
from risk.command.PlaceCommand import PlaceCommand

class CmdPlayer(Player):
    '''
    classdocs
    '''


    def __init__(self, color):
        '''
        Constructor
        '''
        Player.__init__(self, color);
        
    def placeSingle(self, game):
        print'Turn of %s have %d armies. Place one army (PLACE Alaska)' % (self.color, self.armies)
        done = False
        while(not done):
            try:
                command = game.parser.parse(raw_input())
                if(isinstance(command, PlaceCommand)):
                    terr =command.territory
                    if(terr.occupant):
                        print 'Territory %s occupied by %s' % (terr.name, terr.occupant.color)
                    else:
                        terr.occupant = self
                        self.armies -=1
                        done = True
                        print "%s occupied %s" % (terr.occupant.color, terr.name)
            except(ParseException):
                print 'Enter a proper command'
        
        
        