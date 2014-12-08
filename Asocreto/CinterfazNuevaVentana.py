'''
Created on 25/11/2014

@author: Juanito
'''

from PyQt4 import QtCore, QtGui
import interfazNuevaVentana
import psycopg2
import sys

from CinterfazSecundaria import interfazSecundaria

class interfazNuevaVentana(QtGui.QDialog, interfazNuevaVentana.Ui_Dialog):
    def __init__(self, parent=None):
        super(interfazNuevaVentana, self).__init__(parent)
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
        self.connectActions()
          
    
    #Metodos para invocar nueva pantalla merianteboton
    def nuevoProyecto2(self):
        nueva=interfazSecundaria()
        nueva.exec_()
    
    def connectActions(self):
        
        self.buttonIniciar.clicked.connect(self.nuevoProyecto2)
                 
    #Metodo para hacer una consulta a la BD, convertirlo en un arreglo y adicionar los items a un combobox
        
        self.llenarComboCategoria()#declaro antes la funcion
        self.llenarComboNorma()#declaro antes la funcion
        
    def llenarComboCategoria(self):

        con = psycopg2.connect(database='asocreto', user='postgres', password= 'dsa') 
        cur = con.cursor()
        cur.execute('SELECT nombrecategoria from categoria')          
        registro  = cur.fetchall()
        r1 = [row[0] for row in registro]
        cur.close()
        
        for i in range(len(r1)):
            categoria = self.palabras(r1[i])
            self.cboxCategoria.addItem(categoria)
            print categoria    
    
    #Metodo para tomar la seleccion del cboxCategoria       
        self.cboxCategoria.activated[str].connect(self.onActivated)
    def palabras(self, text):
        seleccion = ""
        for i in range(len(text)):
            if text[i] != " ":
                seleccion += text[i]
        return seleccion
    
    def onActivated(self, text):
        seleccion = text
        
    #Metodo para hacer una consulta a la BD, convertirlo en un arreglo y adicionar los items a un combobox
        
        
        
    def llenarComboNorma(self):

        con = psycopg2.connect(database='asocreto', user='postgres', password= 'dsa') 
        cur = con.cursor()
        cur.execute('SELECT nombrenorma from norma')          
        registro2  = cur.fetchall()
        r2 = [row[0] for row in registro2]
        cur.close()
        
        for i in range(len(r2)):
            norma = self.palabras(r2[i])
            self.cboxNorma.addItem(norma)
            print norma    
    
    #Metodo para tomar la seleccion del cboxCategoria       
        self.cboxNorma.activated[str].connect(self.onActivated)
    def palabras2(self, text):
        seleccion2 = ""
        for i in range(len(text)):
            if text[i] != " ":
                seleccion2 += text[i]
        return seleccion2
    
    def onActivated2(self, text):
        seleccion2 = text
        
       
        
def main():
    app = QtGui.QApplication(sys.argv)
    ventana=interfazNuevaVentana()
    ventana.show()
    sys.exit(app.exec_())
if __name__=='__main__':
    main()