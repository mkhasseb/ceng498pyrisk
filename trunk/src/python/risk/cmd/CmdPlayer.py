'''
Created on 2011 4 1

@author: cihancimen
'''
from risk.Player import Player
from risk.command.CommandParser import ParseException, PassCommand
from risk.command.PlaceCommand import PlaceCommand
from risk.command.ListCommand import ListCommand
from risk.command.MoveCommand import MoveCommand
from risk.command.AttackCommand import AttackCommand

class CmdPlayer(Player):
    '''
    classdocs
    '''


    def __init__(self, color):
        '''
        Constructor
        '''
        Player.__init__(self, color);
        
    def placeSingle(self, game):
        print'Turn of %s have %d armies. Place one army (Usage: Place <territory name>)' % (self.color, self.armies)
        done = False
        while(not done):
            try:
                command = game.parser.parse(raw_input())
                if(isinstance(command, PlaceCommand)):
                    terr = command.territory
                    if(terr.occupant):
                        print 'Territory %s occupied by %s' % (terr.name, terr.occupant.color)
                    else:
                        terr.occupant = self
                        terr.armies += 1
                        self.armies -= 1
                        self.occupied.append(terr)
                        done = True
                        print "%s occupied %s" % (terr.occupant.color, terr.name)

                elif(isinstance(command, ListCommand)):
                    print command.verbose
                    
            except(ParseException):
                print 'Enter a proper command'
        
    def placeArmies(self, game):
        print 'Turn of %s have %d armies. Place remaining armies (Usage: Place <territory name> <army number>)' % (self.color, self.armies)
        done = False
        while(not done):
            try:
                command = game.parser.parse(raw_input())
                if(isinstance(command, PlaceCommand)):
                    terr = command.territory
                    num = command.number
                    if (not (terr.occupant == self)):
                        print 'Territory %s occupied by %s' % (terr.name, terr.occupant.color)
                    elif (num > self.armies):
                        print '%s only has %s armies' % (self.color, self.armies)
                    else:
                        terr.armies += num
                        self.armies -= num
                        if(self.armies == 0):
                            done = True
                        print 'Territory %s has %s armies by %s' % (terr.name, terr.armies, terr.occupant.color)
                        
                elif(isinstance(command, ListCommand)):
                    print command.verbose
            except(ParseException):
                print 'Enter a proper command'

    def move(self, game):
        while(True):
            print 'Turn of %s. Move or Pass (Usage: Move <from territory> <to territory> <army number> | Pass)' % (self.color)
            try:
                command = game.parser.parse(raw_input())
                if(isinstance(command, PassCommand)):
                    return
                elif(isinstance(command, MoveCommand)):
                    valid = self._isValidMove(command, game)
                    if(valid):
                        command.fromTerr.armies -= command.num
                        command.toTerr.armies += command.num
                        print 'successful'
                        return
                    else:
                        print 'invalid command'
                elif(isinstance(command, ListCommand)):
                    print command.verbose
            except(ParseException):
                print 'Enter proper command'
    def attack(self, game):
        occupied = False
        while(True):
            print 'Turn of %s. Attack or Pass (Usage: Attack <from territory> <to territory> <army number> | Pass)' % (self.color)
            try:
                command = game.parser.parse(raw_input())
                if(isinstance(command, PassCommand)):
                    if(occupied):
                        print 'you conquered somewhere, draw a card...\nDrawed'
                        self.cards.append(game.cards.pop())
                    return
                elif(isinstance(command, AttackCommand)):
                    if(self._isValidAttack(command)):
                        print '%s Attacking from %s to %s\'s %s with %d dice.' % (self.color, command.fromTerr.name, command.toTerr.occupant.color, command.toTerr.name, command.diceNum)
                        def_dice = command.toTerr.occupant.defend(command)
                        dice = command.diceNum
                        result = self._resolveAttack(dice, def_dice)
                        print 'Attacker rolls', result[2]
                        print 'Defender rolls', result[3]
                        command.fromTerr.armies -= result[0]
                        command.toTerr.armies -= result[1]
                        print 'Attacker lost %d, defender lost %d armies, now have %d - %d \n' % (result[0], result[1],command.fromTerr.armies, command.toTerr.armies )
                        if(command.toTerr.armies == 0):
                            occupied = True
                            print '%s captured %s\n ' % (self.color, command.toTerr.name)
                            defender = command.toTerr.occupant
                            defender.occupied.remove(command.toTerr)
                            self.occupied.append(command.toTerr)
                            command.toTerr.occupant = self
                            self._checkElimination(self, defender, game)
                            print 'Please move armies in (enter single integer)'
                            
                            while(True):
                                try:
                                    move = int(raw_input())
                                    if(not (move)> 0 ):
                                        print 'OMG Enter something bigger than zero'
                                    elif(move >= command.fromTerr.armies):
                                        print 'Not enough armies'
                                    else:
                                        command.fromTerr.armies -= move
                                        command.toTerr.armies += move 
                                        print 'Transfer complete: %d armies' % (move)
                                        break
                                except(Exception):
                                    print 'enter a valid integer'
                                
                    else:
                        print 'invalid command' 
                elif(isinstance(command, ListCommand)):
                    print command.verbose
            except(ParseException):
                print 'invalid command'
        
    def defend(self, command):
        print '%s is attacking your territory %s from %s with %d dice, you have %d armies at %s. \n Enter your dice number' % (command.fromTerr.occupant.color, command.toTerr.name, command.fromTerr.name, command.diceNum, command.toTerr.armies, command.toTerr.name)
        while(True):
            try:
                dice = int(raw_input())
                if(dice > command.toTerr.armies):
                    print 'print at most 2 or equal to territory\' army number'
                else:
                    return dice
            except(Exception):
                print 'enter 1 or 2'
        
                
        