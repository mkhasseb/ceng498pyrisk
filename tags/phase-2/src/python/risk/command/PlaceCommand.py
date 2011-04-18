'''
Created on 2011 4 1

@author: cihancimen
'''
from risk.command.AbstractCommand import AbstractCommand

class PlaceCommand(AbstractCommand):
    '''
    classdocs
    '''
    def __init__(self, orig,territory, number):
        '''
        Constructor
        '''
        AbstractCommand.__init__(self, orig)
        self.territory = territory
        self.number = number
