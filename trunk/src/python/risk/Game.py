'''
Created on 2011 3 31

@author: cihancimen
'''
import random
from risk.command.CommandParser import CommandParser
from risk.GoalChecker import VictorFound, GoalChecker

class Game(object):
    '''
    classdocs
    '''

    #fixme players
    def __init__(self, continents, goals, cards, players):
        '''
        Constructor
        '''
        self.goalChecker = GoalChecker(self)
        self.parser = CommandParser(self)
        self.continents = {}
        self.territories = {}
        for continent in continents:
            self.continents[continent.name] = continent
            for territory in continent.territories:
                self.territories[territory.name] = territory
        self.goals = goals
        self.cards = cards
        self.players = players
        random.shuffle(self.goals)
        random.shuffle(self.cards)
        random.shuffle(self.players)
        self.turner= TurnIterator(players)
        for player in players:
            player.game = self
    def setup(self):
        num_armies = 40 - (len(self.players) -2) * 5
        while(not self.turner.roundCompleted()):
            player =self.turner.next()
            player.armies = num_armies
            player.mission = self.goals.pop()
            print 'current player %s' % (player.color)
        self.turner.reset()
        while(self.__countUnoccupied()> 0):
            player = self.turner.next()
            player.placeSingle(self)
        self.turner.reset()
        while(not self.turner.roundCompleted()):
            self.turner.next().placeArmies(self)
        self.turner.reset()
    def play(self):
        self.turner.reset()
        victor = None
        try:
            while(True):
                while(not self.turner.roundCompleted()):
                    player = self.turner.next()
                    player.placeIncome(self)
                    self.goalChecker.check()
                    player.tradeId(self)
                    self.goalChecker.check()
                    player.attack(self)
                    self.goalChecker.check()
                    player.move(self)
                    self.goalChecker.check()
                self.turner.reset()
        except(VictorFound):
            return victor
            
    def __countUnoccupied(self):
        i = 0;
        for ter in self.territories.values():
            if(not ter.occupant):
                i += 1
        return i
    
#FIXME what happens if someone eliminated
class TurnIterator(object):
    def __init__(self, players):
        self.index = 0
        self.turncount = 0;
        self.players = players
        self.roundFlag = False;
        self.completed = False;
    def next(self):
        self.player = self.players[self.index]
        self.index += 1
        self.turncount  +=1
        if(self.index == len(self.players)):
            if(self.roundFlag):
                self.completed = True
            self.index = 0
        return self.player
    
    def reset(self):
        self.index = 0
        self.turncount = 0
        self.roundFlag = False;
        self.completed = False;
        
    def roundCompleted(self):
        if(not self.roundFlag):
            self.roundFlag = True
        if(self.completed):
            self.completed = False
            self.roundFlag = False
            return True    
        
