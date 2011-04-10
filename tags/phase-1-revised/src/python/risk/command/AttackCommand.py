'''
Created on 2011 4 2

@author: cihancimen
'''

class AttackCommand(object):
    '''
    classdocs
    '''


    def __init__(self, fromTerr, toTerr, diceNum):
        '''
        Constructor
        '''
        self.fromTerr = fromTerr
        self.toTerr = toTerr
        self.diceNum = diceNum
        
