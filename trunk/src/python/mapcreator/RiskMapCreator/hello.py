# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hello.ui'
#
# Created: Tue Apr 12 12:18:11 2011
#      by: PyQt4 UI code generator 4.4.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(362, 244)
        Dialog.setAutoFillBackground(False)
        self.verticalLayout_2 = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.header = QtGui.QLabel(Dialog)
        self.header.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(23)
        font.setWeight(75)
        font.setBold(True)
        self.header.setFont(font)
        self.header.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.header.setObjectName("header")
        self.verticalLayout.addWidget(self.header)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.nameEdit = QtGui.QLineEdit(Dialog)
        self.nameEdit.setObjectName("nameEdit")
        self.horizontalLayout.addWidget(self.nameEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.agespinBox = QtGui.QSpinBox(Dialog)
        self.agespinBox.setObjectName("agespinBox")
        self.horizontalLayout_2.addWidget(self.agespinBox)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.showname = QtGui.QLabel(Dialog)
        self.showname.setObjectName("showname")
        self.horizontalLayout_4.addWidget(self.showname)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.displayButton = QtGui.QPushButton(Dialog)
        self.displayButton.setObjectName("displayButton")
        self.horizontalLayout_4.addWidget(self.displayButton)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), self.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), self.reject)
        QtCore.QObject.connect(self.nameEdit, QtCore.SIGNAL("textChanged(QString)"), self.showname.setText)
        QtCore.QObject.connect(self.displayButton, QtCore.SIGNAL("clicked()"), self.displayPressed)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def accept(self):
	print "Hello",self.nameEdit.text(),"your age is",\
		self.agespinBox.text(),"I will remember you"
	Dialog.close()

    def reject(self):
	print "bye",self.nameEdit.text(),"your age is",\
		self.agespinBox.text(),"I will forget you"
	Dialog.close()

    def displayPressed(self):
	print "Hello",self.nameEdit.text(),"your age is",\
		self.agespinBox.text()

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        Dialog.setToolTip(QtGui.QApplication.translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">hello is <span style=\" font-weight:600;\">hello</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.header.setToolTip(QtGui.QApplication.translate("Dialog", "hello is hello", None, QtGui.QApplication.UnicodeUTF8))
        self.header.setStyleSheet(QtGui.QApplication.translate("Dialog", "text-align:center", None, QtGui.QApplication.UnicodeUTF8))
        self.header.setText(QtGui.QApplication.translate("Dialog", "Hello", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "What is your name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "How old are you?", None, QtGui.QApplication.UnicodeUTF8))
        self.showname.setText(QtGui.QApplication.translate("Dialog", "?????????", None, QtGui.QApplication.UnicodeUTF8))
        self.displayButton.setText(QtGui.QApplication.translate("Dialog", "Display", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

