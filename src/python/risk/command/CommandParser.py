'''
Created on 2011 4 1

@author: cihancimen
'''
from risk.command.PlaceCommand import PlaceCommand

class CommandParser(object):
    '''
    classdocs
    '''
    '''Place <Territory> <ArmyNumber=1>'''
    COMMAND_PLACE = "place"
    AVAILABLE_COMMANDS = [COMMAND_PLACE]

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
                if(len(words)>2):
                    num = int(words[2])
                else:
                    num = 1
                return PlaceCommand(ter, num)
            except(Exception):
                raise ParseException()
        else:
            raise ParseException()

class ParseException(Exception):
    def __init__(self):
        Exception.__init__(self)