'''
Created on 2011 4 1

@author: cihancimen
'''
from risk.command.ListCommand import ListCommand
from risk.command.PlaceCommand import PlaceCommand
from risk.command.MoveCommand import MoveCommand
from risk.command.AttackCommand import AttackCommand

class CommandParser(object):
    '''
    classdocs
    '''
    '''Place <Territory> <ArmyNumber=1>'''
    COMMAND_PLACE = "place"
    '''Move <FromTerritory> <ToTerritory> <ArmyNumber>'''
    COMMAND_MOVE = "move"
    '''List (myterritories|unoccupied)'''
    COMMAND_LIST = "list"
    '''Pass'''
    COMMAND_PASS = "pass"
    '''Attack <fromTerr> <toTerr> <dic number>'''
    COMMAND_ATTACK = "attack"
    AVAILABLE_COMMANDS = [COMMAND_PLACE, COMMAND_LIST, COMMAND_MOVE, COMMAND_PASS, COMMAND_ATTACK]

    def __init__(self, game):
        '''
        Constructor
        '''
        self.game = game
    def parse(self, command_str):
        words = command_str.strip().split(" ")
      
        for i in range(len(words)):
            words[i] = words[i].strip()
        for i in range(len(words)):
            if(words[i] == ""):
                del words[i]
        if(len(words) < 1):
            raise ParseException()
        cmd = words[0].lower()
        if(not (cmd in CommandParser.AVAILABLE_COMMANDS)):
            raise ParseException()
        
        if(cmd == CommandParser.COMMAND_PLACE):
            try:
                ter = self.game.territories[words[1]]
                if(len(words) > 2):
                    num = int(words[2])
                else:
                    num = 1
                return PlaceCommand(ter, num)
            except(Exception):
                raise ParseException()
            
        elif(cmd == CommandParser.COMMAND_LIST):
            try:
                if(words[1] == "myterritories"):
                    terrs = ""
                    i = 1
                    terrs += self.game.turner.player.color + "\n"
                    for ter in self.game.territories.values():
                        if(ter.occupant == self.game.turner.player):
                            terrs += str(i) + " " + ter.name + " - Army Number:" + str(ter.armies) + "\n"
                            i += 1
                    return ListCommand(terrs)
                elif(words[1] == "unoccupied"):
                    terrs = ""
                    for ter in self.game.territories.values():
                        if(not(ter.occupant)):
                            terrs += ter.name + "  "
                    return ListCommand(terrs)
                elif(words[1] == "cards"):
                    cards = 'Cards('+str(len(self.game.turner.player.cards))+'):\n'
                    for index,card in enumerate(self.game.turner.player.cards):
                        cards += "\t" + str(index) +" - "+card.type +" "+ (card.territory.name if(card.territory) else "" )  + "\n"
                    return ListCommand(cards)
                elif(words[1] == 'neighbours'):
                    if(len(words) > 2):
                        try:
                            n = "Neighbours of "+words[2]+" :\n"
                            terr  = self.game.territories[words[2]]
                            for ne in terr.neighbours:
                                n += "\t" + ne.name +"(" + ne.continent.name +" "+   (ne.occupant.color if(ne.occupant) else 'unoccupied') +"- " + str(ne.armies) +" armies):\n"
                            return ListCommand(n)
                        except Exception as ex:
                            print ex
                            raise ParseException()  
                    else:
                        player= self.game.turner.player
                        n = "Neighbours:\n"
                        for terr in player.occupied:
                            n += terr.name +"(" + terr.continent.name +"- " + str(terr.armies) +" armies):\n"
                            for ne in terr.neighbours:
                                if(not (ne.occupant == player)):
                                    n += "\t" + ne.name +"( " + ne.continent.name +" "+  (ne.occupant.color if(ne.occupant) else 'unoccupied') +"- " + str(ne.armies) +" armies):\n"
                        return ListCommand(n)
                elif(words[1] == 'all'):
                    all ="World State:\n"
                    for con in self.game.continents.values():
                        all += con.name +":\n"
                        for terr in con.territories:
                            all +="\t" + terr.name + " " + (terr.occupant.color if(terr.occupant) else ' unoccupied ') + " " + str(terr.armies) +"\n"
                    return ListCommand(all)
                elif(words[1] == 'mission'):
                    return ListCommand(self.game.turner.player.mission.verbose)
            except Exception as ex:
                print ex
                raise ParseException()
                
        elif(cmd == CommandParser.COMMAND_MOVE):
            try:
                if(len(words) != 4):
                    #incorrect usage
                    raise ParseException()
                fromTerr = self.game.territories[words[1]]
                toTerr = self.game.territories[words[2]]
                num = int(words[3])
                return MoveCommand(fromTerr, toTerr, num)
            except(Exception):
                raise ParseException()
        elif(cmd == CommandParser.COMMAND_ATTACK):
            try:
                if(len(words) != 4):
                    #incorrect usage
                    raise ParseException()
                fromTerr = self.game.territories[words[1]]
                toTerr = self.game.territories[words[2]]
                num = int(words[3])
                return AttackCommand(fromTerr, toTerr, num)
            except(Exception):
                raise ParseException()
        elif(cmd == CommandParser.COMMAND_PASS):
            return PassCommand()
        else:
            raise ParseException()

        '''elif(cmd == CommandParser.COMMAND_MOVE):
            try:
                num = int(words[1])
                fromTer = self.game.territories[words[3].strip()]
                toTer = self.game.territories[words[5].strip()]'''

class PassCommand(object):
    def __init__(self):
        pass

class ParseException(Exception):
    def __init__(self):
        Exception.__init__(self)
