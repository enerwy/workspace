from PyQt4 import  QtCore, QtGui
from prueba import Ui_MainWindow
import prueba
import sys
import psycopg2
from array import array

class prueba(QtGui.QMainWindow, prueba.Ui_MainWindow):
    def __init__(self, parent=None):
        super(prueba, self).__init__(parent)
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
        self.lbl = QtGui.QLabel("", self)
    
        self.llenarCombo()#declaro antes la funcion

    def llenarCombo(self):

        con = psycopg2.connect(database='asocreto', user='postgres', password= 'dsa') 
        cur = con.cursor()
        cur.execute('SELECT nombrecategoria from categoria')          
        registro  = cur.fetchall()
        print registro
        r1 = [row[0] for row in registro]
        print r1
        cur.close()
        for i in range(len(r1)):
            self.comboBox.addItem(r1[i])
        
    #Metodo para tomar la seleccion del combobox        
        self.comboBox.activated[str].connect(self.onActivated)
    def onActivated(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()
        seleccion= text  
        print seleccion      

def main():
    app = QtGui.QApplication(sys.argv)
    ventana=prueba()
    ventana.show()
    sys.exit(app.exec_())
if __name__=='__main__':
    main()