# -*- coding: utf-8 -*-

import sys
import os
from PyQt4 import QtGui,QtCore, uic
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import lepl.apps.rfc3696
from  Personal import *

email_validator = lepl.apps.rfc3696.Email()
estilo = open('./Ventanas/st.stylesheet','r').read()
login = uic.loadUiType('./Ventanas/login.ui')[0]
personal = uic.loadUiType('./Ventanas/personal.ui')[0]
semillero = uic.loadUiType('./Ventanas/semillero.ui')[0]
ptaPrincipal = uic.loadUiType('./Ventanas/principal.ui')[0]
ninos = uic.loadUiType('./Ventanas/ninos.ui')[0]
representante = uic.loadUiType('./Ventanas/representante.ui')[0]
#consultar = uic.loadUiType('consultar.ui')[0]
#base = uic.loadUiType('base.ui')[0]

class Login(QtGui.QDialog, login):
    #conexion = Conexion()
    def __init__(self,parent=None):
        QtGui.QDialog.__init__(self,parent)
        self.setupUi(self)
        self.quitarVentana()
        self.button_exit.clicked.connect(self.destroy)
        self.button_Login.clicked.connect(self.login_act)
        #screen = QtGui.QDesktopWidget().screenGeometry()
        #size = self.geometry()
        #self.move((screen.width() - size.width())/2, (screen.height() - size.height())/2)
        
	#   
    #def exit(self):
     #   os.system(cmd)
	#QtCore.QCoreApplication.instance().quit
	#self.close()
    
    #def closeEvent(self, event):
        #print "Closing"
        #self.destroy() 
    
    def showPrincipal(self):
        #self.quit
        #self.instance().quit()
	#app = QtGui.QApplication(sys.argv)
        #self.quit()
	#principal = Principal()
        #principal.show()
        #self.setupUi(principal)
	#sys.exit(app.exec_())  
	pass


    
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            #super(LoginDialog, self).keyPressEvent(event)
	    	print 'escape'

    def quitarVentana(self):
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)



    def login_act(self):
        name = str(self.input_username.text())
        pwd = str(self.input_password.text())
        #query = ('SELECT COUNT(*) FROM proyecto_laboratorio.Cuenta WHERE cuenta_nick= %s AND cuenta_pwd = %s')
        #conexion = self.conexion.getConnection()
        #cursor= conexion.cursor()
        #cursor.execute(query,(name,pwd))
        #result=cursor.fetchone()
        print name + pwd     
        self.accept()
        #sys.exit(login.close())
	#if result[0]>0:
           # self.accept()
        #else:
        #QtGui.QMessageBox.warning(self, 'Error', 'Usuario o contrasena equivocadas', QtGui.QMessageBox.Ok)
        #cursor.close()
        
class Principal(QtGui.QMainWindow, ptaPrincipal):
    def __init__(self,parent=None):
        QtGui.QMainWindow.__init__(self,parent)
        self.setupUi(self)
        screen = QtGui.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width())/2, (screen.height() - size.height())/2)
        self.inicializar()
	
    def inicializar(self):
        self.setStyleSheet(estilo )
        self.btnPersonal.clicked.connect(self.irPersonal)
        self.btnSemillero.clicked.connect(self.irSemillero)
        #self.btnContabilidad.clicked.connect(self.irContabilidad)
        	
    def irPersonal(self):
        personal=PantallaPersonal()
        personal.exec_()
		 
    def irSemillero(self):
        semillero=PantallaSemillero()
        semillero.exec_()

    #def irContabilidad(self):
        #ptaContabilidad=PantallaContabilidad()
        #ptaContabilidad.exec_()
	 
