'''
Created on 27/11/2014

@author: Juanito
'''

from PyQt4 import QtCore, QtGui
import interfazSecundaria
import sys

class interfazSecundaria(QtGui.QDialog, interfazSecundaria.Ui_FormSecund):
    def __init__(self, parent=None):
        super(interfazSecundaria, self).__init__(parent)
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
        self.connectActions()
    def connectActions(self):
        
        pass
def main():
    app = QtGui.QApplication(sys.argv)
    ventana=interfazSecundaria()
    ventana.show()
    sys.exit(app.exec_())
if __name__=='__main__':
    main()