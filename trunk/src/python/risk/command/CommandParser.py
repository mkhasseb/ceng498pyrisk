'''
Created on 2011 4 1

@author: cihancimen
'''
from risk.command.ListCommand import ListCommand
from risk.command.PlaceCommand import PlaceCommand

class CommandParser(object):
    '''
    classdocs
    '''
    '''Place <Territory> <ArmyNumber=1>'''
    COMMAND_PLACE = "place"
    COMMAND_MOVE = "move"
    COMMAND_LIST = "list"
    AVAILABLE_COMMANDS = [COMMAND_PLACE, COMMAND_LIST]

    def __init__(self, game):
        '''
        Constructor
        '''
        self.game = game
    def parse(self, command_str):
        words = command_str.strip().split(" ")
        cmd = words[0].strip().lower()
        if(not (cmd in CommandParser.AVAILABLE_COMMANDS)):
            raise ParseException()
        
        if(cmd == CommandParser.COMMAND_PLACE):
            try:
                ter = self.game.territories[words[1].strip()]
                if(len(words) > 2):
                    num = int(words[2])
                else:
                    num = 1
                return PlaceCommand(ter, num)
            except(Exception):
                raise ParseException()
            
        elif(cmd == CommandParser.COMMAND_LIST):
            try:
                if(words[1].strip().lower() == "myterritories"):
                    terrs = ""
                    i = 1
                    terrs += self.game.turner.player.color + "\n"
                    for ter in self.game.territories.values():
                        if(ter.occupant == self.game.turner.player):
                            terrs += str(i) + " " + ter.name + " - Army Number:" + str(ter.num_army) + "\n"
                            i += 1
                    return ListCommand(terrs)
                elif(words[1].strip().lower() == "unoccupied"):
                    terrs = ""
                    for ter in self.game.territories.values():
                        if(not(ter.occupant)):
                            terrs += ter.name + "  "
                    return ListCommand(terrs)
            except(Exception):
                raise ParseException()

        else:
            raise ParseException()

        '''elif(cmd == CommandParser.COMMAND_MOVE):
            try:
                num = int(words[1])
                fromTer = self.game.territories[words[3].strip()]
                toTer = self.game.territories[words[5].strip()]'''

class ParseException(Exception):
    def __init__(self):
        Exception.__init__(self)