'''
Created on 2011 4 23

@author: cihancimen
'''

from copy import copy

from PyQt4 import Qt
from PyQt4 import QtCore
from PyQt4 import QtGui
from PyQt4.pyqtconfig import QtGuiModuleMakefile
from mainwindow import Ui_MainWindow

class Region(object):
    def __init__(self, name):
        self.name = name
        self.polygon = QtGui.QPolygonF()
        self.i = 1
        self.done = False
        self.itemp = None
        self.neighbours = []
    def addPoint(self, point):
        self.polygon.insert(self.i - 1, point)
        self.polygon.insert(self.i, self.polygon.at(0))
        self.i += 1

class MapCreatorApp(QtGui.QMainWindow):
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
        self.ui.mapView.setScene(QtGui.QGraphicsScene(0, 0, 1000, 1000))
        self.ui.mapView.scene().mousePressEvent = self.mouseClickedOnMap
        self.ui.mapView_2.setScene(QtGui.QGraphicsScene(0, 0, 1000, 1000))
        self.ui.mapView_2.scene().mousePressEvent = self.mouseClickedOnMap
        self.regions = {}
        self.chooseRegion(None)
        self.currentTabIndex = self.ui.tabWidget.currentIndex()
        self.formLinking = False
        self.removeLinking = False
        self.selectedRegion = None
        
    def log(self, message):
        if(self.currentTabIndex == 0):
            self.ui.logText.appendPlainText(message)
        elif(self.currentTabIndex == 1):
            self.ui.logText_2.appendPlainText(message)

    def refreshRegionList(self):
        self.ui.regionList.clear()
        for name in self.regions.keys():
            self.ui.regionList.addItem(name)

    def startLinking(self):
        self.log("Clicked start linking button")
        if(self.currentRegion is None):
            self.log("A region has to be selected")
        elif(not (self.currentRegion is None)):
            self.formLinking = True

    def endLinking(self):
        self.log("Clicked end linking button")
        if(self.currentRegion is None):
            self.log("A region has to be selected")
        else:
            self.formLinking = False
            self.chooseRegion(None)

    def startRemoving(self):
        self.log("Clicked start canceling button")
        if(self.currentRegion is None):
            self.log("A region has to be selected")
        elif(not (self.currentRegion is None)):
            self.removeLinking = True

    def endRemoving(self):
        self.log("Clicked end canceling button")
        if(self.currentRegion is None):
            self.log("A region has to be selected")
        else:
            self.removeLinking = False
            self.chooseRegion(None)

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
        self.refreshRegionList()
        
    def clearRegion(self):
        self.log("Clicked clear region button")
        if(self.currentRegion is None):
            self.log("No region to clear")
        else:
            id = self.currentRegion.itemp
            self.ui.mapView.scene().removeItem(id)
            del self.regions[self.currentRegion.name]
            self.chooseRegion(None)
        self.refreshRegionList()
            
    def mouseClickedOnMap(self, event):
        self.log("Mouse clicked on %f, %f" % (event.scenePos().x(), event.scenePos().y()))
        if(self.currentTabIndex == 0):
            if(self.currentRegion is None):
                point = event.scenePos()
                for v in self.regions.values():
                    p = QtGui.QPolygonF()
                    p.insert(0, point)
                    point.setX(point.x() + 1)
                    p.insert(1, point)
                    point.setY(point.y() + 1)
                    p.insert(2, point)
                    i = v.polygon.intersected(p)
                    if(i.count() > 1):
                        self.chooseRegion(v)
                        self.log("Selected region: %s" % v.name)
                        break
            else:
                self.currentRegion.addPoint(event.scenePos())
                self.refreshPolygon(self.currentRegion)
        elif(self.currentTabIndex == 1):
            point = event.scenePos()
            for v in self.regions.values():
                p = QtGui.QPolygonF()
                p.insert(0, point)
                point.setX(point.x() + 1)
                p.insert(1, point)
                point.setY(point.y() + 1)
                p.insert(2, point)
                i = v.polygon.intersected(p)
                if(i.count() > 1):
                    if((not self.formLinking) and (not self.removeLinking)):
                        self.chooseRegion(v)
                    elif(self.formLinking and (not self.removeLinking)):
                        self.addNeighbour(v)
                    elif(self.removeLinking and (not self.formLinking)):
                        self.removeNeighbour(v)
                    self.log("Selected region: %s" % v.name)
                    return

    def addNeighbour(self, r):
        if(not (r.name in self.currentRegion.neighbours)):
            self.currentRegion.neighbours.append(r.name)
            r.neighbours.append(self.currentRegion.name)
            self.log("%s has been added to neighbours of %s" %(r.name, self.currentRegion.name))
        else:
            self.log("%s has already been a neighbour of %s" %(r.name, self.currentRegion.name))

    def removeNeighbour(self, r):
        if(r.name in self.currentRegion.neighbours):
            self.currentRegion.neighbours.remove(r.name)
            r.neighbours.remove(self.currentRegion.name)
            self.log("%s has been removed from neighbours of %s" %(r.name, self.currentRegion.name))
        else:
            self.log("%s is not a neighbour of %s" %(r.name, self.currentRegion.name))

    def refreshPolygon(self, region):
        scene = self.ui.mapView.scene()
        scene.removeItem(region.itemp)
        region.itemp = scene.addPolygon(region.polygon, brush=QtGui.QBrush(QtGui.QColor("lightgray"), style=Qt.Qt.Dense4Pattern))

    def tabChange(self):
        if(not (self.currentRegion is None) and not self.currentRegion.done):
            self.log("Region creation is not finished")
            self.ui.tabWidget.setCurrentIndex(self.currentTabIndex)
        else:
            self.currentTabIndex = self.ui.tabWidget.currentIndex()
            if(self.currentTabIndex == 1):
                self.ui.mapView_2.setScene(self.ui.mapView.scene())

    def actionOpen(self):
        filename = QtGui.QFileDialog.getOpenFileName(self, "Open an Image")
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
        