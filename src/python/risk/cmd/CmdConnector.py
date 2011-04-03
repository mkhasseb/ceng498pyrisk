'''
Created on 2011 4 3

@author: cihancimen
'''
from risk.Connector import Connector

class CmdConnector(Connector):
    '''
    classdocs
    '''


    def __init__(self):
        Connector.__init__(self)
        '''
        Constructor
        '''
    def send(self, message):
        print message
    def receive(self):
        return raw_input()