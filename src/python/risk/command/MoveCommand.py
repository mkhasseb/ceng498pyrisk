'''
Created on 2011 4 2

@author: cihancimen
'''
from risk.command.AbstractCommand import AbstractCommand

class MoveCommand(AbstractCommand):
    '''
    classdocs
    '''


    def __init__(self,orig, fromTerr, toTerr, num):
        '''
        Constructor
        '''
        AbstractCommand.__init__(self, orig)
        self.fromTerr = fromTerr
        self.toTerr = toTerr
        self.num = num
        
