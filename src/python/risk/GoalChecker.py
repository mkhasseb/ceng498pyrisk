'''
Created on 2011 4 1

@author: cihancimen
'''
from risk.Goal import Goal

class GoalChecker(object):
    '''
    classdocs
    '''


    def __init__(self, game):
        '''
        Constructor
        '''
        self.game = game
    def check(self):
        #if victor is found raise VictorFound exception
        for player in self.game.players:
            mission = player.mission
            self._checkPlayer(player, mission)
                        
        
        
    def _checkPlayer(self, player, mission):
        if(mission.type == Goal.TYPE_OCCUPY):
            if(mission.num <= len(player.occupied)):
                raise VictorFound(player)
        elif(mission.type == Goal.TYPE_CONTINENT):
            victor = True
            for con in mission.continents:
                victor = self._checkContinent(player, con)
            if(victor):
                raise VictorFound(player)
        elif(mission.type == Goal.TYPE_ELIMINATE):
            if(mission.color == player.color):
                mission = mission.alternate
                self._checkPlayer(player, mission)
            else:    
                victor = True
                for other in self.game.players:
                    if(other.color == mission.color):
                        victor = False
                        break
                if(victor):
                    raise VictorFound(player)
        elif(mission.type == Goal.TYPE_CONQUER):
            if(mission.num <= len(player.occupied)):
                victor = True
                for ter in player.occupied:
                    if(ter.armies < mission.armNum ):
                        victor = False
                        break
                if(victor):
                    raise VictorFound(player)
    def _checkContinent(self, player, continent):
        has = True
        for terr in continent.territories:
            if(terr.occupant != player):
                has = False
                break
        return has
        
class VictorFound(Exception):
    
    def __init__(self, victor):
        Exception.__init__(self)
        self.victor = victor
