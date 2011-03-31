'''
Created on 2011 3 31

@author: cihancimen
'''
from risk.Goal import GoalFactory
from risk.Player import Player
from risk.Territory import Territory



class DefaultGameSetup(object):
    '''
    classdocs
    '''
    
    
    def __init__(self):
        '''
        Constructor
        '''
    def getGoals(self):
        '''Territories'''
        alaska = Territory("Alaska")
        
        
        
        '''Goals'''
        goals = []
        
        goals.append(GoalFactory.createConquer())
        goals.append(GoalFactory.createOccupy())
        goals.append(GoalFactory.createEliminate(Player.COLOR_BLACK))
        goals.append(GoalFactory.createEliminate(Player.COLOR_BLUE))
        goals.append(GoalFactory.createEliminate(Player.COLOR_GRAY))
        goals.append(GoalFactory.createEliminate(Player.COLOR_GREEN))
        goals.append(GoalFactory.createEliminate(Player.COLOR_RED))
        goals.append(GoalFactory.createEliminate(Player.COLOR_YELLOW))
        
        
        return goals;