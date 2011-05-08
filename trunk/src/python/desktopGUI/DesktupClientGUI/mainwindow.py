# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Sat May  7 20:34:56 2011
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
        MainWindow.resize(1220, 939)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.mapView = QtGui.QGraphicsView(self.centralWidget)
        self.mapView.setGeometry(QtCore.QRect(10, 150, 761, 601))
        self.mapView.setObjectName(_fromUtf8("mapView"))
        self.passButton = QtGui.QPushButton(self.centralWidget)
        self.passButton.setEnabled(False)
        self.passButton.setGeometry(QtCore.QRect(800, 150, 114, 32))
        self.passButton.setObjectName(_fromUtf8("passButton"))
        self.gameLog = QtGui.QPlainTextEdit(self.centralWidget)
        self.gameLog.setGeometry(QtCore.QRect(810, 230, 341, 221))
        self.gameLog.setObjectName(_fromUtf8("gameLog"))
        self.label_2 = QtGui.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(810, 200, 71, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralWidget)
        self.label_3.setGeometry(QtCore.QRect(30, 70, 721, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(24)
        font.setItalic(True)
        font.setUnderline(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.cardList = QtGui.QListWidget(self.centralWidget)
        self.cardList.setGeometry(QtCore.QRect(810, 490, 341, 192))
        self.cardList.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.cardList.setObjectName(_fromUtf8("cardList"))
        self.label_4 = QtGui.QLabel(self.centralWidget)
        self.label_4.setGeometry(QtCore.QRect(810, 460, 62, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.tradeButton = QtGui.QPushButton(self.centralWidget)
        self.tradeButton.setGeometry(QtCore.QRect(1050, 690, 114, 32))
        self.tradeButton.setObjectName(_fromUtf8("tradeButton"))
        self.contList = QtGui.QListWidget(self.centralWidget)
        self.contList.setGeometry(QtCore.QRect(810, 30, 381, 101))
        self.contList.setObjectName(_fromUtf8("contList"))
        self.label_5 = QtGui.QLabel(self.centralWidget)
        self.label_5.setGeometry(QtCore.QRect(811, 10, 71, 20))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.stateLabel = QtGui.QLabel(self.centralWidget)
        self.stateLabel.setGeometry(QtCore.QRect(440, 20, 62, 16))
        self.stateLabel.setObjectName(_fromUtf8("stateLabel"))
        self.widget = QtGui.QWidget(self.centralWidget)
        self.widget.setGeometry(QtCore.QRect(20, 10, 369, 34))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.connectInput = QtGui.QLineEdit(self.widget)
        self.connectInput.setObjectName(_fromUtf8("connectInput"))
        self.horizontalLayout.addWidget(self.connectInput)
        self.connectButton = QtGui.QPushButton(self.widget)
        self.connectButton.setObjectName(_fromUtf8("connectButton"))
        self.horizontalLayout.addWidget(self.connectButton)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1220, 22))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtGui.QToolBar(MainWindow)
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.connectButton, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.connect)
        QtCore.QObject.connect(self.passButton, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.dopass)
        QtCore.QObject.connect(MainWindow, QtCore.SIGNAL(_fromUtf8("log(QString)")), self.gameLog.appendPlainText)
        QtCore.QObject.connect(MainWindow, QtCore.SIGNAL(_fromUtf8("loadImgSig()")), MainWindow.loadImgSlt)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.passButton.setText(QtGui.QApplication.translate("MainWindow", "Pass", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Game Log", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Cards", None, QtGui.QApplication.UnicodeUTF8))
        self.tradeButton.setText(QtGui.QApplication.translate("MainWindow", "Trade In", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "Continents", None, QtGui.QApplication.UnicodeUTF8))
        self.stateLabel.setText(QtGui.QApplication.translate("MainWindow", "State:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "<host>:<port>", None, QtGui.QApplication.UnicodeUTF8))
        self.connectInput.setText(QtGui.QApplication.translate("MainWindow", "localhost:8080", None, QtGui.QApplication.UnicodeUTF8))
        self.connectButton.setText(QtGui.QApplication.translate("MainWindow", "Connect", None, QtGui.QApplication.UnicodeUTF8))

