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


S_PLACE_SINGLE = "placeSingle"
S_PLACE_ARMIES = "placeArmies"
S_PLACE_INCOME = "placeIncome"
S_MOVE = "move"
S_ROAM = "roam"
continentColors = [QtGui.QColor("cyan"), QtGui.QColor("magenta"), QtGui.QColor("darkgray"), QtGui.QColor("darkred"), QtGui.QColor("darkgreen"), QtGui.QColor("white"), QtGui.QColor("black")]
class Region(QtGui.QGraphicsPolygonItem):
    def __init__(self, scene, polygon, continentColor):
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
    def hoverEnterEvent(self, event):
        self.state = "hovered"
        self.updateF()
    def hoverLeaveEvent(self, event):
        self.state = "default"
        brush = QtGui.QBrush()
        self.setBrush(brush)
        self.updateF()
    def paint(self, painter, option, widget=None):
        center = self.boundingRect().center()
        radius = max(self.boundingRect().height(), self.boundingRect().width()) 
        gr = QtGui.QRadialGradient(center, radius);
        if(self.state == 'hovered'):
            gr.setColorAt(0, self.occupantColor.darker())
            gr.setColorAt(1, self.continentColor.darker());
        else:
            gr.setColorAt(0, self.occupantColor);
            gr.setColorAt(1, self.continentColor);
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
        self.scene = QtGui.QGraphicsScene(0, 0, 800, 800)
        self.ui.mapView.setScene(self.scene)
        self.scene.mousePressEvent = self.mouseClickedOnMap
        self.regions = {}
        self.state = S_ROAM
        
        
    
    def dopass(self):
        self.ui.passButton.setEnabled(False)
        self.state = S_ROAM
        self.connector.doPass()
    def connect(self):
        try:
            hp = self.ui.connectInput.text()
            [host, port] = hp.split(':')[:2]
            port = int(port)
            self.connector = ClientHelper(host, port, self)
            self.connector.start()
        except Exception as e:
                self.log('%s' % e)
    def log(self, message):
        self.emit(QtCore.SIGNAL("log(QString)"), QtCore.QString(message))
    
    def map(self, map):
        self.map = map
    def mapImg(self):
        f = open('tmpImage', 'w')
        f.write(self.mapImage)
        f.flush()
        f.close()
        image = QtGui.QPixmap('tmpImage')
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
            r = Region(self.scene, polygon, continentColors[contColors[contName]])
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
                r = self.regions[name.strip()]
                r.occupantColor = QtGui.QColor(color.strip().lower())
                r.armies = int(armies.strip())
                r.updateF()
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
        self.ui.label_3.setText("Select a territory to place armies")
        self.state = S_PLACE_ARMIES
    def placeOrPass(self):
        self.state = S_PLACE_INCOME
        self.ui.passButton.setEnabled(True)
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
                self.connector.place(region.name, army_num)
            elif(self.state == S_PLACE_INCOME):
                army_num, ok = QtGui.QInputDialog.getInteger(self, "Army Placement", "Enter number of armies", value=1)
                while(not ok):
                    army_num, ok = QtGui.QInputDialog.getInteger(self, "Army Placement", "Enter number of armies", value=1)
                self.connector.place(region.name, army_num)
        else:
            self.log("No region selected")
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    window = DesktopClientApp()
    window.showMaximized()
    sys.exit(app.exec_())
        
