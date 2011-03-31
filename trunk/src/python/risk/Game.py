'''
Created on 2011 3 31

@author: cihancimen
'''
import random

class Game(object):
    '''
    classdocs
    '''

    #fixme players
    def __init__(self, continents, goals, cards):
        '''
        Constructor
        '''
        self.continents = {}
        self.territories = {}
        for continent in continents:
            self.continents[continent.name] = continent
            for territory in continent.territories:
                self.territories[territory.name] = territory
        self.goals = random.shuffle(goals)
        self.cards = random.shuffle(cards)
