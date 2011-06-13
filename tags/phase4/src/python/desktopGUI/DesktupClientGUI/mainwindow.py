# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Sun May 15 19:14:13 2011
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1220, 939)
        MainWindow.setStyleSheet("QPushButton {\n"
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
"}")
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setStyleSheet("None")
        self.centralWidget.setObjectName("centralWidget")
        self.mapView = QtGui.QGraphicsView(self.centralWidget)
        self.mapView.setGeometry(QtCore.QRect(20, 250, 761, 501))
        self.mapView.setStyleSheet("color: rgb(255, 255, 255);")
        self.mapView.setObjectName("mapView")
        self.passButton = QtGui.QPushButton(self.centralWidget)
        self.passButton.setEnabled(False)
        self.passButton.setGeometry(QtCore.QRect(820, 180, 114, 32))
        self.passButton.setObjectName("passButton")
        self.label_3 = QtGui.QLabel(self.centralWidget)
        self.label_3.setGeometry(QtCore.QRect(20, 180, 751, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        font.setItalic(True)
        font.setUnderline(True)
        self.label_3.setFont(font)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.stateLabel = QtGui.QLabel(self.centralWidget)
        self.stateLabel.setGeometry(QtCore.QRect(20, 60, 361, 31))
        self.stateLabel.setObjectName("stateLabel")
        self.playerLabel = QtGui.QLabel(self.centralWidget)
        self.playerLabel.setGeometry(QtCore.QRect(410, 10, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.playerLabel.setFont(font)
        self.playerLabel.setText("")
        self.playerLabel.setObjectName("playerLabel")
        self.playerView = QtGui.QGraphicsView(self.centralWidget)
        self.playerView.setGeometry(QtCore.QRect(540, 10, 51, 41))
        self.playerView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.playerView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.playerView.setObjectName("playerView")
        self.missionLabel = QtGui.QLabel(self.centralWidget)
        self.missionLabel.setGeometry(QtCore.QRect(400, 60, 361, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(True)
        self.missionLabel.setFont(font)
        self.missionLabel.setLineWidth(1)
        self.missionLabel.setWordWrap(True)
        self.missionLabel.setObjectName("missionLabel")
        self.layoutWidget = QtGui.QWidget(self.centralWidget)
        self.layoutWidget.setGeometry(QtCore.QRect(820, 220, 258, 227))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.gameLog = QtGui.QPlainTextEdit(self.layoutWidget)
        self.gameLog.setObjectName("gameLog")
        self.verticalLayout.addWidget(self.gameLog)
        self.layoutWidget1 = QtGui.QWidget(self.centralWidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(790, 10, 351, 161))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_5 = QtGui.QLabel(self.layoutWidget1)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_5.addWidget(self.label_5)
        self.contList = QtGui.QListWidget(self.layoutWidget1)
        self.contList.setObjectName("contList")
        self.verticalLayout_5.addWidget(self.contList)
        self.label_4 = QtGui.QLabel(self.centralWidget)
        self.label_4.setGeometry(QtCore.QRect(820, 460, 261, 31))
        self.label_4.setObjectName("label_4")
        self.cardList = QtGui.QListWidget(self.centralWidget)
        self.cardList.setEnabled(True)
        self.cardList.setGeometry(QtCore.QRect(820, 490, 256, 192))
        self.cardList.setMinimumSize(QtCore.QSize(256, 192))
        self.cardList.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.cardList.setObjectName("cardList")
        self.label = QtGui.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(21, 11, 124, 31))
        self.label.setObjectName("label")
        self.connectInput = QtGui.QLineEdit(self.centralWidget)
        self.connectInput.setGeometry(QtCore.QRect(151, 11, 137, 33))
        self.connectInput.setObjectName("connectInput")
        self.connectButton = QtGui.QPushButton(self.centralWidget)
        self.connectButton.setEnabled(True)
        self.connectButton.setGeometry(QtCore.QRect(294, 12, 94, 31))
        self.connectButton.setStyleSheet("None")
        self.connectButton.setObjectName("connectButton")
        self.tradeButton = QtGui.QPushButton(self.centralWidget)
        self.tradeButton.setEnabled(False)
        self.tradeButton.setGeometry(QtCore.QRect(985, 691, 94, 31))
        self.tradeButton.setObjectName("tradeButton")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1220, 23))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtGui.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.ToolBarArea(QtCore.Qt.TopToolBarArea), self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.connectButton, QtCore.SIGNAL("clicked()"), MainWindow.connect)
        QtCore.QObject.connect(self.passButton, QtCore.SIGNAL("clicked()"), MainWindow.dopass)
        QtCore.QObject.connect(MainWindow, QtCore.SIGNAL("log(QString)"), self.gameLog.appendPlainText)
        QtCore.QObject.connect(MainWindow, QtCore.SIGNAL("loadImgSig()"), MainWindow.loadImgSlt)
        QtCore.QObject.connect(MainWindow, QtCore.SIGNAL("signalDefendPopup(QString)"), MainWindow.slotDefendPopup)
        QtCore.QObject.connect(MainWindow, QtCore.SIGNAL("signalTransferPopup()"), MainWindow.slotTransferPopup)
        QtCore.QObject.connect(self.tradeButton, QtCore.SIGNAL("clicked()"), MainWindow.slotTradeIn)
        QtCore.QObject.connect(MainWindow, QtCore.SIGNAL("signalPlayerName(QString)"), MainWindow.slotPlayerName)
        QtCore.QObject.connect(MainWindow, QtCore.SIGNAL("signalMission(QString)"), MainWindow.slotMission)
        QtCore.QObject.connect(MainWindow, QtCore.SIGNAL("signalVictor(QString)"), MainWindow.slotVictor)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.passButton.setText(QtGui.QApplication.translate("MainWindow", "Pass", None, QtGui.QApplication.UnicodeUTF8))
        self.stateLabel.setText(QtGui.QApplication.translate("MainWindow", "State:", None, QtGui.QApplication.UnicodeUTF8))
        self.missionLabel.setText(QtGui.QApplication.translate("MainWindow", "Mission: ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Game Log", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "Continents", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Cards", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "<host>:<port>", None, QtGui.QApplication.UnicodeUTF8))
        self.connectInput.setText(QtGui.QApplication.translate("MainWindow", "localhost:8080", None, QtGui.QApplication.UnicodeUTF8))
        self.connectButton.setText(QtGui.QApplication.translate("MainWindow", "Connect", None, QtGui.QApplication.UnicodeUTF8))
        self.tradeButton.setText(QtGui.QApplication.translate("MainWindow", "Trade In", None, QtGui.QApplication.UnicodeUTF8))

