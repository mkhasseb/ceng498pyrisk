# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="ozgur"
__date__ ="$May 6, 2011 12:25:30 AM$"

import socket

class ClientHelper(Thread):
    def __init__(self, host, port):
        Thread.__init__(self)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.socket.connect((host, port))
        except socket.error, msg:
            #sendGUI(connection error)
            return
        self.end = False
        self.currentState = None

    def run(self):
        while(not self.end):
            str = self.socket.recv(10000)
            str = str.strip()
            if(str != ""):
                continue
            elif 'Usage: Place' in str:
                if 'Pass' in str:
                    #sendGUI(PlaceOrPass)
                    self.currentState = 'PlaceOrPass'
                    continue
                elif 'Usage: Place <territory name> <army number>' in str:
                    #sendGUI(Place)
                    self.currentState = 'Place'
                    continue
                elif 'Usage: Place <territory name>' in str:
                    #sendGUI(PlaceSingle)
                    self.currentState = 'PlaceSingle'
                    continue
            elif 'Usage: Trade' in str:
                if 'Pass' in str:
                    #sendGUI(TradeOrPass)
                    self.currentState = 'TradeOrPass'
                    continue
                else:
                    #sendGUI(MustTrade)
                    self.currentState = 'MustTrade'
                    continue
            elif 'Usage: Move' in str:
                #sendGUI(MoveOrPass)
                self.currentState = 'MoveOrPass'
                continue
            elif 'Usage: Attack' in str:
                #sendGUI(AttackOrPass)
                self.currentState = 'AttackOrPass'
                continue
            elif 'Enter your dice number' in str:
                #sendGUI(Defend)
                self.currentState = 'Defend'
                continue
            else:
                if 'Cards cannot be traded in, please enter card numbers correctly' in str:
                    str = 'Cards cannot be traded in, please select correct cards'
                elif 'Please move armies in (enter single integer)' in str:
                    str = 'Please move armies in'
                #updateGUIList(str)
                if 'occupied by' in str or 'have only' in str:
                    if self.currentState == 'PlaceOrPass':
                        #sendGUI(PlaceOrPass)
                        continue
                    elif self.currentState == 'Place':
                        #sendGUI(Place)
                        continue
                    elif self.currentState == 'PlaceSingle':
                        #sendGUI(PlaceSingle)
                        continue
                elif 'occupied' in str or 'armies in territory' in str:
                    if self.currentState == 'PlaceOrPass':
                        #sendGUI(UpdateWorld)
                        self.currentState = None
                        continue
                    elif self.currentState == 'Place':
                        #sendGUI(UpdateWorld)
                        self.currentState = None
                        continue
                    elif self.currentState == 'PlaceSingle':
                        #sendGUI(UpdateWorld)
                        self.currentState = None
                        continue
                if 'cannot' in str:
                    if self.currentState == 'TradeOrPass':
                        #sendGUI(TradeOrPass)
                        continue
                    elif self.currentState == 'MustTrade':
                        #sendGUI(MustTrade)
                        continue
                if 'has traded in and get' in str:
                    if self.currentState == 'TradeOrPass':
                        #sendGUI(UpdateWorld)
                        self.currentState = None
                        continue
                    elif self.currentState == 'MustTrade':
                        #sendGUI(UpdateWorld)
                        self.currentState = None
                        continue
                if 'Invalid Move' in str:
                    if self.currentState == 'MoveOrPass':
                        #sendGUI(MoveOrPass)
                        continue
                if 'Successful' in str:
                    if self.currentState == 'MoveOrPass':
                        #sendGUI(UpdateWorld)
                        self.currentState = None
                        continue
                if 'Invalid Attack' in str:
                    if self.currentState == 'AttackOrPass':
                        #sendGUI(AttackOrPass)
                        continue
                if 'Attacker lost' in str:
                    if self.currentState == 'AttackOrPass':
                        toArmyNum = int(str.split('-')[1].strip())
                        if(toArmyNum == 0):
                            #sendGUI(PlaceCapturedRegion)
                            self.currentState = 'PlaceCapturedRegion'
                            continue
                if 'Enter something bigger' in str or 'Not enough armies' in str or 'enter a valid integer' in str:
                    if self.currentState == 'PlaceCapturedRegion':
                        #sendGUI(PlaceCapturedRegion)
                        continue
                if 'Transfer complete' in str:
                    if self.currentState == 'PlaceCapturedRegion':
                        #sendGUI(UpdateWorld)
                        self.currentState = None
                        continue
                if 'at most 2 or' in str or 'enter 1 or 2' in str:
                    if self.currentState == 'Defend':
                        #sendGUI(Defend)
                        continue
                if 'defended with' in str:
                    if self.currentState == 'Defend':
                        self.currentState = None
                        continue
        return

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
        self.send('Pass')
    