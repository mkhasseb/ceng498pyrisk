# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Sun May 15 18:44:29 2011
#      by: PyQt4 UI code generator 4.8.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1600, 754)
        MainWindow.setStyleSheet(_fromUtf8("QPushButton {\n"
"color: #333;\n"
"border: 2px solid #555;\n"
"border-radius: 11px;\n"
"padding: 5px;\n"
"background: qradialgradient(cx: 0.3, cy: -0.4,\n"
"fx: 0.3, fy: -0.4,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #888);\n"
"min-width: 80px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: qradialgradient(cx: 0.3, cy: -0.4,\n"
"fx: 0.3, fy: -0.4,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #bbb);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background: qradialgradient(cx: 0.4, cy: -0.1,\n"
"fx: 0.4, fy: -0.1,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #ddd);\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"color: #333;\n"
"border: 2px solid #555;\n"
"border-radius: 11px;\n"
"background: qradialgradient(cx: 0.3, cy: -0.4,\n"
"fx: 0.3, fy: -0.4,\n"
"radius: 1.35, stop: 0 #888, stop: 1 #888);\n"
"}\n"
"\n"
"QMainWindow, #centralWidget, QListWidget, QLabel, QPlainTextEdit, QComboBox, QMessageBox, QInputDialog, QPlainTextEdit::handle {\n"
" color: #333;\n"
"border: 2px solid #555;\n"
"border-radius: 11px;\n"
"padding: 5px;\n"
"background: qradialgradient(cx: 0.3, cy: -0.4,\n"
"fx: 0.3, fy: -0.4,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #888);\n"
"}\n"
"\n"
"QSpinBox {\n"
" color: #333;\n"
"padding: 5px;\n"
"background: qradialgradient(cx: 0.3, cy: -0.4,\n"
"fx: 0.3, fy: -0.4,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #888);\n"
"}\n"
"QGraphicsView, QLineEdit {\n"
"     color: #333;\n"
"border: 2px solid #555;\n"
"border-radius: 11px;\n"
"padding: 5px;\n"
"\n"
"}"))
        self.centralWidget = QtGui.QWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralWidget.sizePolicy().hasHeightForWidth())
        self.centralWidget.setSizePolicy(sizePolicy)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralWidget)
        self.tabWidget.setGeometry(QtCore.QRect(50, 0, 1291, 701))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.regionTab = QtGui.QWidget()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.regionTab.sizePolicy().hasHeightForWidth())
        self.regionTab.setSizePolicy(sizePolicy)
        self.regionTab.setObjectName(_fromUtf8("regionTab"))
        self.logText = QtGui.QPlainTextEdit(self.regionTab)
        self.logText.setGeometry(QtCore.QRect(910, 390, 341, 211))
        self.logText.setObjectName(_fromUtf8("logText"))
        self.mapView = QtGui.QGraphicsView(self.regionTab)
        self.mapView.setGeometry(QtCore.QRect(0, 0, 901, 611))
        self.mapView.setProperty(_fromUtf8("cursor"), QtCore.Qt.CrossCursor)
        self.mapView.setMouseTracking(True)
        self.mapView.setObjectName(_fromUtf8("mapView"))
        self.layoutWidget = QtGui.QWidget(self.regionTab)
        self.layoutWidget.setGeometry(QtCore.QRect(910, 10, 240, 152))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setMaximumSize(QtCore.QSize(100, 40))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.regionName = QtGui.QLineEdit(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.regionName.sizePolicy().hasHeightForWidth())
        self.regionName.setSizePolicy(sizePolicy)
        self.regionName.setMaximumSize(QtCore.QSize(200, 40))
        self.regionName.setObjectName(_fromUtf8("regionName"))
        self.horizontalLayout.addWidget(self.regionName)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.beginButton = QtGui.QPushButton(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.beginButton.sizePolicy().hasHeightForWidth())
        self.beginButton.setSizePolicy(sizePolicy)
        self.beginButton.setObjectName(_fromUtf8("beginButton"))
        self.horizontalLayout_2.addWidget(self.beginButton)
        self.endButton = QtGui.QPushButton(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.endButton.sizePolicy().hasHeightForWidth())
        self.endButton.setSizePolicy(sizePolicy)
        self.endButton.setObjectName(_fromUtf8("endButton"))
        self.horizontalLayout_2.addWidget(self.endButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.clearButton = QtGui.QPushButton(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clearButton.sizePolicy().hasHeightForWidth())
        self.clearButton.setSizePolicy(sizePolicy)
        self.clearButton.setMinimumSize(QtCore.QSize(94, 0))
        self.clearButton.setObjectName(_fromUtf8("clearButton"))
        self.horizontalLayout_3.addWidget(self.clearButton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.regionList = QtGui.QListWidget(self.regionTab)
        self.regionList.setGeometry(QtCore.QRect(910, 180, 341, 191))
        self.regionList.setObjectName(_fromUtf8("regionList"))
        self.tabWidget.addTab(self.regionTab, _fromUtf8(""))
        self.neighbourTab = QtGui.QWidget()
        self.neighbourTab.setObjectName(_fromUtf8("neighbourTab"))
        self.mapView_2 = QtGui.QGraphicsView(self.neighbourTab)
        self.mapView_2.setGeometry(QtCore.QRect(0, 0, 1001, 611))
        self.mapView_2.setProperty(_fromUtf8("cursor"), QtCore.Qt.CrossCursor)
        self.mapView_2.setMouseTracking(True)
        self.mapView_2.setObjectName(_fromUtf8("mapView_2"))
        self.logText_2 = QtGui.QPlainTextEdit(self.neighbourTab)
        self.logText_2.setGeometry(QtCore.QRect(1020, 300, 411, 211))
        self.logText_2.setObjectName(_fromUtf8("logText_2"))
        self.layoutWidget1 = QtGui.QWidget(self.neighbourTab)
        self.layoutWidget1.setGeometry(QtCore.QRect(1130, 50, 151, 134))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.startLinkButton = QtGui.QPushButton(self.layoutWidget1)
        self.startLinkButton.setObjectName(_fromUtf8("startLinkButton"))
        self.verticalLayout_2.addWidget(self.startLinkButton)
        self.endLinkButton = QtGui.QPushButton(self.layoutWidget1)
        self.endLinkButton.setObjectName(_fromUtf8("endLinkButton"))
        self.verticalLayout_2.addWidget(self.endLinkButton)
        self.startRemoveButton = QtGui.QPushButton(self.layoutWidget1)
        self.startRemoveButton.setObjectName(_fromUtf8("startRemoveButton"))
        self.verticalLayout_2.addWidget(self.startRemoveButton)
        self.endRemoveButton = QtGui.QPushButton(self.layoutWidget1)
        self.endRemoveButton.setObjectName(_fromUtf8("endRemoveButton"))
        self.verticalLayout_2.addWidget(self.endRemoveButton)
        self.tabWidget.addTab(self.neighbourTab, _fromUtf8(""))
        self.continentTab = QtGui.QWidget()
        self.continentTab.setObjectName(_fromUtf8("continentTab"))
        self.mapView_3 = QtGui.QGraphicsView(self.continentTab)
        self.mapView_3.setGeometry(QtCore.QRect(10, 0, 721, 631))
        self.mapView_3.setObjectName(_fromUtf8("mapView_3"))
        self.continentList = QtGui.QListWidget(self.continentTab)
        self.continentList.setGeometry(QtCore.QRect(740, 0, 241, 281))
        self.continentList.setObjectName(_fromUtf8("continentList"))
        self.logText_3 = QtGui.QPlainTextEdit(self.continentTab)
        self.logText_3.setGeometry(QtCore.QRect(740, 300, 321, 281))
        self.logText_3.setObjectName(_fromUtf8("logText_3"))
        self.layoutWidget2 = QtGui.QWidget(self.continentTab)
        self.layoutWidget2.setGeometry(QtCore.QRect(990, 0, 261, 222))
        self.layoutWidget2.setObjectName(_fromUtf8("layoutWidget2"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_5.setMargin(0)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_3 = QtGui.QLabel(self.layoutWidget2)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_5.addWidget(self.label_3)
        self.continentNameEdit = QtGui.QLineEdit(self.layoutWidget2)
        self.continentNameEdit.setObjectName(_fromUtf8("continentNameEdit"))
        self.horizontalLayout_5.addWidget(self.continentNameEdit)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_4 = QtGui.QLabel(self.layoutWidget2)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_6.addWidget(self.label_4)
        self.continentBonusEdit = QtGui.QLineEdit(self.layoutWidget2)
        self.continentBonusEdit.setObjectName(_fromUtf8("continentBonusEdit"))
        self.horizontalLayout_6.addWidget(self.continentBonusEdit)
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.newContinentButton = QtGui.QPushButton(self.layoutWidget2)
        self.newContinentButton.setObjectName(_fromUtf8("newContinentButton"))
        self.verticalLayout_3.addWidget(self.newContinentButton)
        self.deleteContinentButton = QtGui.QPushButton(self.layoutWidget2)
        self.deleteContinentButton.setObjectName(_fromUtf8("deleteContinentButton"))
        self.verticalLayout_3.addWidget(self.deleteContinentButton)
        self.verticalLayout_5.addLayout(self.verticalLayout_3)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem1)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.addToContinentButton = QtGui.QPushButton(self.layoutWidget2)
        self.addToContinentButton.setObjectName(_fromUtf8("addToContinentButton"))
        self.verticalLayout_4.addWidget(self.addToContinentButton)
        self.removeFromContinentButton = QtGui.QPushButton(self.layoutWidget2)
        self.removeFromContinentButton.setObjectName(_fromUtf8("removeFromContinentButton"))
        self.verticalLayout_4.addWidget(self.removeFromContinentButton)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        self.tabWidget.addTab(self.continentTab, _fromUtf8(""))
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1600, 21))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuFile = QtGui.QMenu(self.menuBar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtGui.QToolBar(MainWindow)
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuBar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QObject.connect(self.actionOpen, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.actionOpen)
        QtCore.QObject.connect(self.actionSave, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.actionSave)
        QtCore.QObject.connect(self.beginButton, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.beginRegion)
        QtCore.QObject.connect(self.endButton, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.endRegion)
        QtCore.QObject.connect(self.clearButton, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.clearRegion)
        QtCore.QObject.connect(self.tabWidget, QtCore.SIGNAL(_fromUtf8("currentChanged(int)")), MainWindow.tabChange)
        QtCore.QObject.connect(self.startLinkButton, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.startLinking)
        QtCore.QObject.connect(self.endLinkButton, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.endLinking)
        QtCore.QObject.connect(self.startRemoveButton, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.startRemoving)
        QtCore.QObject.connect(self.endRemoveButton, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.endRemoving)
        QtCore.QObject.connect(self.newContinentButton, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.createContinent)
        QtCore.QObject.connect(self.deleteContinentButton, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.deleteContinent)
        QtCore.QObject.connect(self.addToContinentButton, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.addRegionToContinent)
        QtCore.QObject.connect(self.removeFromContinentButton, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.removeRegionFromContinent)
        QtCore.QObject.connect(self.continentList, QtCore.SIGNAL(_fromUtf8("itemClicked(QListWidgetItem*)")), MainWindow.selectContinent)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "RegionName", None, QtGui.QApplication.UnicodeUTF8))
        self.beginButton.setText(QtGui.QApplication.translate("MainWindow", "Begin Area", None, QtGui.QApplication.UnicodeUTF8))
        self.endButton.setText(QtGui.QApplication.translate("MainWindow", "End Area", None, QtGui.QApplication.UnicodeUTF8))
        self.clearButton.setText(QtGui.QApplication.translate("MainWindow", "Clear", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.regionTab), QtGui.QApplication.translate("MainWindow", "Regions", None, QtGui.QApplication.UnicodeUTF8))
        self.startLinkButton.setText(QtGui.QApplication.translate("MainWindow", "Start Linking", None, QtGui.QApplication.UnicodeUTF8))
        self.endLinkButton.setText(QtGui.QApplication.translate("MainWindow", "End Linking", None, QtGui.QApplication.UnicodeUTF8))
        self.startRemoveButton.setText(QtGui.QApplication.translate("MainWindow", "Start Removing", None, QtGui.QApplication.UnicodeUTF8))
        self.endRemoveButton.setText(QtGui.QApplication.translate("MainWindow", "End Removing", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.neighbourTab), QtGui.QApplication.translate("MainWindow", "Neighbours", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Continent Name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Continent Bonus", None, QtGui.QApplication.UnicodeUTF8))
        self.newContinentButton.setText(QtGui.QApplication.translate("MainWindow", "New Continent", None, QtGui.QApplication.UnicodeUTF8))
        self.deleteContinentButton.setText(QtGui.QApplication.translate("MainWindow", "Delete Continent", None, QtGui.QApplication.UnicodeUTF8))
        self.addToContinentButton.setText(QtGui.QApplication.translate("MainWindow", "Add To Continent", None, QtGui.QApplication.UnicodeUTF8))
        self.removeFromContinentButton.setText(QtGui.QApplication.translate("MainWindow", "Remove From Continent", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.continentTab), QtGui.QApplication.translate("MainWindow", "Continents", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setText(QtGui.QApplication.translate("MainWindow", "Open", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setText(QtGui.QApplication.translate("MainWindow", "Save", None, QtGui.QApplication.UnicodeUTF8))

