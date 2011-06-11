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
import socket
from risk.Territory import Territory
from risk.Continent import Continent
from risk.Card import Card
from risk.Goal import GoalFactory
from risk.Player import Player
from random import shuffle
from threading import Thread

class GameThread(Thread):
    def __init__(self, gameName, setup, continents, cards, goals, handle):
        Thread.__init__(self)
        self.setup = setup
         
        self.ended = False
        self.handle = handle
        self.continents = continents
        self.cards = cards
        self.goals = goals
        self.gameName = gameName
        
    def run(self):
        try:
            self.handle.addLog(self.gameName, "Setting up game\n")
            self.handle.log(gameName = self.gameName)
            self.game = self.setup.initGame(self.continents, self.cards, self.goals, self)
            self.game.start()
            self.handle.addLog(self.gameName, "Game started wait until it finishes\n")
            self.handle.log(gameName = self.gameName)
            
            while(not self.game.ended):
                time.sleep(1)
            if(self.game.victor):
                self.handle.addLog(self.gameName, 'victor is ' + self.game.victor.color + 'with mission ' + self.game.victor.mission.verbose + '\n')
                self.handle.log(gameName = self.gameName)
            else:
                self.handle.addLog(self.gameName, 'There was a quiter noob newbie in the game\n')
                self.handle.log(gameName = self.gameName)
                
            time.sleep(3)
            self.handle.endGame(game = self.gameName)
        except Exception as e:
            self.handle.log(message = '%s' % e)
            self.handle.endGame(game = self.gameName)


class GamesInfoThread(Thread):
    def __init__(self, host, port, games):
        self.host = host
        self.port = port
        self.games = games
        Thread.__init__(self)

    def run(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((self.host, self.port))
        server.listen(5)

        while True:
            cs  = server.accept()
            gamesInfo = ''
            for name,info in self.games.iteritems():
                gamesInfo += name + ','
                gamesInfo += info['host'] + ':' + str(info['port']) + ','
                gamesInfo += str(info['currentPlayerNum']) + '/' + str(info['playerNum']) + '\n'
            cs[0].send(gamesInfo)


class GameCreator(QtGui.QMainWindow):
    '''
    classdocs
    '''
    def __init__(self, gamesInfoHost, gamesInfoPort, parent=None):
        '''
        Constructor
        '''
        QtGui.QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.mapF = None
        self.games = {}
        self.gip = gamesInfoPort
        self.gih = gamesInfoHost
        self.gamesInfoT = GamesInfoThread(self.gih, self.gip, self.games)
        self.gamesInfoT.start()

    def openMap(self):
        file = QtGui.QFileDialog.getOpenFileName(self, "Open a Map")
        mapFile = file + "_image"
        if(os.path.isfile(file) and os.path.isfile(mapFile)):
            self.mapF = file
            self.ui.selectedMapLabel.setText('Map loaded from %s' % file)
        else:
            self.mapF = None
            self.ui.selectedMapLabel.setText('Can not load map')

    def addLog(self, gameName, log):
        self.games[gameName]['log'] += log

    def playerNumInc(self, gameName):
        self.games[gameName]['currentPlayerNum'] += 1

    def startGameServer(self):
        try:
            #self.ui.startServerButton.setEnabled(False)
            host = self.ui.hostInput.text()
            port = int(self.ui.portInput.text())
            numplayer = int(self.ui.numPlayerInput.text())
            gameSetup = GenericGameSetup(host, port, numplayer)
            (continents, cards, goals) = self.parseGame(numplayer)

            gName = str(self.ui.gameNameInput.text())
            if(gName.strip() == ""):
                QtGui.QMessageBox.warning(self, "Game Name Warning", "Empty game name not allowed")
                return
            elif(gName in self.games):
                QtGui.QMessageBox.warning(self, "Game Name Warning", "Game %s already exists" % gName)
                return
            
            self.games[gName] = {}
            self.games[gName]['host'] = host
            self.games[gName]['port'] = port
            self.games[gName]['playerNum'] = numplayer
            self.games[gName]['currentPlayerNum'] = 0
            self.games[gName]['log'] = ''

            self.games[gName]['log'] += 'host:' + host + '  port:' + str(port) + '\n'
            self.ui.gameList.addItem(gName)
            
            self.gt = GameThread(gName, gameSetup, continents, cards, goals, self)
            self.games[gName]['game'] = self.gt
            self.games[gName]['game'].start()
        except Exception as e:
            self.log(message = str(e))
            self.endGame()

    def endGame(self, game=None):
        print 'end game'
        if game:
            print 'end game %s ' % game    
            del self.games[game]
            self.emit(QtCore.SIGNAL("removeGame(QString)"), QtCore.QString(game))
        self.ui.startServerButton.setEnabled(True)
    def deleteGame(self, gameName):
        gameName = str(gameName)
        print 'delete %s ' % gameName
        for i in range(self.ui.gameList.count()):
            print 'checking %s ' % str(self.ui.gameList.item(i))
            if(gameName == str(self.ui.gameList.item(i).text())):
                print 'removed item'
                self.ui.gameList.takeItem(i)
                break
    
    
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
        goals.append(GoalFactory.createOccupy((len(regions) * 2 / 3)+1))
        goals.append(GoalFactory.createConquer((len(regions) / 2)+1, 2))
        colors = [Player.COLOR_ORANGE, Player.COLOR_LPINK, Player.COLOR_GRAY, Player.COLOR_GREEN, Player.COLOR_RED, Player.COLOR_YELLOW]
        for i in range(numplayer):
            goals.append(GoalFactory.createEliminate(colors[i], (len(regions) * 2 / 3)+1))
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

    def selectGame(self, selectedGame):
        gameName = selectedGame.text()
        self.log(gameName = gameName)

    def log(self, message=None, gameName=None):
        if message:
            self.emit(QtCore.SIGNAL("log(QString)"),QtCore.QString(message))
        elif gameName and str(gameName) in self.games:
            gameName = str(gameName)
            tempStr = ''
            tempStr += str(self.games[gameName]['currentPlayerNum']) + '/' + str(self.games[gameName]['playerNum']) + '\n'
            tempStr += self.games[gameName]['log']
            #self.emit(QtCore.SIGNAL("clearGameLog(QString)"), QtCore.QString(gameName))
            self.emit(QtCore.SIGNAL("setGameLog(QString)"), QtCore.QString(tempStr))   
        else:
            print message
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    host = sys.argv[1]
    port = int(sys.argv[2])
    window = GameCreator(host, port)
    window.showMaximized()
    sys.exit(app.exec_())
