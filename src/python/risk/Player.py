'''
Created on 2011 3 31

@author: cihancimen
'''
from risk.command import MoveCommand
from compiler.pycodegen import EXCEPT
import random

class Player(object):
    '''
    classdocs
    '''
    COLOR_RED = "Red"
    COLOR_BLUE = "Blue"
    COLOR_GREEN = "Green"
    COLOR_GRAY = "Gray"
    COLOR_BLACK = "Black"
    COLOR_YELLOW = "Yellow"


    def __init__(self, color):
        '''
        Constructor
        '''
        self.color = color
        self.game = None
        self.armies = 0
        self.mission = None
        self.occupied = []
        self.eliminates = []
        self.cards = []
    def placeSingle(self, game):
        print "I am %s have %d armies. I am placing one" % (self.color, self.armies)
        
    def placeArmies(self, game):
        print "I am %s have %d armies. I am placing arbitrary" % (self.color, self.armies) 
        pass
    #TODO implement here
    def placeIncome(self, game):
        pass
    def tradeIn(self, game):
        pass
    def attack(self, game):
        pass
    def move(self, game):
        pass
    def defend(self, command):
        pass
    
    def _isValidMove(self, command, game):
        try:
            if(not self._pathExists(command.fromTerr, command.toTerr, game)):
                return False
            elif(command.fromTerr.armies + 1 < command.num):
                return False
            else:
                return True
        except Exception as e:
            print e
            return False;
    def _isValidAttack(self, command):
        try:
            if(command.fromTerr.occupant != self ):
                return False
            elif(command.toTerr.occupant == self):
                return False
            elif(not (command.toTerr in command.fromTerr.neighbours)):
                return False
            elif(command.diceNum > 3 or command.diceNum < 1):
                return False
            elif(command.fromTerr.armies <= command.diceNum):
                return False
            else:
                return True
        except(Exception):
            return False;
        
    def _pathExists(self, fromTerr, toTerr, game):
        observed = self._getSelfNeighbours(fromTerr)
        for terr in observed:
            if(toTerr in observed):
                return True;
            for nt in self._getSelfNeighbours(terr):
                if(not(nt in observed)):
                    observed.append(nt)
        else:
            return False;
        
    def _getSelfNeighbours(self, terr):
        n = []
        for ne in terr.neighbours:
            if(ne.occupant == self):
                n.append(ne)
        return n
    
    def _resolveAttack(self, dice_att, dice_def):
        atts = []
        defs = []
        att_lose = 0
        def_lose = 0
        for i in range(dice_att):
            atts.append(random.randint(1,6))
        for i in range(dice_def):
            defs.append(random.randint(1,6))
        atts.sort(reverse=True)
        defs.sort(reverse=True)
        for i in range(min(dice_att, dice_def)):
            if(atts[i] > defs[i]):
                def_lose +=1
            else:
                att_lose +=1
        return [att_lose, def_lose, atts, defs]

    def _checkElimination(self, attacker,defender, game):
        if(len(defender.occupied) == 0):
            print '%s eliminated by %s'
            attacker.eliminates.append(defender.color)
            attacker.cards.extend(defender.cards)
            #FIXME handle card limit here
            game.players.remove(defender)
        
