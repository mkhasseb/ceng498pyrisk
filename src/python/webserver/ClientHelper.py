# To change this template, choose Tools | Templates
# and open the template in the editor.
from threading import Thread


__author__="ozgur"
__date__ ="$May 6, 2011 12:25:30 AM$"

import socket
S_MOVE = 'moveorpass'
S_MOVE_0 = 'move0'
S_MOVE_1 = 'move1'
S_MOVE_2 = 'move2'
S_TRANSFER = 'transferarmies'
S_ATTACK = 'attack'
S_ATTACK_0 = "attack0"
S_ATTACK_1 = "attack1"
S_ATTACK_2 = "attack2"
S_DEFEND = 'defend'
S_PLACE_SINGLE = "placeSingle"
S_PLACE_ARMIES = "placeArmies"
S_PLACE_INCOME = "placeIncome"
S_ROAM = "roam"
S_TRADE = 'trade'
S_TRADE_MUST = 'trade_must'

class ClientHelper(Thread):
    def __init__(self, host, port):
        Thread.__init__(self)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((host, port))
        self.mapSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.mapSocket.connect((host, port + 1))
        self.end = False
        self.currentState = S_ROAM
        self.currentMapState = 'None'
        self.map = ''
        self.mapImage = ''
        self.logstr = ""
        self.worldMap = ''
        
    def run(self):
        while(not self.end):
            if self.currentMapState == 'Map':
                self.map  = ''
#                print self.socket.recv(10000)
                while True:
                    self.log("Waiting for map content")
                    part = self.mapSocket.recv(10000)
                    if  "EOF" in part:
                        self.map += part.split("EOF")[0]
                        break
                    self.map += part
                
                self.log("Retrieved map content")
                self.mapSocket.send("mapImg")
                self.mapImage  = ""
                while True:
                    self.log("Waiting for map image content")
                    part = self.mapSocket.recv(10000)
                    print part
                    if  "EOF" in part:
                        self.mapImage += part.split("EOF")[0]
                        break
                    self.mapImage += part
                #self.handle.mapImgSig()
                self.currentMapState = 'None'
                self.log("Retrieved map image")
                
#                self.mapSocket.close()
            self.log("Waiting")
            #self.handle.setStateLabel()
            str = self.socket.recv(10000)
            self.log(str + ' : ' + self.currentState)
            
            str = str.strip()
            self.log('message: ' +str)
                
            if(str == ""):
                continue
            if 'Game starting...' in str:
                    self.log("Game is starting retrieving map")
                    self.currentMapState = 'Map'
                    print 'map is requested'
                    self.mapSocket.send("map")
            if 'World State' in str:
                pass
                self.updateWorldMap(str)
            if 'Cards' in str:
                pass
                #self.handle.updateCardList(str)
            if 'you conquered somewhere, draw a card' in str:
                self.refreshCards()
                
            if 'Welcome' in str:
                pass
                #self.handle.setPlayerName(str.split(' ')[2][:-1])
            if 'Your mission is:' in str:
                pass
                #self.handle.setMission(str.split('Your mission is:')[1].split(".")[0])
            if 'Victor found:' in str:
                pass
                #self.handle.victorFound(str.split('Victor found:')[1].split('.')[0])
                
