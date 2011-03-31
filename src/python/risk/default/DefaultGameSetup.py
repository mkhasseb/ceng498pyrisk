'''
Created on 2011 3 31

@author: cihancimen
'''
from risk.Goal import GoalFactory



class DefaultGameSetup(object):
    '''
    classdocs
    '''
    
    
    def __init__(self):
        '''
        Constructor
        '''
    def getGoals(self):
        goals = []
        
        goals.append(GoalFactory.createConquer())
        
        
        return goals;