class PantallaPersonal(QtGui.QDialog, personal):
    tmp_name = ''
    tmp_lastname = ''
    tmp_cedula = ''
    tmp_telefono = ''
    personales = []
    personal = Personal()

    def __init__(self,parent=None):
       QtGui.QDialog.__init__(self, parent)
       self.setupUi(self)
       self.inicializar()
       
    def inicializar(self):
        self.setStyleSheet(estilo )
        self.txt_nombre.textChanged.connect(lambda: self.onlyText('nombre,' + self.txt_nombre.text()))
        self.txt_apellido.textChanged.connect(lambda: self.onlyText('apellido,' + self.txt_apellido.text()))
        self.txt_cedula.textChanged.connect(lambda: self.onlyDigit('cedula,' + self.txt_cedula.text()))
        self.txt_telefono.textChanged.connect(lambda: self.onlyDigit('telefono,' + self.txt_telefono.text()))
        self.txt_correo.editingFinished.connect(self.checkMail)
        self.btn_guardar.clicked.connect(self.guardar)
        self.btn_limpiar.clicked.connect(self.limpiar)
        self.btn_eliminar_selec.clicked.connect(self.borrarSelec)
        self.btn_eliminar_todo.clicked.connect(self.borrarTodo)
        self.btn_buscar.clicked.connect(self.buscar)
        self.tb_personal.doubleClicked.connect(self.elegir_dobleclick)
        self.cargarPersonal()

    def checkMail(self):
		if not email_validator(str(self.txt_correo.text())):
			QMessageBox.about(self,"ERROR","Ingresar un correo valido")
			return True
		else: False


    def guardar(self):
        if self.checkMail():
            QMessageBox.about(self,"ERROR","Ingresar un correo valido")
        else:
			self.personal.nombre = str(self.txt_nombre.text())
			self.personal.apellido = str(self.txt_apellido.text())
			self.personal.cedula = str(self.txt_cedula.text())
			self.personal.direccion = str(self.txt_direccion.text())
			self.personal.telefono = str(self.txt_telefono.text())
			self.personal.correo = str(self.txt_correo.text())
			self.personal.tipo = str(self.cmb_tipo.currentText())
			self.personal.carrera = str(self.txt_carrera.text())
			self.personal.sexo = str(self.cmb_sexo.currentText())
			self.personal.carrera = str(self.txt_carrera.text())
			self.personal.facultad = str(self.txt_facultad.text())
			self.personal.guardar()
 			self.cargarPersonal()
			self.limpiar()
			QMessageBox.about(self,"Correcto","Cliente guardado con exito")


    
    def limpiar(self):
        self.personal.id=0
        self.txt_nombre.setText('')
        self.txt_apellido.setText('')
        self.txt_cedula.setText('')
        self.txt_direccion.setText('')
        self.txt_telefono.setText('')
        self.txt_correo.setText('')
        self.txt_carrera.setText('')
        self.txt_facultad.setText('')
        

        
    def onlyText(self,texto):
		try:
			text = str(texto.split(',')[1])
			name = str(texto.split(',')[0])
			
			if text != '':
				
				if not ((text.replace(' ','')).isalpha()):
					QMessageBox.about(self,"ERROR","Caracter no valido")
					if name == 'nombre':
						self.txt_nombre.setText(self.tmp_name)
					elif name == 'apellido':
						self.txt_apellido.setText(self.tmp_lastname)
				else:
					
					if len(text) == 1:
						self.tmp_name = ''
						self.tmp_lastname = ''
					else:
						if name == 'nombre':
							self.tmp_name = text
						elif name == 'apellido':
							self.tmp_lastname = text

		except:
			name = str(texto.split(',')[0])
			QMessageBox.about(self,"ERROR","Caracter ASCII no valido")
								
			if name == 'nombre':
				self.tmp_name=''
				self.txt_nombre.setText('')
			elif name == 'apellido':
				self.tmp_lastname=''
				self.txt_apellido.setText('')

    
    def onlyDigit(self,texto):
		try:
			number = str(texto.split(',')[1])
			name = str(texto.split(',')[0])

			if number != '':
				if not ((number.replace(' ','')).isdigit()):
					QMessageBox.about(self,"ERROR","Ingresar solo digitos")
					if name == 'cedula':
						self.txt_cedula.setText(self.tmp_cedula)
					elif name == 'telefono':
						self.txt_telefono.setText(self.tmp_telefono)

				else:
					if len(number) == 1:
						self.tmp_cedula = ''
						self.tmp_telefono = ''
					else:
						if name == 'cedula':
							self.tmp_cedula = number
						elif name == 'telefono':
							self.tmp_telefono = number
		
		except:
			name = str(texto.split(',')[0])
			QMessageBox.about(self,"ERROR","Ingresar solo digitos")
											
			if name == 'cedula':
				self.tmp_cedula=''
				self.txt_cedula.setText('')
			elif name == 'telefono':
				self.tmp_telefono=''
				self.txt_telefono.setText('')

    def cargarPersonal(self,atribute=None, name=None):
        self.personales = []
        busq =[]
        model = QStandardItemModel()
        model.setColumnCount(10)
        model.setHorizontalHeaderLabels(self.personal.headernames)
        if (atribute is not None) and (name is not None):
            if name == 'nombre' or name == 'apellido' or name == 'cedula':
                busq = self.personal.consultar_By_Atribute(atribute,name)
            else:
                busq = []
        else :
            busq =self.personal.consultar_todos()
        
        
        for p in busq:

            tmp=[p.id,p.nombre,p.apellido,p.cedula,p.telefono,p.tipo,p.direccion,p.sexo,p.correo,p.carrera,p.facultad]

            li = [p.nombre,p.apellido, p.cedula,p.telefono,p.tipo,p.direccion,p.sexo,p.correo,p.carrera,p.facultad]
            self.personales.append(tmp)
            row = []
            for nam in li:
                item = QStandardItem(str(nam))
                item.setEditable(False)
                row.append(item)
            
            model.appendRow(row)
        self.tb_personal.setModel(model)
        self.tb_personal_eliminar.setModel(model)

    def elegir_dobleclick(self):
        selected = self.tb_personal.selectedIndexes()
        selected_index = selected.__getitem__(0)
        select = self.personales[selected_index.row()]
        self.tabWidget.setCurrentWidget(self.tab_1)
        self.personal.id = select[0]
        self.txt_nombre.setText(select[1])
        self.txt_apellido.setText(select[2])
        #print select[3]
        #print select[4]
        self.txt_cedula.setText(str(select[3]))
        self.txt_direccion.setText(str(select[6]))
        self.txt_telefono.setText(str(select[4]))
        self.txt_correo.setText(select[8])
        self.cmb_tipo.setCurrentIndex(self.cmb_tipo.findText(select[5]))
        self.cmb_sexo.setCurrentIndex(self.cmb_sexo.findText(select[7]))
        self.txt_carrera.setText(str(select[9]))
        self.txt_facultad.setText(str(select[10]))

    def borrarTodo(self):
        try:
            rst=QMessageBox.warning(self,"Alerta","Esta seguro que desea eliminar", QMessageBox.Cancel, QMessageBox.Ok)
            if rst == QMessageBox.Ok:
                self.personal.borrarPersonales()
                QMessageBox.about(self,"Correcto", "Se ha eliminado todo el personal")
        except:
            QMessageBox.about(self,"Error", "Problemas con la base de datos")
        self.cargarPersonal()

    def borrarSelec(self):
        try:
            selected = self.tb_personal_eliminar.selectedIndexes()
            selected_index = selected.__getitem__(0)
            select = self.personales[selected_index.row()]
            self.personal.id = select[0]

            rst=QMessageBox.warning(self,"Alerta","Esta seguro que desea eliminar", QMessageBox.Cancel, QMessageBox.Ok)
            if rst == QMessageBox.Ok:
                self.personal.borrarPersonal()
                QMessageBox.about(self,"Correcto", "Se ha eliminado al Cliente")
        except:
            QMessageBox.about(self,"Error", "Problemas con la base de datos")
        self.cargarPersonal()

    def buscar(self):
        atribute= (str(self.txt_buscar.text())).strip()
        name=''
        print atribute
        if atribute != '':
            if self.radioButton_nombre.isChecked():
                name= 'nombre'
                print 'nombre = entro'
                self.cargarPersonal(atribute,name)
            elif self.radioButton_apellido.isChecked():
                name= 'apellido'
                self.cargarPersonal(atribute,name)
            elif self.radioButton_cedula.isChecked():
                name= 'cedula'
                self.cargarPersonal(atribute,name)
            else:
                self.cargarPersonal()
        else:
            self.cargarPersonal()

		

