'''
Created on 2011 3 31

@author: cihancimen
'''
from risk.connector.CmdConnector import CmdConnector
import random
from risk.command.CommandParser import CommandParser
from risk.GoalChecker import VictorFound, GoalChecker
import sys
from threading import Thread, Lock, Semaphore
import time

class Game(Thread):
    '''
    classdocs
    '''

    def __init__(self, continents, goals, cards, players, map=None, mapImage=None):
        '''
        Constructor
        '''
        Thread.__init__(self)
        self.victorFound = False
        self.victor = None
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
        self.turner = TurnIterator(players)
        for player in players:
            player.set_game(self)
        self.gameSet = 1
        self.ended= False
        self.map = map
        self.mapImage= mapImage
#        self.locks = {}
#        for pl in self.players:
#            self.locks[pl] = Semaphore(0) 
    def setup(self):
        num_armies = 40 - (len(self.players) - 2) * 5
        while(not self.turner.roundCompleted()):
            player = self.turner.next()
            player.armies = num_armies
            player.mission = self.goals.pop()
            print 'current player %s' % (player.color)
        self.turner.reset()
        while(self.__countUnoccupied() > 0):
            player = self.turner.next()
            player.placeSingle(self)
        self.turner.reset()
        while(not self.turner.roundCompleted()):
            self.turner.next().placeArmies(self)
        self.turner.reset()
    def run(self):
        time.sleep(3)
        self.setup()
        self.turner.reset()
        victor = None
        try:
            while(not self.victorFound):
                while(not self.turner.roundCompleted() and (not self.victorFound)):
                    player = self.turner.next()
                    player.tradeIn(self)
                    self.goalChecker.check()
                    player.placeIncome(self)
                    self.goalChecker.check()
                    player.attack(self)
                    self.goalChecker.check()
                    player.move(self)
                    self.goalChecker.check()
                self.turner.reset()
        except VictorFound as e:
            self.ended = True
            self.victor = e.victor
            self.broadcast('Victor found: %s with mission %s' % (self.victor.color, self.victor.mission.verbose))
    def __countUnoccupied(self):
        i = 0;
        for ter in self.territories.values():
            if(not ter.occupant):
                i += 1
        return i
    
    def broadcast(self, message):
        if(isinstance(self.turner.player.connector, CmdConnector)):
            self.turner.player.connector.send(message)
        else:
            for p in self.players:
                try:
                    p.connector.send(message)
                except Exception as e:
                    print 'exception at send message '
                    print e
    def exit(self):
        self.broadcast("Game is ending...")
#        for player in self.players:
#            try:
#                player.connector.close()
#            except Exception as e:
#                print 'exception at closing a connector '
#                print e
        self.ended = True
        

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
        self.turncount += 1
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
    