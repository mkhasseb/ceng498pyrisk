'''
Created on 2011 4 3

@author: cihancimen
'''

class Connector(object):
    '''
    Client specific, message sender/receiver
    '''


    def __init__(self):
        '''
        Constructor
        '''
    
    def send(self, message):
        '''Blocking send function'''
        pass
    def receive(self):
        '''Blocking receive function'''
        pass
    def listen(self, message):
        '''Non-Blocking receive function'''
    def set_env(self, game = None, player = None):
        '''If connectors needs access to game override this function'''
        pass
    def close(self):
        '''Release any resources, prepare for shutdown'''
        pass
