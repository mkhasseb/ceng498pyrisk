'''
Created on 2011 5 7

@author: cihancimen
'''

from PyQt4 import Qt
from PyQt4 import QtCore
from PyQt4 import QtGui
from PyQt4.pyqtconfig import QtGuiModuleMakefile
from mainwindow import Ui_MainWindow
from threading import Thread
from ClientHelper import ClientHelper
from mapcreator.RiskMapCreator.MapCreatorApp import Region
import time
import uuid
import re


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
COLOR_RED = "Red"
COLOR_LPINK = "Pink"
COLOR_GREEN = "Green"
COLOR_GRAY = "Gray"
COLOR_ORANGE = "Orange"
COLOR_YELLOW = "Yellow"
    

occupantColors = { COLOR_RED : QtGui.QColor(253, 18, 26),  COLOR_LPINK : QtGui.QColor(238, 143, 255), COLOR_GREEN : QtGui.QColor(147, 255, 31), COLOR_GRAY: QtGui.QColor(183,183,183), COLOR_ORANGE: QtGui.QColor(251, 113, 14), COLOR_YELLOW: QtGui.QColor(241, 237,    4)}
continentColors = [QtGui.QColor(2, 157, 17), QtGui.QColor(1, 10, 254), QtGui.QColor(151,3,214), QtGui.QColor(113, 56 , 0), QtGui.QColor(96, 21, 21), QtGui.QColor("black"), QtGui.QColor("white")]
class Region(QtGui.QGraphicsPolygonItem):
    def __init__(self, scene, polygon, continentColor, context):
        QtGui.QGraphicsPolygonItem.__init__(self, polygon, scene=scene)
        self.setAcceptHoverEvents(True)
#        self.setActive(True)
        self.neighbours = []
        self.armies = 0
        self.name = None
        self.occupantColor = QtGui.QColor("white")
        self.continentColor = continentColor
        self.state = "default"
        self.otherBrush = None
        self.context = context
    def hoverEnterEvent(self, event):
        self.state = "hovered"
        for n in self.neighbours:
            self.context.regions[n].state = 'shiver'
        self.updateF()
    def hoverLeaveEvent(self, event):
        self.state = "default"
        for n in self.neighbours:
            self.context.regions[n].state = 'default'
        brush = QtGui.QBrush()
        self.setBrush(brush)
        self.updateF()
    def paint(self, painter, option, widget=None):
        center = self.boundingRect().center()
        radius = max(self.boundingRect().height(), self.boundingRect().width()) 
        gr = QtGui.QRadialGradient(center, radius);
        if(self.state == 'hovered'):
            gr.setColorAt(0, self.occupantColor.darker())
            gr.setColorAt(0.27, self.occupantColor.darker())
            gr.setColorAt(0.3, QtGui.QColor("white"))
            gr.setColorAt(0.5, self.continentColor.darker())
            gr.setColorAt(1, self.continentColor.darker())
        elif(self.state == 'shiver'):
            factor = 150
            gr.setColorAt(0, self.occupantColor.lighter(factor = factor))
            gr.setColorAt(0.27, self.occupantColor.lighter(factor = factor))
            gr.setColorAt(0.3, QtGui.QColor("white"))
            gr.setColorAt(0.5, self.continentColor.lighter(factor = factor))
            gr.setColorAt(1, self.continentColor.lighter(factor = factor))
        else:
            gr.setColorAt(0, self.occupantColor);
            gr.setColorAt(0.27, self.occupantColor);
            gr.setColorAt(0.3, QtGui.QColor("white"))
            gr.setColorAt(0.5, self.continentColor)
            gr.setColorAt(1, self.continentColor)
        brush = QtGui.QBrush(gr)
        self.setBrush(brush)
        QtGui.QGraphicsPolygonItem.paint(self, painter, option, widget)
        painter.drawText(self.boundingRect(), QtCore.Qt.AlignCenter, self.name+str(self.armies))
            
    def updateF(self):
        self.update(self.boundingRect())

