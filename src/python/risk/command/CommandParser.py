'''
Created on 2011 4 1

@author: cihancimen
'''
from risk.command.ListCommand import ListCommand
from risk.command.PlaceCommand import PlaceCommand
from risk.command.MoveCommand import MoveCommand
from risk.command.AttackCommand import AttackCommand
from risk.command.TradeCommand import TradeCommand
from copy import copy
from risk.command.AbstractCommand import AbstractCommand

class CommandParser(object):
    '''
    classdocs
    '''
    '''Place <Territory> <ArmyNumber=1>'''
    COMMAND_PLACE = "place"
    '''Move <FromTerritory> <ToTerritory> <ArmyNumber>'''
    COMMAND_MOVE = "move"

    COMMAND_LIST = "list"
    '''Pass'''
    COMMAND_PASS = "pass"
    '''Attack <fromTerr> <toTerr> <dic number>'''
    COMMAND_ATTACK = "attack"
    '''Trade <first card number> <second card number> <third card number>'''
    COMMAND_TRADE = "trade"
    COMMAND_EXIT = "exit"
    COMMAND_MAP = "map"
    COMMAND_MAPIMG = "mapimg"
    AVAILABLE_COMMANDS = [COMMAND_PLACE, COMMAND_LIST, COMMAND_MOVE, COMMAND_PASS, COMMAND_ATTACK, COMMAND_TRADE, COMMAND_EXIT, COMMAND_MAP, COMMAND_MAPIMG]

    def __init__(self, game):
        '''
        Constructor
        '''
        self.game = game
    def parse(self, player, command_str):
        orig = copy(command_str)
        words = command_str.strip().split(" ")
      
        for i in range(len(words)):
            words[i] = words[i].strip()
        for i in range(len(words)):
            if(words[i] == ""):
                del words[i]
        if(len(words) < 1):
            raise ParseException('Enter something other than whitespaces\n')
        cmd = words[0].lower()
        if(not (cmd in CommandParser.AVAILABLE_COMMANDS)):
            raise ParseException('Unkown command: %s\n' % (cmd))
        
        if(cmd == CommandParser.COMMAND_PLACE):
            try:
                ter = self.game.territories[words[1]]
                if(len(words) > 2):
                    num = int(words[2])
                else:
                    num = 1
                return PlaceCommand(orig, ter, num)
            except KeyError as e:
                raise ParseException('Unknown Territory: %s\n' % (str(e)))
            except Exception as e:
                raise ParseException(str(e))
            
        elif(cmd == CommandParser.COMMAND_LIST):
            try:
                if(words[1] == "my"):
                    terrs = ""
                    i = 1
                    terrs += player.color + "\n"
                    for ter in self.game.territories.values():
                        if(ter.occupant == player):
                            terrs += str(i) + " " + ter.name + " - Army Number:" + str(ter.armies) + "\n"
                            i += 1
                    terrs += "Free Armies:" + str(player.armies)
                    return ListCommand(orig, terrs)
                elif(words[1] == "unoccupied"):
                    terrs = ""
                    for ter in self.game.territories.values():
                        if(not(ter.occupant)):
                            terrs += ter.name + "  "
                    return ListCommand(orig, terrs)
                elif(words[1] == "cards"):
                    cards = 'Cards(' + str(len(player.cards)) + '):\n'
                    for index, card in enumerate(player.cards):
                        cards += "\t" + str(index) + " - " + card.type + " " + (card.territory.name if(card.territory) else "") + "\n"
                    return ListCommand(orig, cards)
                elif(words[1] == 'neighbours'):
                    if(len(words) > 2):
                        try:
                            n = "Neighbours of " + words[2] + " :\n"
                            terr = self.game.territories[words[2]]
                            for ne in terr.neighbours:
                                n += "\t" + ne.name + "(" + ne.continent.name + " " + (ne.occupant.color if(ne.occupant) else 'unoccupied') + "- " + str(ne.armies) + " armies):\n"
                            return ListCommand(n)
                        except KeyError as e:
                            raise ParseException('Unknown Territory: %s\n' % (str(e)))
                        except Exception as ex:
                            raise ParseException(str(ex))  
                    else:
                        n = "Neighbours:\n"
                        for terr in player.occupied:
                            n += terr.name + "(" + terr.continent.name + "- " + str(terr.armies) + " armies):\n"
                            for ne in terr.neighbours:
                                if(not (ne.occupant == player)):
                                    n += "\t" + ne.name + "( " + ne.continent.name + " " + (ne.occupant.color if(ne.occupant) else 'unoccupied') + "- " + str(ne.armies) + " armies):\n"
                        return ListCommand(orig, n)
                elif(words[1] == 'all'):
                    all = "World State:\n"
                    for con in self.game.continents.values():
                        all += con.name + ":\n"
                        for terr in con.territories:
                            all += "\t" + terr.name + " " + (terr.occupant.color if(terr.occupant) else ' unoccupied ') + " " + str(terr.armies) + "\n"
                    return ListCommand(orig, all)
                elif(words[1] == 'mission'):
                    return ListCommand(orig, 'Your mission is: ' + player.mission.verbose)
                elif(words[1] == 'commands'):
                    commands = ""
                    commands += "----------\n"
                    commands += "list my                            :   list the player's territories, placed and free armies\n"
                    commands += "list unoccupied                    :   list the unoccupied territories\n"
                    commands += "list cards                         :   list the player's risk cards\n"
                    commands += "list mission                       :   shows the player's mission\n"
                    commands += "list neighbours                    :   list the player's occupied territories' neighbours\n"
                    commands += "list neighbours <territory>        :   list the given territory's neighbours\n"
                    commands += "list all                           :   list each continent and its territories with occupants\n"
                    commands += "----------\n"
                    commands += "place <territory> <army number>    :   place entered number of army in given territory\n"
                    commands += "----------\n"
                    commands += "move <from territory> <to territory> <army number>    :   move armies from one territory to another territory\n"
                    commands += "----------\n"
                    commands += "attack <from territory> <to territory> <dice number>    :   attack from one territory to another territory with entered number of dice\n"
                    commands += "----------\n"
                    commands += "trade <first card number> <second card number> <third card number>    :   trade in with given cards\n"
                    commands += "----------\n"
                    commands += "exit\n"
                    return ListCommand(orig, commands)
                else:
                    raise ParseException('Not Valid Command\n')
            except Exception as e:
                raise ParseException(str(e))
                
        elif(cmd == CommandParser.COMMAND_MOVE):
            try:
                if(len(words) != 4):
                    raise ParseException('Usage: Move <from territory name> <to territory name> <number of armies>\n')
                fromTerr = self.game.territories[words[1]]
                toTerr = self.game.territories[words[2]]
                num = int(words[3])
                return MoveCommand(orig, fromTerr, toTerr, num)
            except KeyError as e:
                raise ParseException('Unknown Territory: %s\n' % (str(e)))
            except Exception as e:
                raise ParseException(str(e))
        elif(cmd == CommandParser.COMMAND_ATTACK):
            try:
                if(len(words) != 4):
                    raise ParseException('Usage: Attack <from territory name> <to territory name> <number of dice>\n')
                fromTerr = self.game.territories[words[1]]
                toTerr = self.game.territories[words[2]]
                num = int(words[3])
                return AttackCommand(orig, fromTerr, toTerr, num)
            except KeyError as e:
                raise ParseException('Unknown Territory: %s\n' % (str(e)))
            except Exception as e:
                raise ParseException(str(e))
        elif(cmd == CommandParser.COMMAND_TRADE):
            try:
                if(len(words) != 4):
                    raise ParseException('Usage: Trade <first card number> <second card number> <third card number>\n')
                cardNum1 = int(words[1])
                if(cardNum1 > len(self.game.turner.player.cards) or cardNum1 < 0):
                    raise ParseException('First card number is not legal please enter between 0 and %s\n' %(len(self.game.turner.player.cards)))
                cardNum2 = int(words[2])
                if(cardNum2 > len(self.game.turner.player.cards) or cardNum2 < 0):
                    raise ParseException('Second card number is not legal please enter between 0 and %s\n' %(len(self.game.turner.player.cards)))
                cardNum3 = int(words[3])
                if(cardNum3 > len(self.game.turner.player.cards) or cardNum3 < 0):
                    raise ParseException('Third card number is not legal please enter between 0 and %s\n' %(len(self.game.turner.player.cards)))

                cards = []
                cards.append(self.game.turner.player.cards[cardNum1])
                cards.append(self.game.turner.player.cards[cardNum2])
                cards.append(self.game.turner.player.cards[cardNum3])
                return TradeCommand(orig, cards)
            except Exception as e:
                raise ParseException(str(e))
        elif(cmd == CommandParser.COMMAND_PASS):
            return PassCommand(orig)
        elif(cmd == CommandParser.COMMAND_EXIT):
            return ExitCommand(orig)
        elif(cmd == CommandParser.COMMAND_MAP):
            return MapCommand(orig, self.game.map)
        elif(cmd == CommandParser.COMMAND_MAPIMG):
            return MapCommand(orig, self.game.mapImage)
        else:
            raise ParseException('Unknown command: %s\n' % (cmd))


class PassCommand(AbstractCommand):
    def __init__(self, orig):
        AbstractCommand.__init__(self, orig)

class ExitCommand(AbstractCommand):
    def __init__(self, orig):
        AbstractCommand.__init__(self, orig)
        
class MapCommand(AbstractCommand):
    def __init__(self, orig, map):
        AbstractCommand.__init__(self, orig)
        if(map is None):
            self.map = 'No map'
        else:
            self.map = map
            
class MapImageCommand(AbstractCommand):
    def __init__(self, orig, mapImg):
        AbstractCommand.__init__(self, orig)
        if(mapImg is None):
            self.mapImg = 'No map'
        else:
            self.mapImg = mapImg

class ParseException(Exception):
    def __init__(self, message):
        Exception.__init__(self)
        self.mess = message
