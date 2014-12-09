'''
Created on 25/11/2014

@author: Juanito
'''

from PyQt4 import  QtCore, QtGui
from interfazPrincipal import Ui_ventanaPrincipal
import interfazPrincipal
import sys
from CinterfazNuevaVentana import interfazNuevaVentana

class interfazPrincipal(QtGui.QMainWindow, interfazPrincipal.Ui_ventanaPrincipal):
    def __init__(self, parent=None):
        super(interfazPrincipal, self).__init__(parent)
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
        self.connectActions()
    def nuevoProyecto(self):
        nueva=interfazNuevaVentana()
        nueva.exec_()
    
    def connectActions(self):
        self.actionNuevo_Proyecto.triggered.connect(self.nuevoProyecto)

def main():
    app = QtGui.QApplication(sys.argv)
    ventana=interfazPrincipal()
    ventana.show()
    sys.exit(app.exec_())
if __name__=='__main__':
    main()