#           available
            if(self.currentState == S_ROAM):
                if 'Usage: Place' in str:
                    if 'Pass' in str:
                        #self.handle.placeOrPass()
                        self.updateState(S_PLACE_INCOME, None)
                        continue
                    elif 'Usage: Place <territory name> <army number>' in str:
                        #self.handle.placeArmy()
                        self.updateState(S_PLACE_ARMIES, None)
                        continue
                    elif 'Usage: Place <territory name>' in str:
                        #self.handle.placeSingle()
                        self.updateState(S_PLACE_SINGLE, None)
                        self.send('list mission')
                        continue
                elif 'Usage: Attack' in str:
                    #self.handle.attackOrPass()
                    self.updateState(S_ATTACK, None)
                elif 'Usage: Move <from territory> <to territory> <army number> | Pass' in str:
                    self.updateState(S_MOVE, S_MOVE)
                    #self.handle.moveOrPass()
                elif 'Usage: Trade' in str and 'must trade' in str:
                    self.updateState(S_TRADE_MUST, S_TRADE_MUST)
                    #self.handle.tradeOrPass()
                elif 'Usage: Trade' in str:
                    self.updateState(S_TRADE, S_TRADE)
                    #self.handle.tradeOrPass()
                elif 'Enter your dice number' in str:
                    self.updateState(S_DEFEND, None)
                    #self.handle.defend(str.split('\n')[0].split(' ')[-2][:-1])
                    #self.defend(dice)
                elif (not ("World State" in str)) and (not ('Welcome' in str)):
                    self.refresh()
                    continue

            if(self.currentState == S_PLACE_SINGLE):
                if ('World State' in str):
                    continue
                elif('occupied' in str and not 'Territory' in str):
                    self.refresh()
                    self.updateState(S_ROAM, S_ROAM)
            if(self.currentState == S_PLACE_ARMIES):
                if('armies in territory' in str):
                    self.refresh()
                elif('You completed army placement' in str):
                    self.updateState(S_ROAM, S_ROAM)
            if(self.currentState == S_PLACE_INCOME):
                if('armies in territory' in str):
                    self.refresh()
                elif('You completed income placement' in str):
                    self.updateState(S_ROAM, S_ATTACK)
                    #self.handle.attackOrPass()
                    self.updateState(S_ATTACK, None)
            if(self.currentState == S_ATTACK):
                if 'Invalid Attack' in str:
                    self.updateState(S_ATTACK, S_ATTACK_0)
                elif 'captured' in str:
                    self.updateState(S_TRANSFER, S_TRANSFER)
                    #self.handle.transfer()
                elif 'Attacker lost' in str:
                    self.updateState(S_ATTACK, S_ATTACK_0)
                    self.refresh()
                    #self.handle.attackOrPass()
            if(self.currentState == S_TRANSFER):
                if 'Invalid Transfer:' in str:
                    self.updateState(S_TRANSFER, S_TRANSFER)
                    #self.handle.transfer()
                elif 'Transfer complete:' in str:
                    self.updateState(S_ROAM, S_ROAM)
                    self.refresh()
            if(self.currentState == S_DEFEND):
                if 'defended with' in str:
                    self.updateState(S_ROAM, S_ROAM)
                    self.refresh()
                elif 'at most 2 or equal to territory army number' in str or 'enter 1 or 2' in str:
                    self.updateState(S_DEFEND, None)
                    #self.handle.defend()
            if(self.currentState == S_MOVE):
                if 'Successful' in str:
                    self.updateState(S_ROAM, S_ROAM)
                elif 'Invalid Move:' in str:
                    #self.handle.moveOrPass()
                    pass
            if(self.currentState == S_TRADE):
                if 'has traded in and get' in str:
                    self.updateState(S_ROAM, S_ROAM)
                    self.refreshCards()
                elif 'Cards cannot be traded in' in str:
                    pass
                    #self.handle.tradeOrPass()
            if(self.currentState == S_TRADE_MUST):
                if 'has traded in and get' in str:
                    self.updateState(S_ROAM, S_ROAM)
                    self.refreshCards()
                elif 'Cards cannot be traded in' in str:
                    self.updateState(S_TRADE_MUST, S_TRADE_MUST)
                    #self.handle.tradeOrPass()

#*********************************************************************************

                    #self.defend(dice)
