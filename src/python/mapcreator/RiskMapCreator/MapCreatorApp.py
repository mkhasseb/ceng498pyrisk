'''
Created on 2011 4 23

@author: cihancimen
'''
from mapcreator.RiskMapCreator.mainwindow import Ui_MainWindow
from PyQt4 import Qt, QtGui, QtCore
from copy import copy
from PyQt4.pyqtconfig import QtGuiModuleMakefile

class Region(object):
    def __init__(self, name):
        self.name= name
        self.polygon = QtGui.QPolygonF()
        self.i= 1
        self.done = False
        self.itemp =None
    def addPoint(self, point):
        self.polygon.insert(self.i - 1 , point)
        self.polygon.insert(self.i, self.polygon.at(0))
        self.i += 1
    

class MapCreatorApp(QtGui.QMainWindow):
    '''
    classdocs
    '''
    

    def __init__(self,parent=None):
        '''
        Constructor
        '''
        QtGui.QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.mapView.setScene(QtGui.QGraphicsScene(0, 0, 1000  , 1000))
        self.ui.mapView.scene().mousePressEvent = self.mouseClickedOnMap
        self.regions = {}
        self.chooseRegion(None)
        
    def log(self, message):
        self.ui.logText.appendPlainText(message)
    def beginRegion(self):
        self.log("Clicked begin region button")
        if(not (self.currentRegion is None) and not self.currentRegion.done):
            self.log("Current region is not finished")
            return 
        name = self.ui.regionName.text()
        if(name is None or name == ""):
            self.log("Region name can not be null")
        elif(name in self.regions):
            self.log("Name %s already in regions" % name)
        else:
            self.log("Adding region %s " % name)
            r = Region(name)
            self.chooseRegion(r)
            self.regions[name] = r
            self.refreshPolygon(r)
           
    def endRegion(self):
        self.log("Clicked end region button")
        if(self.currentRegion is None):
            self.log("No region to end")
        else:
            self.chooseRegion(None)
        
    def clearRegion(self):
        self.log("Clicked clear region button")
        if(self.currentRegion is None):
            self.log("No region to clear")
        else:
            id = self.currentRegion.itemp
            self.ui.mapView.scene().removeItem(id)
            del self.regions[self.currentRegion.name]
            self.chooseRegion( None)
            
            
    def mouseClickedOnMap(self, event):
        self.log("Mouse clicked on %f, %f" % (event.scenePos().x(), event.scenePos().y()))
        if(self.currentRegion is None):
            point = event.scenePos()
            for v in self.regions.values():
                p = QtGui.QPolygonF()
                p.insert(0, point)
                point.setX(point.x()+1)
                p.insert(1, point)
                point.setY(point.y()+1)
                p.insert(2, point)
                i = v.polygon.intersected(p)
                if(i.count() > 1):
                    self.chooseRegion(v)
                    self.log("Selected region: %s" % v.name)
                    break
        else:
            self.currentRegion.addPoint(event.scenePos())
            self.refreshPolygon(self.currentRegion)
    
    def refreshPolygon(self, region):
        scene = self.ui.mapView.scene()
        scene.removeItem(region.itemp)
        region.itemp = scene.addPolygon(region.polygon, brush= QtGui.QBrush(QtGui.QColor("lightgray"), style=Qt.Qt.Dense4Pattern))

    def actionOpen(self):
        
        filename=QtGui.QFileDialog.getOpenFileName(self, "Open an Image")
        try:
            image = QtGui.QPixmap(filename)
            item = QtGui.QGraphicsPixmapItem(image)
            self.ui.mapView.scene().clear()
            self.ui.mapView.scene().addItem(item)
            self.regions.clear()
            self.chooseRegion(None)
            self.log("opened file %s" % filename)
        except Exception as e:
            self.log("%s" % (e))
    def actionSave(self):
        self.log("Clicked save menu")    
    def chooseRegion(self, r):
        self.currentRegion = r
        if(r is None):
            self.ui.linkButton.setEnabled(True)
        else:
            self.ui.linkButton.setEnabled(False)
    def link(self):
        pass


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    window = MapCreatorApp()
    window.show()
    sys.exit(app.exec_())
        