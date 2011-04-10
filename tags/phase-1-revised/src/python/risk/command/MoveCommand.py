'''
Created on 2011 4 2

@author: cihancimen
'''

class MoveCommand(object):
    '''
    classdocs
    '''


    def __init__(self, fromTerr, toTerr, num):
        '''
        Constructor
        '''
        self.fromTerr = fromTerr
        self.toTerr = toTerr
        self.num = num
        