class PantallaSemillero(QtGui.QDialog, semillero):
    
	select = ''
	def __init__(self,parent=None):
		QtGui.QDialog.__init__(self, parent)
		self.setupUi(self)
		self.inicializar()
       
	def inicializar(self):
		self.setStyleSheet(estilo )
		self.btn_ninos.connect(self.irNino)
		#self.btn_image.setStyleShett()
		#self.btn_imagen.connect(self.irSearchFile)

	#def irSearchFile(self):
		# search_file = PantallaSearchFile()
		#search_file.exec_()
		#print search_file.filePath

	def irNino(self):
		nino= PantallaNino()
		nino.exec_()


class PantallaNino(QtGui.QDialog, ninos):

	def __init__(self,parent=None):
		QtGui.QDialog.__init__(self,parent)
		self.setupUi(self)

	def irRepresentante(self):
		representante = PantallaRepresentante()
		representante.exec_()

class PantallaRepresentante(QtGui.QDialog, representante):

	def __init__(self,parent=None):
		QtGui.QDialog.__init__(self,parent)
		self.setupUi(self)	




if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    #if 
    log = Login()
    
    if log.exec_() == QtGui.QDialog.Accepted:
        print 'holiwis'
    	#log.close()
        principal = Principal()
        principal.show()
    
    sys.exit(app.exec_()) 
    sys.exit(log.close())