class DesktopClientApp(QtGui.QMainWindow):
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
        self.connector = None
        self.scene = QtGui.QGraphicsScene(0, 0, 1000, 1000)
        self.ui.mapView.setScene(self.scene)
        self.scene.mousePressEvent = self.mouseClickedOnMap
        self.regions = {}
        self.state = S_ROAM
        self.ui.playerLabel.setVisible(False)
        self.ui.playerView.setVisible(False)
        self.ui.missionLabel.setVisible(False)
        self.ui
        
        
    
    def dopass(self):
        self.ui.passButton.setEnabled(False)
        self.ui.tradeButton.setEnabled(False)
        self.state = S_ROAM
        self.connector.doPass()
    def connect(self):
        try:
            hp = self.ui.connectInput.text()
            [host, port] = hp.split(':')[:2]
            port = int(port)
            self.connector = ClientHelper(host, port, self)
            self.connector.start()
            self.ui.connectButton.setEnabled(False)
        except Exception as e:
            self.ui.connectButton.setEnabled(True)
            self.log('%s' % e)
    def log(self, message):
        self.emit(QtCore.SIGNAL("log(QString)"), QtCore.QString(message))
    
    def map(self, map):
        self.map = map
    def mapImg(self):
        fname = "tmpImage"+str(uuid.uuid1())
        f = open(fname, 'w')
        f.write(self.mapImage)
        f.flush()
        f.close()
        image = QtGui.QPixmap(fname)
        item = QtGui.QGraphicsPixmapItem(image)
        self.scene.clear()
        self.scene.addItem(item)
        
        print self.map
        lines = self.map.split("\n")
        for i in range(len(lines)):
            if(lines[i] == "" or ("Turn of" in lines[i])):
                del lines[i]
        numReg = int(lines[0])
        numCont = int(lines[numReg + 1])
        contColors = {}
        for i in range(numCont):
            (conname, bonus) = lines[numReg + 2 + i].split(",")
            contColors[conname] = i
            self.ui.contList.addItem(QtCore.QString(conname + " " + bonus + "(Bonus)"))
            self.ui.contList.item(i).setData(QtCore.Qt.DecorationRole, QtCore.QVariant(continentColors[contColors[conname]]))
        for i in range(numReg):
            regStr = lines[i+1]
            [namecont,neighbours,points] = regStr.split(":")
            [name, contName] = namecont.split(',')
            neighbours = neighbours.split(',')[:-1]
            points = points.split(',')[:-1]
            polygon = QtGui.QPolygonF()
            for p in points:
                point  = QtCore.QPointF(float(p.split('-')[0]),float(p.split('-')[1]) )
                polygon.append(point)
            r = Region(self.scene, polygon, continentColors[contColors[contName]], self)
            r.name = name
            r.armies = 0
            r.neighbours = neighbours
            self.regions[r.name] = r
    def updateWorldMap(self, wm):
        lines = wm.split("\n")
        for line in lines:
            parts = line.split(" ")
            if(len(parts) == 3):
                [name, color, armies] = parts
                if name.strip() in self.regions:
                    r = self.regions[name.strip()]
                    r.occupantColor = occupantColors[color]
                    r.armies = int(armies.strip())
                    r.updateF()
                
    def updateCardList(self, cl):
        lines = cl.split('\n')
        for i  in range(len(lines)):
            line = lines[i]
            if 'Cards' in line:
                match = re.search('(\d+)', line)
                cardnum = int(match.group())
                self.ui.cardList.clear()
                for j in range(i+1, i+ 1+cardnum):
                    self.ui.cardList.addItem(lines[j].replace("\t",''))
                break
    def slotTradeIn(self):
        selected = self.ui.cardList.selectedItems()
        if(len(selected) != 3):
            QtGui.QMessageBox.information(self, 'Selection Error', 'Select Exactly 3 Cards')
        else:
            selectedids = map( lambda x: re.search('(\d+)', x).group() , selected)
            self.connector.trade(selectedids)
    def loadImgSlt(self):
        self.mapImg()
    def setStateLabel(self):
        self.ui.stateLabel.setText(self.connector.currentState+ " " + self.state)
    def mapImgSig(self):
        self.emit(QtCore.SIGNAL("loadImgSig()"))
    def placeSingle(self):
        self.ui.label_3.setText("Select an unoccupied territory to occupy")
        self.state = S_PLACE_SINGLE
    def placeArmy(self):
        self.setCommandLabel("Select a territory to place armies")
        self.state = S_PLACE_ARMIES
    def placeOrPass(self):
        self.setCommandLabel("PLACE Income or PASS")
        self.state = S_PLACE_INCOME
        self.ui.passButton.setEnabled(True)
    def attackOrPass(self):
        self.setCommandLabel("Select a region to ATTACK or PASS")
        self.state = S_ATTACK_0
        self.ui.passButton.setEnabled(True)
    def moveOrPass(self):
        self.setCommandLabel("SELECT a region to MOVE armies from or PASS")
        self.state = S_MOVE_0
        self.ui.passButton.setEnabled(True)
    def tradeOrPass(self):
        self.setCommandLabel("SELECT cards to TRADE or PASS")
        self.ui.tradeButton.setEnabled(True)
        if(self.state == S_TRADE):
            self.ui.passButton.setEnabled(True)
    def transfer(self):
        self.setCommandLabel("TRANSFER armies to occupied region")
        self.state = S_TRANSFER
        print 'signaling transfer' 
        self.emit(QtCore.SIGNAL("signalTransferPopup()"))
        
    def slotTransferPopup(self):
        army_num, ok = QtGui.QInputDialog.getInteger(self, "Select Number of armies to transfer newly conquered region", "Enter number of armies", value=1)
        while(not ok):
            army_num, ok = QtGui.QInputDialog.getInteger(self, "Select Number of armies to transfer newly conquered region", "Enter number of armies", value=1)
        self.connector.place(army = str(army_num), captured = True)
    def defend(self, region=None):
        if(region is None):
            region = self.defendRegion
        else:
            self.defendRegion = region
        if region is None:
            region = 'Amk'
        print 'signaling with region : %s'  % region
        self.emit(QtCore.SIGNAL("signalDefendPopup(QString)"), QtCore.QString(region))
    def setPlayerName(self, name):
        self.emit(QtCore.SIGNAL("signalPlayerName(QString)"), QtCore.QString(name))
    def setMission(self, mission):
        self.emit(QtCore.SIGNAL("signalMission(QString)"), QtCore.QString(mission))
    def victorFound(self, mess):
        self.emit(QtCore.SIGNAL("signalVictor(QString)"), QtCore.QString(mess))
    def slotVictor(self, mess):
        QtGui.QMessageBox.warning(self, 'Game Ended', mess)
        sys.exit()
    def slotMission(self, mission):
        self.ui.missionLabel.setVisible(True)
        self.ui.missionLabel.setText("Mission: " + str(mission))
    def slotPlayerName(self, name):
        self.ui.playerLabel.setVisible(True)
        self.ui.playerView.setVisible(True)
        self.ui.playerLabel.setText(name)
        scene = QtGui.QGraphicsScene(0, 0, 51, 41)
        brush = QtGui.QBrush(occupantColors[str(name)])
        pen = QtGui.QPen(brush)
        scene.addRect(QtCore.QRectF(0,0,51,41), pen=pen).setBrush(brush)
        self.ui.playerView.setScene(scene)
    def slotDefendPopup(self,region):
        army_num, ok = QtGui.QInputDialog.getInteger(self, "Defend Territory %s" % region, "Enter number of armies to defend", value=1, min =1, max =2, step=1)
        while(not ok):
            army_num, ok = QtGui.QInputDialog.getInteger(self, "Defend Territory %s" % region, "Enter number of armies to defend", value=1, min =1, max =2, step=1)
        self.connector.defend(str(army_num))
    def setCommandLabel(self, message):
        self.ui.label_3.setText(message)
    def mouseClickedOnMap(self, event):
        items = self.scene.items(event.scenePos())
