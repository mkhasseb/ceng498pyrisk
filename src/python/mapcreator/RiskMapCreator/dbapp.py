#!/usr/bin/python
from PyQt4 import QtCore, QtGui
from mapcreator.RiskMapCreator.dbdia import Ui_Dialog
import sqlite3

class DBapp(QtGui.QDialog):
   def __init__(self,dbname,parent=None):
	QtGui.QDialog.__init__(self,parent)
	self.ui = Ui_Dialog()
	self.ui.setupUi(self)
	print "connecting",dbname
	self.db = sqlite3.connect(dbname)
	# done in designer so commented out
	#QtCore.QObject.connect(self.ui.insertButton, 
		#QtCore.SIGNAL("clicked()"), self.insertitem)
	#QtCore.QObject.connect(self.ui.searchButton, 
		#QtCore.SIGNAL("clicked()"), self.searchitem)
	self.ui.status.setText('')

   def insertitem(self):
	(a,b,c)=(str(self.ui.username.text()), str(self.ui.fullname.text()),
			 str(self.ui.password.text()))
	print "inserting ", a,b,c
	try:
		self.db.execute("""insert into user values (?,?,?)""",
				(a,b,c))
		self.ui.status.setText("Insertion successful")
	except sqlite3.Error, e:
		self.ui.status.setText("DB error: " + e.args[0])
	self.db.commit()
   def searchitem(self):
	a = str(self.ui.searchEdit.text())
	print "searching for username ",a
	c = self.db.cursor()
	try:
		c.execute("""select * from user where username like ?;""",
				('%'+a+'%',))
	except sqlite3.Error, e:
		self.ui.status.setText("DB error: " + e.args[0])
		return
	self.ui.username.setText('')
	self.ui.fullname.setText('')
	self.ui.password.setText('')
	for row in c:
		self.ui.username.setText(row[0])
		self.ui.fullname.setText(row[1])
		self.ui.password.setText(row[2])
		print row
	

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = DBapp('test.db')        #QtGui.QDialog()
    #ui = Ui_Dialog()
    #ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

