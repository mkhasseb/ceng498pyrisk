'''
Created on 2011 4 2

@author: cihancimen
'''
from risk.command.AbstractCommand import AbstractCommand

class AttackCommand(AbstractCommand):
    '''
    classdocs
    '''


    def __init__(self,orig , fromTerr, toTerr, diceNum):
        '''
        Constructor
        '''
        AbstractCommand.__init__(self, orig)
        self.fromTerr = fromTerr
        self.toTerr = toTerr
        self.diceNum = diceNum
        