#        self.log("Selected items are %s" % items)
        region = None
        for item in items:
            if(isinstance(item, Region)):
                region  = item
                break;
        if(not region is None):
            self.log("Selected region is %s" % region.name)
            if(self.state == S_PLACE_SINGLE):
                self.connector.place(region.name)
            elif(self.state == S_PLACE_ARMIES):
                army_num, ok = QtGui.QInputDialog.getInteger(self, "Army Placement", "Enter number of armies", value=1)
                while(not ok):
                    army_num, ok = QtGui.QInputDialog.getInteger(self, "Army Placement", "Enter number of armies", value=1)
                self.connector.place(region.name, str(army_num))
            elif(self.state == S_PLACE_INCOME):
                army_num, ok = QtGui.QInputDialog.getInteger(self, "Army Placement", "Enter number of armies", value=1)
                while(not ok):
                    army_num, ok = QtGui.QInputDialog.getInteger(self, "Army Placement", "Enter number of armies", value=1)
                self.connector.place(region.name, str(army_num))
            elif(self.state == S_ATTACK_0):
                self.attackfrom = region.name
                self.state = S_ATTACK_1
                self.setCommandLabel("SELECT a region to ATTACK")
                self.ui.passButton.setEnabled(False)
            elif(self.state == S_ATTACK_1):
                self.attackto = region.name
                army_num, ok = QtGui.QInputDialog.getInteger(self, "Select Number of armies to attack", "Enter number of armies", value=1)
                while(not ok):
                    army_num, ok = QtGui.QInputDialog.getInteger(self, "Select Number of armies to attack", "Enter number of armies", value=1)
                self.setCommandLabel("ENTER number of armies to ATTACK")
                self.state = S_ATTACK_2
                self.connector.attack(self.attackfrom, self.attackto, str(army_num))
                self.attackto, self.attackfrom = None, None
            elif(self.state == S_MOVE_0):
                self.movefrom = region.name
                self.setCommandLabel("SELECT a region to MOVE armies")
                self.state = S_MOVE_1
                self.ui.passButton.setEnabled(False)
            elif(self.state == S_MOVE_1):
                self.moveto = region.name
                army_num, ok = QtGui.QInputDialog.getInteger(self, "Select Number of armies to move", "Enter number of armies", value=1)
                while(not ok):
                    army_num, ok = QtGui.QInputDialog.getInteger(self, "Select Number of armies to move", "Enter number of armies", value=1)
                self.setCommandLabel("ENTER number of armies to MOVE")
                self.state = S_MOVE_2
                self.connector.move(self.movefrom, self.moveto, str(army_num))
                self.moveto, self.movefrom = None, None
        else:
            self.log("No region selected")
            
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    window = DesktopClientApp()
    window.showMaximized()
    sys.exit(app.exec_())
        