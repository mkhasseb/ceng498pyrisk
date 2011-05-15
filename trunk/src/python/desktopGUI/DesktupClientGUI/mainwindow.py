# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Sun May 15 18:40:23 2011
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
        MainWindow.setEnabled(True)
        MainWindow.resize(1220, 939)
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
        self.centralWidget.setStyleSheet(_fromUtf8(""))
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.mapView = QtGui.QGraphicsView(self.centralWidget)
        self.mapView.setGeometry(QtCore.QRect(20, 250, 761, 601))
        self.mapView.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.mapView.setObjectName(_fromUtf8("mapView"))
        self.passButton = QtGui.QPushButton(self.centralWidget)
        self.passButton.setEnabled(True)
        self.passButton.setGeometry(QtCore.QRect(830, 250, 114, 32))
        self.passButton.setObjectName(_fromUtf8("passButton"))
        self.label_3 = QtGui.QLabel(self.centralWidget)
        self.label_3.setGeometry(QtCore.QRect(20, 180, 751, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(24)
        font.setItalic(True)
        font.setUnderline(True)
        self.label_3.setFont(font)
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.stateLabel = QtGui.QLabel(self.centralWidget)
        self.stateLabel.setGeometry(QtCore.QRect(20, 60, 361, 31))
        self.stateLabel.setObjectName(_fromUtf8("stateLabel"))
        self.layoutWidget = QtGui.QWidget(self.centralWidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 10, 369, 34))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.connectInput = QtGui.QLineEdit(self.layoutWidget)
        self.connectInput.setObjectName(_fromUtf8("connectInput"))
        self.horizontalLayout.addWidget(self.connectInput)
        self.connectButton = QtGui.QPushButton(self.layoutWidget)
        self.connectButton.setEnabled(True)
        self.connectButton.setStyleSheet(_fromUtf8(""))
        self.connectButton.setObjectName(_fromUtf8("connectButton"))
        self.horizontalLayout.addWidget(self.connectButton)
        self.playerLabel = QtGui.QLabel(self.centralWidget)
        self.playerLabel.setGeometry(QtCore.QRect(410, 10, 131, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(20)
        self.playerLabel.setFont(font)
        self.playerLabel.setText(_fromUtf8(""))
        self.playerLabel.setObjectName(_fromUtf8("playerLabel"))
        self.playerView = QtGui.QGraphicsView(self.centralWidget)
        self.playerView.setGeometry(QtCore.QRect(540, 10, 51, 41))
        self.playerView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.playerView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.playerView.setObjectName(_fromUtf8("playerView"))
        self.missionLabel = QtGui.QLabel(self.centralWidget)
        self.missionLabel.setGeometry(QtCore.QRect(400, 60, 361, 71))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(9)
        font.setItalic(True)
        self.missionLabel.setFont(font)
        self.missionLabel.setLineWidth(1)
        self.missionLabel.setWordWrap(True)
        self.missionLabel.setObjectName(_fromUtf8("missionLabel"))
        self.widget = QtGui.QWidget(self.centralWidget)
        self.widget.setGeometry(QtCore.QRect(820, 560, 262, 266))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout_4.setMargin(0)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_4 = QtGui.QLabel(self.widget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_2.addWidget(self.label_4)
        self.cardList = QtGui.QListWidget(self.widget)
        self.cardList.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.cardList.setObjectName(_fromUtf8("cardList"))
        self.verticalLayout_2.addWidget(self.cardList)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem = QtGui.QSpacerItem(108, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.tradeButton = QtGui.QPushButton(self.widget)
        self.tradeButton.setEnabled(False)
        self.tradeButton.setObjectName(_fromUtf8("tradeButton"))
        self.horizontalLayout_2.addWidget(self.tradeButton)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.widget1 = QtGui.QWidget(self.centralWidget)
        self.widget1.setGeometry(QtCore.QRect(820, 320, 258, 227))
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget1)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_2 = QtGui.QLabel(self.widget1)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.gameLog = QtGui.QPlainTextEdit(self.widget1)
        self.gameLog.setObjectName(_fromUtf8("gameLog"))
        self.verticalLayout.addWidget(self.gameLog)
        self.widget2 = QtGui.QWidget(self.centralWidget)
        self.widget2.setGeometry(QtCore.QRect(820, 70, 351, 161))
        self.widget2.setObjectName(_fromUtf8("widget2"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.widget2)
        self.verticalLayout_5.setMargin(0)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.label_5 = QtGui.QLabel(self.widget2)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout_5.addWidget(self.label_5)
        self.contList = QtGui.QListWidget(self.widget2)
        self.contList.setObjectName(_fromUtf8("contList"))
        self.verticalLayout_5.addWidget(self.contList)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1220, 21))
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
        QtCore.QObject.connect(MainWindow, QtCore.SIGNAL(_fromUtf8("signalDefendPopup(QString)")), MainWindow.slotDefendPopup)
        QtCore.QObject.connect(MainWindow, QtCore.SIGNAL(_fromUtf8("signalTransferPopup()")), MainWindow.slotTransferPopup)
        QtCore.QObject.connect(self.tradeButton, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.slotTradeIn)
        QtCore.QObject.connect(MainWindow, QtCore.SIGNAL(_fromUtf8("signalPlayerName(QString)")), MainWindow.slotPlayerName)
        QtCore.QObject.connect(MainWindow, QtCore.SIGNAL(_fromUtf8("signalMission(QString)")), MainWindow.slotMission)
        QtCore.QObject.connect(MainWindow, QtCore.SIGNAL(_fromUtf8("signalVictor(QString)")), MainWindow.slotVictor)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.passButton.setText(QtGui.QApplication.translate("MainWindow", "Pass", None, QtGui.QApplication.UnicodeUTF8))
        self.stateLabel.setText(QtGui.QApplication.translate("MainWindow", "State:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "<host>:<port>", None, QtGui.QApplication.UnicodeUTF8))
        self.connectInput.setText(QtGui.QApplication.translate("MainWindow", "localhost:8080", None, QtGui.QApplication.UnicodeUTF8))
        self.connectButton.setText(QtGui.QApplication.translate("MainWindow", "Connect", None, QtGui.QApplication.UnicodeUTF8))
        self.missionLabel.setText(QtGui.QApplication.translate("MainWindow", "Mission: ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Cards", None, QtGui.QApplication.UnicodeUTF8))
        self.tradeButton.setText(QtGui.QApplication.translate("MainWindow", "Trade In", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Game Log", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "Continents", None, QtGui.QApplication.UnicodeUTF8))

