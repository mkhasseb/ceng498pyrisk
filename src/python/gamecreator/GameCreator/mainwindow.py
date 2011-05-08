# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Sat May  7 16:25:51 2011
#      by: PyQt4 UI code generator 4.8.3
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
        MainWindow.setEnabled(True)
        MainWindow.resize(833, 386)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.selectedMapLabel = QtGui.QLabel(self.centralWidget)
        self.selectedMapLabel.setGeometry(QtCore.QRect(170, 110, 111, 16))
        self.selectedMapLabel.setObjectName(_fromUtf8("selectedMapLabel"))
        self.startServerButton = QtGui.QPushButton(self.centralWidget)
        self.startServerButton.setGeometry(QtCore.QRect(243, 180, 141, 32))
        self.startServerButton.setObjectName(_fromUtf8("startServerButton"))
        self.label_2 = QtGui.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(30, 50, 62, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.portInput = QtGui.QLineEdit(self.centralWidget)
        self.portInput.setGeometry(QtCore.QRect(170, 50, 113, 22))
        self.portInput.setObjectName(_fromUtf8("portInput"))
        self.label_4 = QtGui.QLabel(self.centralWidget)
        self.label_4.setGeometry(QtCore.QRect(30, 110, 62, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_3 = QtGui.QLabel(self.centralWidget)
        self.label_3.setGeometry(QtCore.QRect(30, 80, 131, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.numPlayerInput = QtGui.QLineEdit(self.centralWidget)
        self.numPlayerInput.setGeometry(QtCore.QRect(170, 70, 113, 22))
        self.numPlayerInput.setObjectName(_fromUtf8("numPlayerInput"))
        self.label = QtGui.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(30, 20, 62, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.hostInput = QtGui.QLineEdit(self.centralWidget)
        self.hostInput.setGeometry(QtCore.QRect(170, 20, 113, 22))
        self.hostInput.setObjectName(_fromUtf8("hostInput"))
        self.logText = QtGui.QPlainTextEdit(self.centralWidget)
        self.logText.setEnabled(False)
        self.logText.setGeometry(QtCore.QRect(440, 20, 371, 231))
        self.logText.setObjectName(_fromUtf8("logText"))
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 833, 22))
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
        self.actionOpen_Map = QtGui.QAction(MainWindow)
        self.actionOpen_Map.setObjectName(_fromUtf8("actionOpen_Map"))
        self.menuFile.addAction(self.actionOpen_Map)
        self.menuBar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.startServerButton, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.startGameServer)
        QtCore.QObject.connect(self.actionOpen_Map, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.openMap)
        QtCore.QObject.connect(MainWindow, QtCore.SIGNAL(_fromUtf8("log(QString)")), self.logText.appendPlainText)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.selectedMapLabel.setText(QtGui.QApplication.translate("MainWindow", "No map selected", None, QtGui.QApplication.UnicodeUTF8))
        self.startServerButton.setText(QtGui.QApplication.translate("MainWindow", "Start Game Server", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Port", None, QtGui.QApplication.UnicodeUTF8))
        self.portInput.setText(QtGui.QApplication.translate("MainWindow", "8081", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Map", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Number Of Players", None, QtGui.QApplication.UnicodeUTF8))
        self.numPlayerInput.setText(QtGui.QApplication.translate("MainWindow", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Host", None, QtGui.QApplication.UnicodeUTF8))
        self.hostInput.setText(QtGui.QApplication.translate("MainWindow", "localhost", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen_Map.setText(QtGui.QApplication.translate("MainWindow", "Open Map", None, QtGui.QApplication.UnicodeUTF8))

