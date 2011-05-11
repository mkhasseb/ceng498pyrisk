'''
Created on 2011 5 7

@author: cihancimen
'''
from PyQt4 import Qt
from PyQt4 import QtCore
from PyQt4 import QtGui
from PyQt4.pyqtconfig import QtGuiModuleMakefile
from mainwindow import Ui_MainWindow
import os
from risk.default.GenericGameSetup import GenericGameSetup
import time
from risk.Territory import Territory
from risk.Continent import Continent
from risk.Card import Card
from risk.Goal import GoalFactory
from risk.Player import Player
from random import shuffle
from threading import Thread

class GameThread(Thread):
    def __init__(self, setup, continents, cards, goals, handle):
        Thread.__init__(self)
        self.setup = setup
         
        self.ended = False
        self.handle = handle
        self.continents = continents
        self.cards = cards
        self.goals = goals
    def run(self):
        try:
            self.handle.log("Setting up game")
            self.game = self.setup.initGame(self.continents, self.cards, self.goals, self.handle)
            
            self.game.start()
            self.handle.log("Game started wait until it finishes")
            while(not self.game.ended):
                time.sleep(1)
            if(self.game.victor):
                self.handle.log('victor is %s with mission %s ' % (self.game.victor.color, self.game.victor.mission))
            else:
                self.handle.log('There was a quiter noob newbie in the game')
            time.sleep(3)
            self.handle.endGame()
        except Exception as e:
            self.handle.log('%s' % e)
            self.handle.endGame()

class GameCreator(QtGui.QMainWindow):
    '''
    classdocs
    '''
    def __init__(self, parent=None):
        '''
        Constructor
        '''
        QtGui.QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.mapF = None

    def openMap(self):
        file = QtGui.QFileDialog.getOpenFileName(self, "Open a Map")
        mapFile = file + "_image"
        if(os.path.isfile(file) and os.path.isfile(mapFile)):
            self.mapF = file
            self.ui.selectedMapLabel.setText('Map loaded from %s' % file)
        else:
            self.mapF = None
            self.ui.selectedMapLabel.setText('Can not load map')
    def startGameServer(self):
        try:
            self.ui.startServerButton.setEnabled(False)
            host = self.ui.hostInput.text()
            port = int(self.ui.portInput.text())
            numplayer = int(self.ui.numPlayerInput.text())
            gameSetup = GenericGameSetup(host, port, numplayer)
            (continents, cards, goals) = self.parseGame(numplayer)
            
            self.gt = GameThread(gameSetup, continents, cards, goals, self)
            self.gt.start()
        except Exception as e:
            self.log("%s " % e)
            self.endGame()

    def endGame(self):
            self.ui.startServerButton.setEnabled(True)
    
    def parseGame(self, numplayer):
        mapFile = open(self.mapF, 'r')
        numReg = int(mapFile.readline())
        regions = {}
        conTerrs = {}
        continents = {}
        cards = []
        goals = []
#        print 'regions ', numReg
        for i in range(numReg):
            regstr = mapFile.readline().split(':')[:2]
            (name, conName) = tuple(regstr[0]. split(','))
#            print 'reg', name, conName
            neigbours = regstr[1].split(',')[:-1]
#            print 'n ', neigbours
            terr = Territory(name)
            regions[name] = terr
            terr.nn = neigbours
            terr.cn = conName
            if(not (conName in conTerrs)):
                conTerrs[conName] = [] 
            conTerrs[conName].append(terr)
        numCont = int(mapFile.readline())
#        print 'conts ', numCont
        print conTerrs
        for terr in regions.values():
            for n in terr.nn:
                terr.addNeighbour(regions[n])
                                     
        for i in range(numCont):
            (contName, bonus) = tuple(mapFile.readline().split(','))
            print contName, bonus
            cont = Continent(contName, conTerrs[contName], int(bonus))
            continents[contName] = cont
            for terr in cont.territories:
                print 't,', terr.name
                terr.continent = cont
        i = 0;
        for terr in regions.values():
            type = None
            if(i == 0):
                type = Card.TYPE_INFANTRY
            elif(i == 1):
                type = Card.TYPE_CAVALRY
            else:
                type = Card.TYPE_ARTILLERY
            cards.append(Card(type, territory=terr))
            i += 1
            i %= 3
        cards.append(Card(Card.TYPE_WILD))
        cards.append(Card(Card.TYPE_WILD))
        goals.append(GoalFactory.createOccupy(len(regions) * 2 / 3))
        goals.append(GoalFactory.createConquer((len(regions) / 2), 2))
        colors = [Player.COLOR_BLACK, Player.COLOR_BLUE, Player.COLOR_GRAY, Player.COLOR_GREEN, Player.COLOR_RED, Player.COLOR_YELLOW]
        for i in range(numplayer):
            goals.append(GoalFactory.createEliminate(colors[i], len(regions) * 2 / 3))
        if(len(continents) > 5):
            for i in range(3):
                conts = continents.values()
                shuffle(conts)
                c1 = conts.pop()
                c2 = conts.pop()
                goals.append(GoalFactory.createConquerContinent([c1, c2]))
                
        mapFile.close()
        f = open(self.mapF, 'r')
        self.map = f.read()
        f.close()
        fi = open(self.mapF+"_image")
        self.mapImg = ""
        while True:
            temp  = fi.read()
            if(temp == ''):break
            self.mapImg +=temp
        print self.mapImg
        fi.close()
        return (continents.values(), cards, goals)
                         
    def log(self, message):
        self.emit(QtCore.SIGNAL("log(QString)"),QtCore.QString(message))
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    window = GameCreator()
    window.showMaximized()
    sys.exit(app.exec_())
