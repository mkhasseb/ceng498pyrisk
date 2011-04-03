'''
Created on 2011 3 31

@author: cihancimen
'''
import random
from risk.command.PlaceCommand import PlaceCommand
from risk.command.ListCommand import ListCommand
from risk.command.CommandParser import ParseException, PassCommand
from risk.command.AttackCommand import AttackCommand
from risk.command.MoveCommand import MoveCommand

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
        pass
    def placeIncome(self, game):
        pass
    def placeSingle(self, game):
        self.connector.send('Turn of %s have %d armies. Place one army (Usage: Place <territory name>)' % (self.color, self.armies))
        done = False
        while(not done):
            try:
                command = game.parser.parse(self.connector.receive())
                if(isinstance(command, PlaceCommand)):
                    terr = command.territory
                    if(terr.occupant):
                        self.connector.send( 'Territory %s occupied by %s' % (terr.name, terr.occupant.color))
                    else:
                        terr.occupant = self
                        terr.armies += 1
                        self.armies -= 1
                        self.occupied.append(terr)
                        done = True
                        self.connector.send( "%s occupied %s" % (terr.occupant.color, terr.name))

                elif(isinstance(command, ListCommand)):
                    self.connector.send( command.verbose)
                else:
                    self.connector.send('Command not allowed here')    
            except ParseException as e:
                self.connector.send( e.mess)
        
    def placeArmies(self, game):
        self.connector.send( 'Turn of %s have %d armies. Place remaining armies (Usage: Place <territory name> <army number>)' % (self.color, self.armies))
        done = False
        while(not done):
            try:
                command = game.parser.parse(self.connector.receive())
                if(isinstance(command, PlaceCommand)):
                    terr = command.territory
                    num = command.number
                    if (not (terr.occupant == self)):
                        self.connector.send( 'Territory %s occupied by %s' % (terr.name, terr.occupant.color))
                    elif (num > self.armies):
                        self.connector.send( '%s only has %s armies' % (self.color, self.armies))
                    else:
                        terr.armies += num
                        self.armies -= num
                        if(self.armies == 0):
                            done = True
                        self.connector.send( 'Territory %s has %s armies by %s' % (terr.name, terr.armies, terr.occupant.color))
                        
                elif(isinstance(command, ListCommand)):
                    self.connector.send( command.verbose)
                else:
                    self.connector.send('Command not allowed here')
            except ParseException as e:
                self.connector.send(e.mess)

    def move(self, game):
        while(True):
            self.connector.send( 'Turn of %s. Move or Pass (Usage: Move <from territory> <to territory> <army number> | Pass)' % (self.color))
            try:
                command = game.parser.parse(self.connector.receive())
                if(isinstance(command, PassCommand)):
                    return
                elif(isinstance(command, MoveCommand)):
                    validity = self._isValidMove(command, game)
                    if(validity[0]):
                        command.fromTerr.armies -= command.num
                        command.toTerr.armies += command.num
                        self.connector.send( 'successful')
                        return
                    else:
                        self.connector.send("Invalid Move:" + validity[1])
                elif(isinstance(command, ListCommand)):
                    self.connector.send( command.verbose)
                else:
                    self.connector.send('Command not allowed here')
            except ParseException as e:
                self.connector.send(e.mess)
    def attack(self, game):
        occupied = False
        while(True):
            self.connector.send( 'Turn of %s. Attack or Pass (Usage: Attack <from territory> <to territory> <army number> | Pass)' % (self.color))
            try:
                command = game.parser.parse(self.connector.receive())
                if(isinstance(command, PassCommand)):
                    if(occupied):
                        self.connector.send( 'you conquered somewhere, draw a card...\nDrawed')
                        self.cards.append(game.cards.pop())
                    return
                elif(isinstance(command, AttackCommand)):
                    validity =self._isValidAttack(command) 
                    if(validity[0]):
                        self.connector.send( '%s Attacking from %s to %s\'s %s with %d dice.' % (self.color, command.fromTerr.name, command.toTerr.occupant.color, command.toTerr.name, command.diceNum))
                        def_dice = command.toTerr.occupant.defend(command)
                        dice = command.diceNum
                        result = self._resolveAttack(dice, def_dice)
                        self.connector.send( 'Attacker rolls' +  str(result[2]))
                        self.connector.send( 'Defender rolls'+ str(result[3]))
                        command.fromTerr.armies -= result[0]
                        command.toTerr.armies -= result[1]
                        self.connector.send( 'Attacker lost %d, defender lost %d armies, now have %d - %d \n' % (result[0], result[1],command.fromTerr.armies, command.toTerr.armies ))
                        if(command.toTerr.armies == 0):
                            occupied = True
                            self.connector.send( '%s captured %s\n ' % (self.color, command.toTerr.name))
                            defender = command.toTerr.occupant
                            defender.occupied.remove(command.toTerr)
                            self.occupied.append(command.toTerr)
                            command.toTerr.occupant = self
                            self._checkElimination(self, defender, game)
                            self.connector.send( 'Please move armies in (enter single integer)')
                            
                            while(True):
                                try:
                                    move = int(self.connector.receive())
                                    if(not (move)> 0 ):
                                        self.connector.send( 'OMG Enter something bigger than zero')
                                    elif(move >= command.fromTerr.armies):
                                        self.connector.send( 'Not enough armies')
                                    else:
                                        command.fromTerr.armies -= move
                                        command.toTerr.armies += move 
                                        self.connector.send( 'Transfer complete: %d armies' % (move))
                                        break
                                except(Exception):
                                    self.connector.send( 'enter a valid integer')
                                
                    else:
                        self.connector.send("Invalid Attack: " + validity[1]) 
                elif(isinstance(command, ListCommand)):
                    self.connector.send( command.verbose)
                else:
                    self.connector.send('Command not allowed here')
            except ParseException as e:
                self.connector.send( e.mess)
        
    def defend(self, command):
        self.connector.send( '%s is attacking your territory %s from %s with %d dice, you have %d armies at %s. \n Enter your dice number' % (command.fromTerr.occupant.color, command.toTerr.name, command.fromTerr.name, command.diceNum, command.toTerr.armies, command.toTerr.name))
        while(True):
            try:
                dice = int(self.connector.receive())
                if(dice > command.toTerr.armies or dice > 2):
                    self.connector.send( 'self.connector.send( at most 2 or equal to territory\' army number')
                else:
                    return dice
            except(Exception):
                self.connector.send( 'enter 1 or 2')
    
    
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
            return [False , str(e)]
    def _isValidAttack(self, command):
        try:
            if(command.fromTerr.occupant != self ):
                return [False, 'It is not your territory']
            elif(command.toTerr.occupant == self):
                return [False, 'Can not attack your territory']
            elif(not (command.toTerr in command.fromTerr.neighbours)):
                return [False, 'Can only attack adjacent territory']
            elif(command.diceNum > 3 or command.diceNum < 1):
                return [False, 'Dice number must be 0 < dice number < 4' ]
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
            self.connector.send( '%s eliminated by %s')
            attacker.eliminates.append(defender.color)
            attacker.cards.extend(defender.cards)
            #FIXME handle card limit here
            game.players.remove(defender)
        