#            elif 'Usage: Place' in str:
#                if 'Pass' in str:
#                    self.handle.placeOrPass()
#                    self.currentState = 'PlaceOrPass'
#                    self.send("list all")
#                    continue
#                elif 'Usage: Place <territory name> <army number>' in str:
#                    self.handle.placeArmy()
#                    self.currentState = 'Place'
#                    self.send("list all")
#                    continue
#                elif 'Usage: Place <territory name>' in str:
#                    self.handle.placeSingle()
#                    self.currentState = 'PlaceSingle'
#                    self.send("list all")
#                    continue
#            elif 'Usage: Trade' in str:
#                if 'Pass' in str:
#                    #sendGUI(TradeOrPass)
#                    self.currentState = 'TradeOrPass'
#                    self.send("list all")
#                    continue
#                else:
#                    #sendGUI(MustTrade)
#                    self.currentState = 'MustTrade'
#                    self.send("list all")
#                    continue
#            elif 'Usage: Move' in str:
#                #sendGUI(MoveOrPass)
#                self.currentState = 'MoveOrPass'
#                self.send("list all")
#                continue
#            elif 'Usage: Attack' in str:
#                #sendGUI(AttackOrPass)
#                self.currentState = 'AttackOrPass'
#                self.send("list all")
#                continue
#            elif 'Enter your dice number' in str:
#                #sendGUI(Defend)
#                self.currentState = 'Defend'
#                self.send("list all")
#                continue
#            else:
#                if 'Cards cannot be traded in, please enter card numbers correctly' in str:
#                    str = 'Cards cannot be traded in, please select correct cards'
#                elif 'Please move armies in (enter single integer)' in str:
#                    str = 'Please move armies in'
#                if not ("World State" in str):
#                    self.log(str)
#                if 'occupied by' in str:
#                    if self.currentState == 'PlaceSingle':
#                        self.handle.state = "roam"
#                        self.currentState = None 
#                        self.send("list all")
#                        continue
#                
#                if 'cannot' in str:
#                    if self.currentState == 'TradeOrPass':
#                        #sendGUI(TradeOrPass)
#                        continue
#                    elif self.currentState == 'MustTrade':
#                        #sendGUI(MustTrade)
#                        continue
#                if 'has traded in and get' in str:
#                    if self.currentState == 'TradeOrPass':
#                        
#                        self.currentState = None
#                        continue
#                    elif self.currentState == 'MustTrade':
#                        
#                        self.currentState = None
#                        continue
#                if 'Invalid Move' in str:
#                    if self.currentState == 'MoveOrPass':
#                        #sendGUI(MoveOrPass)
#                        continue
#                if 'Successful' in str:
#                    if self.currentState == 'MoveOrPass':
#                        
#                        self.currentState = None
#                        continue
#                if 'Invalid Attack' in str:
#                    if self.currentState == 'AttackOrPass':
#                        #sendGUI(AttackOrPass)
#                        continue
#                if 'Attacker lost' in str:
#                    if self.currentState == 'AttackOrPass':
#                        toArmyNum = int(str.split('-')[1].strip())
#                        if(toArmyNum == 0):
#                            #sendGUI(PlaceCapturedRegion)
#                            self.currentState = 'PlaceCapturedRegion'
#                            continue
#                if 'Enter something bigger' in str or 'Not enough armies' in str or 'enter a valid integer' in str:
#                    if self.currentState == 'PlaceCapturedRegion':
#                        #sendGUI(PlaceCapturedRegion)
#                        continue
#                if 'Transfer complete' in str:
#                    if self.currentState == 'PlaceCapturedRegion':
#                        
#                        self.currentState = None
#                        continue
#                if 'at most 2 or' in str or 'enter 1 or 2' in str:
#                    if self.currentState == 'Defend':
#                        #sendGUI(Defend)
#                        continue
#                if 'defended with' in str:
#                    if self.currentState == 'Defend':
#                        self.currentState = None
#                        continue
#                if "World State" in str:
#                    self.handle.updateWorldMap(str)
#                if 'You completed income placement' in str and self.handle.state == "place_or_pass" and self.currentState == "PlaceOrPass":
#                    self.handle.state = "roam"
#                    self.currentState = None
#                if 'You completed army placement' in str and self.handle.state == "place_army" and self.currentState == "Place":
#                    self.handle.state = "roam"
#                    self.currentState = None
#                if "placed" in str and "armies" in str and (self.currentState == "PlaceOrPass" or self.currentState == "Place"):
#                    self.send("list all")
#                if "occupied" in str and self.currentState == "PlaceSingle":
#                    self.send("list all")
            
        return

    def updateWorldMap(self, wm):
        self.worldMap = ''
        lines = wm.split("\n")
        for line in lines:
            parts = line.split(" ")
            if(len(parts) == 3):
                [name, color, armies] = parts
                lineStr = ''
                lineStr += name.strip() + ',' + color.strip() + ',' + armies.strip() + '\n'
                self.worldMap += lineStr

    def updateState(self, s1, s2):
        if(not s2 is None):
            pass
            #self.handle.state = s2
            if(s2 == S_ROAM):
                pass
                #self.handle.setCommandLabel("Waiting for others")
        if(not s1 is None): 
            self.currentState = s1
        
    def refresh(self):
        self.send("list all")
        
    def refreshCards(self):
        self.send("list cards")
        
    def send(self, message):
        self.socket.send(message)

    def place(self, terr=None, army = None, passFlag = True, captured = False):
        if captured:
            self.send(army)
        elif(not army):
            self.send('Place ' + terr)
        elif(not passFlag):
            self.send('Place ' + terr + ' ' + army)
        else:
            self.send('Place ' + terr + ' ' + army)

    def trade(self, cardNums, passFlag = True):
        if not passFlag:
            self.send('Trade ' + cardNums[0] + ' ' + cardNums[1] + ' ' + cardNums[2])
        else:
            self.send('Trade ' + cardNums[0] + ' ' + cardNums[1] + ' ' + cardNums[2])

    def move(self, fromTerr, toTerr, armyNum):
        self.send('Move ' + fromTerr + ' ' + toTerr + ' ' + armyNum)

    def attack(self, fromTerr, toTerr, armyNum):
        self.send('Attack ' + fromTerr + ' ' + toTerr + ' ' + armyNum)

    def defend(self, diceNum):
        self.send(diceNum)

    def doPass(self):
        self.updateState(S_ROAM, S_ROAM)
        self.send('Pass')
        
    def log(self,message):
        self.logstr+=message
    