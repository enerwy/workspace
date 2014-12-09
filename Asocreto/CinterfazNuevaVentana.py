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
        self.seleccion=""
        self.seleccion2=""  
    
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
            try:
                if text[i] != " "  or text[i+1] != " ":
                    seleccion += text[i]
            except IndexError:
                pass 
        return seleccion
    
    def onActivated(self, text):
        self.seleccion = text
        
        
        
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
    
    #Metodo para tomar la seleccion del cboxNorma      
        self.cboxNorma.activated[str].connect(self.onActivated2)
        
    def onActivated2(self, text):
        self.seleccion2 = text
        
        self.llenarComboExperimento()#declaro antes la funcion
        
     #Metodo para hacer una consulta a la BD, convertirlo en un arreglo y adicionar los items a un combobox       
    def llenarComboExperimento(self):
        self.cboxExp.clear()
        con = psycopg2.connect(database='asocreto', user='postgres', password= 'dsa') 
        cur = con.cursor()
        self.seleccion=str(self.seleccion)
        self.seleccion2=str(self.seleccion2)
        print "SELECT nombreexperimento FROM experimento WHERE idcategoria=(SELECT idcategoria FROM categoria WHERE nombrecategoria = '"+self.seleccion+"') AND idnorma=(SELECT idnorma FROM norma WHERE nombrenorma = '"+self.seleccion2+"')"
        cur.execute("SELECT nombreexperimento FROM experimento WHERE idcategoria=(SELECT idcategoria FROM categoria WHERE nombrecategoria = '"+self.seleccion+"') AND idnorma=(SELECT idnorma FROM norma WHERE nombrenorma = '"+self.seleccion2+"')")          
        registro3  = cur.fetchall()
        print registro3
        r3 = [row[0] for row in registro3]
        print r3
        cur.close()
        
        for i in range(len(r3)):
            experimento = self.palabras(r3[i])
            self.cboxExp.addItem(experimento)
            print experimento 
    
    #Metodo para tomar la seleccion del cboxExpe       
        self.cboxExp.activated[str].connect(self.onActivated3)
    
    
    def onActivated3(self, text):
        seleccion3 = text
       
def main():
    app = QtGui.QApplication(sys.argv)
    ventana=interfazNuevaVentana()
    ventana.show()
    sys.exit(app.exec_())
if __name__=='__main__':
    main()