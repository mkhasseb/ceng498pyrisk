'''
Created on 2011 3 31

@author: cihancimen
'''
import random

from risk.Card import Card
from risk.command.AttackCommand import AttackCommand
from risk.command.CommandParser import ParseException
from risk.command.CommandParser import PassCommand
from risk.command.ListCommand import ListCommand
from risk.command.MoveCommand import MoveCommand
from risk.command.PlaceCommand import PlaceCommand

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


    def __init__(self, color, connector):
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
        self.connector = connector
 
    def tradeIn(self, game):
        '''1 - getting armies according to territory number'''
        num = 0
        if (len(self.occupied) < 12):
            num = 3
        else:
            num = len(self.occupied) / 3
        self.connector.send('%s has %d territories and gets %s armies.' % (self.color, len(self.occupied), num))
        self.armies += num
       
        '''2 - getting armies according to occupied continent bonus'''
        for cont in game.continents.values():
            terNum = 0
            for ter in cont.territories:
                if (ter in self.occupied):
                    terNum += 1
                else:
                    break
            if (terNum == len(cont.territories)):
                self.connector.send('%s has %s continent and gets %s armies as continent bonus.' % (self.color, cont.name, cont.bonus))
                self.armies += cont.bonus

        '''3 - getting armies by trade cards'''
        if(len(self.cards) > 5):
            self.connector.send('%s has %d risk cards and must trade in.(Usage: Trade <first card number> <second card number> <third card number>)' % (self.color, len(self.cards)))
            done = False
            while(not done):
                try:
                    command = game.parser.parse(self.connector.receive())
                    if(isinstance(command, TradeCommand)):
                        cardTypes = []
                        for c in command.cards:
                            cardTypes.append(c.type)
                        if(_checkTradeIn(cardTypes)):
                            armyNum = _evaluateArmyNum(game)
                            game.gameSet += 1
                            self.connector.send('%s has traded in and get %s armies. Game set has increased to %s' % (self.color, armyNum, game.gameSet))
                            self.armies += armyNum
                            done = True

                            '''4 - getting armies by the territory behind traded cards'''
                            card = _checkTerrBehindCard(command.cards)
                            if(card):
                                self.connector.send('%s has %s territory in traded cards and get 2 extra armies.' % (self.color, card.territory.name))
                            for c in command.cards:
                                self.cards.remove(c)
                        else:
                            self.connector.send('Cards cannot be traded in, please enter card numbers correctly')
                    elif(isinstance(command, ListCommand)):
                        self.connector.send(command.verbose)
                    else:
                        self.connector.send('Command not allowed here')
                except ParseException as e:
                    self.connector.send(e.mess)

        elif(len(self.cards) >= 3):
            self.connector.send('%s has %d risk cards and may trade in or not.(Usage: Trade <first card number> <second card number> <third card number> | Pass)' % (self.color, len(self.cards)))
            done = False
            while(not done):
                try:
                    command = game.parser.parse(self.connector.receive())
                    if(isinstance(command, PassCommand)):
                        return
                    elif(isinstance(command, TradeCommand)):
                        cardTypes = []
                        for c in command.cards:
                            cardTypes.append(c.type)
                        if(_checkTradeIn(cardTypes)):
                            armyNum = _evaluateArmyNum(game)
                            game.gameSet += 1
                            self.connector.send('%s has traded in and get %s armies. Game set has increased to %s' % (self.color, armyNum, game.gameSet))
                            self.armies += armyNum
                            done = True

                            '''4 - getting armies by the territory behind traded cards'''
                            card = _checkTerrBehindCard(command.cards)
                            if(card):
                                self.connector.send('%s has %s territory in traded cards and get 2 extra armies.' % (self.color, card.territory.name))
                        else:
                            self.connector.send('Cards cannot be traded in, please enter card numbers correctly')
                    elif(isinstance(command, ListCommand)):
                        self.connector.send(command.verbose)
                    else:
                        self.connector.send('Command not allowed here')
                except ParseException as e:
                    self.connector.send(e.mess)
                    
    def placeIncome(self, game):
        self.connector.send('Turn of %s has %d free armies. Place them or pass (Usage: Place <territory name> <army number> | Pass)' % (self.color, self.armies))
        done = False
        while(not done):
            try:
                command = game.parser.parse(self.connector.receive())
                if(isinstance(command, PassCommand)):
                    return
                elif(isinstance(command, PlaceCommand)):
                    terr = command.territory
                    num = command.number
                    if (not (terr.occupant == self)):
                        self.connector.send('Territory %s occupied by %s' % (terr.name, terr.occupant.color))
                    elif (num > self.armies):
                        self.connector.send('%s only has %s armies' % (self.color, self.armies))
                    else:
                        terr.armies += num
                        self.armies -= num
                        if(self.armies == 0):
                            done = True
                        self.connector.send('Territory %s has %s armies by %s' % (terr.name, terr.armies, terr.occupant.color))

                elif(isinstance(command, ListCommand)):
                    self.connector.send(command.verbose)
                else:
                    self.connector.send('Command not allowed here')
            except ParseException as e:
                self.connector.send(e.mess)

    def placeSingle(self, game):
        self.connector.send('Turn of %s has %d armies. Place one army (Usage: Place <territory name>)' % (self.color, self.armies))
        done = False
        while(not done):
            try:
                command = game.parser.parse(self.connector.receive())
                if(isinstance(command, PlaceCommand)):
                    terr = command.territory
                    if(terr.occupant):
                        self.connector.send('Territory %s occupied by %s' % (terr.name, terr.occupant.color))
                    else:
                        terr.occupant = self
                        terr.armies += 1
                        self.armies -= 1
                        self.occupied.append(terr)
                        done = True
                        self.connector.send("%s occupied %s" % (terr.occupant.color, terr.name))

                elif(isinstance(command, ListCommand)):
                    self.connector.send(command.verbose)
                else:
                    self.connector.send('Command not allowed here')    
            except ParseException as e:
                self.connector.send(e.mess)
        
    def placeArmies(self, game):
        self.connector.send('Turn of %s has %d armies. Place remaining armies (Usage: Place <territory name> <army number>)' % (self.color, self.armies))
        done = False
        while(not done):
            try:
                command = game.parser.parse(self.connector.receive())
                if(isinstance(command, PlaceCommand)):
                    terr = command.territory
                    num = command.number
                    if (not (terr.occupant == self)):
                        self.connector.send('Territory %s occupied by %s' % (terr.name, terr.occupant.color))
                    elif (num > self.armies):
                        self.connector.send('%s only has %s armies' % (self.color, self.armies))
                    else:
                        terr.armies += num
                        self.armies -= num
                        if(self.armies == 0):
                            done = True
                        self.connector.send('Territory %s has %s armies by %s' % (terr.name, terr.armies, terr.occupant.color))
                        
                elif(isinstance(command, ListCommand)):
                    self.connector.send(command.verbose)
                else:
                    self.connector.send('Command not allowed here')
            except ParseException as e:
                self.connector.send(e.mess)

    def move(self, game):
        while(True):
            self.connector.send('Turn of %s. Move or Pass (Usage: Move <from territory> <to territory> <army number> | Pass)' % (self.color))
            try:
                command = game.parser.parse(self.connector.receive())
                if(isinstance(command, PassCommand)):
                    return
                elif(isinstance(command, MoveCommand)):
                    validity = self._isValidMove(command, game)
                    if(validity[0]):
                        command.fromTerr.armies -= command.num
                        command.toTerr.armies += command.num
                        self.connector.send('successful')
                        return
                    else:
                        self.connector.send("Invalid Move:" + validity[1])
                elif(isinstance(command, ListCommand)):
                    self.connector.send(command.verbose)
                else:
                    self.connector.send('Command not allowed here')
            except ParseException as e:
                self.connector.send(e.mess)
    def attack(self, game):
        occupied = False
        while(True):
            self.connector.send('Turn of %s. Attack or Pass (Usage: Attack <from territory> <to territory> <army number> | Pass)' % (self.color))
            try:
                command = game.parser.parse(self.connector.receive())
                if(isinstance(command, PassCommand)):
                    if(occupied):
                        self.connector.send('you conquered somewhere, draw a card...\nDrawed')
                        self.cards.append(game.cards.pop(0))
                    return
                elif(isinstance(command, AttackCommand)):
                    validity = self._isValidAttack(command) 
                    if(validity[0]):
                        self.connector.send('%s Attacking from %s to %s\'s %s with %d dice.' % (self.color, command.fromTerr.name, command.toTerr.occupant.color, command.toTerr.name, command.diceNum))
                        def_dice = command.toTerr.occupant.defend(command)
                        dice = command.diceNum
                        result = self._resolveAttack(dice, def_dice)
                        self.connector.send('Attacker rolls' + str(result[2]))
                        self.connector.send('Defender rolls' + str(result[3]))
                        command.fromTerr.armies -= result[0]
                        command.toTerr.armies -= result[1]
                        self.connector.send('Attacker lost %d, defender lost %d armies, now have %d - %d \n' % (result[0], result[1], command.fromTerr.armies, command.toTerr.armies))
                        if(command.toTerr.armies == 0):
                            occupied = True
                            self.connector.send('%s captured %s\n ' % (self.color, command.toTerr.name))
                            defender = command.toTerr.occupant
                            defender.occupied.remove(command.toTerr)
                            self.occupied.append(command.toTerr)
                            command.toTerr.occupant = self
                            self._checkElimination(self, defender, game)
                            self.connector.send('Please move armies in (enter single integer)')
                            
                            while(True):
                                try:
                                    move = int(self.connector.receive())
                                    if(not (move) > 0):
                                        self.connector.send('OMG Enter something bigger than zero')
                                    elif(move >= command.fromTerr.armies):
                                        self.connector.send('Not enough armies')
                                    else:
                                        command.fromTerr.armies -= move
                                        command.toTerr.armies += move 
                                        self.connector.send('Transfer complete: %d armies' % (move))
                                        break
                                except(Exception):
                                    self.connector.send('enter a valid integer')
                                
                    else:
                        self.connector.send("Invalid Attack: " + validity[1]) 
                elif(isinstance(command, ListCommand)):
                    self.connector.send(command.verbose)
                else:
                    self.connector.send('Command not allowed here')
            except ParseException as e:
                self.connector.send(e.mess)
        
    def defend(self, command):
        self.connector.send('%s is attacking your territory %s from %s with %d dice, you have %d armies at %s. \n Enter your dice number' % (command.fromTerr.occupant.color, command.toTerr.name, command.fromTerr.name, command.diceNum, command.toTerr.armies, command.toTerr.name))
        while(True):
            try:
                dice = int(self.connector.receive())
                if(dice > command.toTerr.armies or dice > 2):
                    self.connector.send('at most 2 or equal to territory army number')
                else:
                    return dice
            except(Exception):
                self.connector.send('enter 1 or 2')
    
    
    def _isValidMove(self, command, game):
        try:
            if(command.fromTerr.occupant != self or command.toTerr.occupant != self):
                return [False, 'Only move between your territories']
            elif(not self._pathExists(command.fromTerr, command.toTerr, game)):
                return [False, 'No valid path']
            elif(command.fromTerr.armies + 1 < command.num):
                return [False, 'Not enough armies']
            else:
                return [True]
        except Exception as e:
            return [False, str(e)]
    def _isValidAttack(self, command):
        try:
            if(command.fromTerr.occupant != self):
                return [False, 'It is not your territory']
            elif(command.toTerr.occupant == self):
                return [False, 'Can not attack your territory']
            elif(not (command.toTerr in command.fromTerr.neighbours)):
                return [False, 'Can only attack adjacent territory']
            elif(command.diceNum > 3 or command.diceNum < 1):
                return [False, 'Dice number must be 0 < dice number < 4']
            elif(command.fromTerr.armies <= command.diceNum):
                return [False, 'Not enough armies']
            else:
                return [True]
        except Exception as e:
            return [False, str(e)]
        
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
            atts.append(random.randint(1, 6))
        for i in range(dice_def):
            defs.append(random.randint(1, 6))
        atts.sort(reverse=True)
        defs.sort(reverse=True)
        for i in range(min(dice_att, dice_def)):
            if(atts[i] > defs[i]):
                def_lose += 1
            else:
                att_lose += 1
        return [att_lose, def_lose, atts, defs]

    def _checkElimination(self, attacker, defender, game):
        if(len(defender.occupied) == 0):
            self.connector.send('%s eliminated by %s')
            attacker.eliminates.append(defender.color)
            attacker.cards.extend(defender.cards)
            if(len(defender.cards) >= 6):
                self.connector.send('%s has taken %d risk cards of eliminated player and must trade in until 2, 3 or 4 cards remain.(Usage: Trade <first card number> <second card number> <third card number>)' % (attacker.color, len(defender.cards)))
                done = False
                while(not done):
                    try:
                        command = game.parser.parse(self.connector.receive())
                        if(isinstance(command, TradeCommand)):
                            cardTypes = []
                            for c in command.cards:
                                cardTypes.append(c.type)
                            if(_checkTradeIn(cardTypes)):
                                armyNum = _evaluateArmyNum(game)
                                game.gameSet += 1
                                self.connector.send('%s has traded in and get %s armies. Game set has increased to %s' % (attacker.color, armyNum, game.gameSet))
                                attacker.armies += armyNum
                                if(len(attacker.cards) <= 4):
                                    done = True

                                '''getting armies by the territory behind traded cards'''
                                card = _checkTerrBehindCard(command.cards)
                                if(card):
                                    self.connector.send('%s has %s territory in traded cards and get 2 extra armies.' % (self.color, card.territory.name))
                                for c in command.cards:
                                    attacker.cards.remove(c)
                            else:
                                self.connector.send('Cards cannot be traded in, please enter card numbers correctly')
                        elif(isinstance(command, ListCommand)):
                            self.connector.send(command.verbose)
                        else:
                            self.connector.send('Command not allowed here')
                    except ParseException as e:
                        self.connector.send(e.mess)
            game.players.remove(defender)
        
    def _checkTradeIn(self, cardTypes=None):
        types = [Card.TYPE_INFANTRY, Card.TYPE_CAVALRY, Card.TYPE_ARTILLERY]
        if(not cardTypes):
            cardTypes = self.cards
        if(Card.TYPE_WILD in cardTypes):
            return True
        else:
            for type in types:
                sameTypeNum = 0
                for ct in cardTypes:
                    if(type == ct):
                        sameTypeNum += 1
                if (sameTypeNum >= 3):
                    return True

            difTypeNum = 0
            for type in types:
                if(type in cardTypes):
                    difTypeNum += 1
                else:
                    break
            if(difTypeNum == 3):
                return True

        return False

    def _evaluateArmyNum(self, game):
        armyNum = 0
        if(game.gameSet < 6):
            armyNum = (game.gameSet + 1) * 2
        elif(game.gameSet >= 6):
            armyNum = ((game.gameSet - 6) * 5) + 15
        return armyNum

    def _checkTerrBehindCard(self, cards):
        for c in cards:
            if(c.territory in self.occupied):
                return c
        return None
