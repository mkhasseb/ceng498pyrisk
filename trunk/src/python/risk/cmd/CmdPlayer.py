'''
Created on 2011 4 1

@author: cihancimen
'''
from risk.Player import Player
from risk.command.CommandParser import ParseException
from risk.command.PlaceCommand import PlaceCommand
from risk.command.ListCommand import ListCommand

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
        print'Turn of %s have %d armies. Place one army (Usage: Place <territory name>)' % (self.color, self.armies)
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
                        terr.num_army += 1
                        self.armies -=1
                        done = True
                        print "%s occupied %s" % (terr.occupant.color, terr.name)

                elif(isinstance(command, ListCommand)):
                    print command.verbose
                    
            except(ParseException):
                print 'Enter a proper command'
        
    def placeArmies(self, game):
        print 'Turn of %s have %d armies. Place remaining armies (Usage: Place <territory name> <army number>)' % (self.color, self.armies)
        done = False
        while(not done):
            try:
                command = game.parser.parse(raw_input())
                if(isinstance(command, PlaceCommand)):
                    terr = command.territory
                    num = command.number
                    if (not (terr.occupant == self)):
                        print 'Territory %s occupied by %s' % (terr.name, terr.occupant.color)
                    elif (num > self.armies):
                        print '%s only has %s armies' %(self.color, self.armies)
                    else:
                        terr.num_army += num
                        self.armies -= num
                        if(self.armies == 0):
                            done = True
                        print 'Territory %s has %s armies by %s' % (terr.name, terr.num_army, terr.occupant.color)
                        
                elif(isinstance(command, ListCommand)):
                    print command.verbose
            except(ParseException):
                print 'Enter a proper command'


