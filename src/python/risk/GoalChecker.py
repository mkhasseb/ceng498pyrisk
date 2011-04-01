'''
Created on 2011 4 1

@author: cihancimen
'''

class GoalChecker(object):
    '''
    classdocs
    '''


    def __init__(self, game):
        '''
        Constructor
        '''
        self.game  = game
    def check(self):
        #if victor is found raise VictorFound exception
        pass
class VictorFound(Exception):
    
    def __init__(self, victor):
        Exception.__init__(self)
        self.victor= victor