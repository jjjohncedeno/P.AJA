# -*- coding: utf-8 -*-

import sys
import os
from PyQt4 import QtGui,QtCore, uic
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import lepl.apps.rfc3696
from  Personal import *
from Juego import *
from Nino import *
from Semillero import *
from Representante import *
from Compras import *
from Ventas import *
from Conexion import *
from Oficio import *
#from Semillero import *

email_validator = lepl.apps.rfc3696.Email()
estilo = open('./Ventanas/st.stylesheet','r').read()
login = uic.loadUiType('./Ventanas/login.ui')[0]
personal = uic.loadUiType('./Ventanas/personal.ui')[0]
semillero = uic.loadUiType('./Ventanas/semillero.ui')[0]
ptaPrincipal = uic.loadUiType('./Ventanas/principal.ui')[0]
ninos = uic.loadUiType('./Ventanas/ninos.ui')[0]
representante = uic.loadUiType('./Ventanas/representante.ui')[0]
oficio = uic.loadUiType('./Ventanas/oficio.ui')[0]
#consultar = uic.loadUiType('consultar.ui')[0]
#base = uic.loadUiType('base.ui')[0]
juego=uic.loadUiType('./Ventanas/juego.ui')[0]
contabilidad = uic.loadUiType('./Ventanas/contabilidad.ui')[0]
ventas = uic.loadUiType('./Ventanas/Venta.ui')[0]
compras = uic.loadUiType('./Ventanas/compras.ui')[0]
resultados = uic.loadUiType('./Ventanas/resultados.ui')[0]
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
        self.btnContabilidad.clicked.connect(self.irContabilidad)
        self.btnJuego.clicked.connect(self.irJuego)
        self.btnOficio.clicked.connect(self.irOficio)
        self.btnContabilidad.clicked.connect(self.irContabilidad)

    def irPersonal(self):
        personal=PantallaPersonal()
        personal.exec_()
		 
    def irSemillero(self):
        semillero=PantallaSemillero()
        semillero.exec_()

    def irJuego(self):
        juego=PantallaJuego()
        juego.exec_()
    
    def irOficio(self):
        oficio=PantallaOficio()
        oficio.exec_()
    
    def irContabilidad(self):
        contabilidad=PantallaContabilidad()
        contabilidad.exec_()
	 
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
    
            tmp= [p.id,p.nombre,p.apellido,p.cedula,p.telefono,p.tipo,p.direccion,p.sexo,p.correo,p.carrera,p.facultad]
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
    personal = Personal()
    nino = Nino()
    semillero = Semillero()

    ninos = []


    def __init__(self,parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)
        self.inicializar()
       
    def inicializar(self):

        #self.btn_ninos.setStyleSheet("background-color: transparent")
        #self.btn_ninos.setStyleSheet("border: 0px solid transparent")

        self.btn_ninos.setStyleSheet("background-color: transparent")
        self.btn_ninos.setStyleSheet("border: 0px solid transparent")
        self.btn_ninos.setIcon(QIcon('./Imagenes/personal_agregar.png'))
        self.btn_ninos.setIconSize(QSize(35,25))

        self.setStyleSheet(estilo)
        #self.btn_ninos.setStyleSheet("color: transparent")
        #self.btn_imagen.setStyleSheet("background-color: transparent")
        #self.btn_imagen.setStyleSheet("border: 0px solid transparent")
        self.btn_imagen.setIcon(QIcon('./Imagenes/search.png'))
        self.btn_imagen.setIconSize(QSize(50,45))

        #self.btn_ninos.setStyleSheet("background-color: transparent")
        #self.btn_ninos.setStyleSheet("border: 0px solid transparent")
        self.btn_ninos.setIcon(QIcon('./Imagenes/personal_agregar.png'))
        self.btn_ninos.setIconSize(QSize(35,25))

        self.btn_ninos.clicked.connect(self.agregarNino)
        self.btn_guardar.clicked.connect(self.guardar)

        #self.btn_ninos.clicked.connect(self.irNino)

		#self.btn_image.setStyleShett()
		#self.btn_imagen.connect(self.irSearchFile)

        for p in self.personal.consultar_todos():
              self.cmb_personal.addItem(p.nombre + ' ' + p.apellido,p.id)

	#def irSearchFile(self):
		# search_file = PantallaSearchFile()
		#search_file.exec_()
		#print search_file.filePath

    def cargarNinos(self):
        for n in self.nino.consultar_todos():
              self.cmb_ninos.addItem(n.nombre,n.id)
    

    def agregarNino(self):
        nino= PantallaNino()
        nino.exec_()

        n = Nino()
        #print d.producto
        #if d.producto is None:
        #    return 0
        n.nombre = nino.nino.nombre
        n.apellido = nino.nino.apellido
        n.edad = nino.nino.edad
        n.esAlergico = nino.nino.esAlergico
        n.observacion = nino.nino.observacion
        print n.nombre
        self.ninos.append(n)
        #self.actualizar()

    def irNino(self):
        nino= PantallaNino()
        nino.exec_()

    def validarDatos(self):
        """try:
            if len(str(self.txt_tipo.text()))<1:
                return False
        except:
            return False"""
        return True



    def guardar(self):
        if not self.validarDatos():
            QMessageBox.about(self,"ERROR","Ingrese un tipo de semillero")
        else:
            self.semillero.tipo = str(self.txt_tipo.text())
            self.semillero.imagen = str(self.txt_imagen.text())
            self.semillero.ubicacion = str(self.txt_ubicacion.text())
            self.semillero.personal.id = (self.cmb_personal.itemData(self.cmb_personal.currentIndex())).toInt()[0]
            #self.semillero. = str(self.txt_telefono.text())
            #self.semillero.nIntegrantes = len(self.ninos)
            #self.semillero.ninos = self.nino
            self.semillero.ninos = self.ninos
            self.semillero.guardar()
            #self.cargarPersonal()
            self.limpiar()
            QMessageBox.about(self,"Correcto","Semillero guardado con exito")
    
    def limpiar(self):
        self.ninos = []
        self.txt_tipo.setText('')
        self.txt_imagen.setText('')
        self.txt_ubicacion.setText('')

    def guardar(self):
        if self.validarDatos():
            QMessageBox.about(self,"ERROR","Ingrese un tipo de semillero")
        else:
            self.semillero.tipo = star(self.txt_nombre.text())
            self.semillero.imagen = str(self.txt_apellido.text())
            self.semillero.ubicacion = str(self.txt_cedula.text())
            self.semillero.personal.id = str(self.txt_direccion.text())
            self.semillero.telefono = str(self.txt_telefono.text())
            self.semillero.nIntegrantes = len(self.semillero.ninos)
            self.semillero.guardar()
            #self.cargarPersonal()
            #self.limpiar()
            QMessageBox.about(self,"Correcto","Semillero guardado con exito")
    
    

class PantallaNino(QtGui.QDialog, ninos):
    nino = Nino()
    representantes = []

    def __init__(self,parent=None):
        QtGui.QDialog.__init__(self,parent)
        self.setupUi(self)
        self.inicializar()

    def inicializar(self):
        self.btn_guardar.clicked.connect(self.guardar)
        self.btn_representante.clicked.connect(self.agregarRepresentante)
    
    def agregarRepresentante(self):
        representante = PantallaRepresentante()
        representante.exec_()

        repre = Representante()

        repre.nombre = representante.repre.nombre
        repre.apellido = representante.repre.apellido
        repre.telefono = representante.repre.telefono
        repre.expreso = representante.repre.expreso
        #self.repre.nInscritos = len(self.representantes)
        self.representantes.append(repre)


    def guardar(self):
        #self.detalle.producto.id = (self.cbo_producto.itemData(self.cbo_producto.currentIndex())).toInt()[0]
        #self.detalle.producto.consultar()

        if len(str(self.txt_nombre.text()))<1 and len(str(self.txt_apellido.text()))<1 and len(str(self.txt_edad.text()))==0:
            QMessageBox.about(self,"ERROR","Ingrese los campos")
        else:
            self.nino.nombre = str(self.txt_nombre.text())
            self.nino.apellido = str(self.txt_apellido.text())
            self.nino.edad= str(self.txt_edad.text())
            self.nino.esAlergico = str(self.cmb_alergia.currentText())
            self.nino.representantes = self.representantes
            #self.observacion = str(self.txt_observacion.text())
            self.nino.guardar()
            print self.nino.nombre
            print self.nino.apellido
            self.limpiar()
            #self.close()
            QMessageBox.about(self,"CORRECTO","Se ha ingresado un nino")

    def limpiar(self):
        self.representantes = []
        self.txt_nombre.setText('')
        self.txt_apellido.setText('')
        self.txt_edad.setText('') 
        #self.txt_esAlergico.setText('')
        self.txt_observacion.setText('')

class PantallaRepresentante(QtGui.QDialog, representante):
    
    repre = Representante()

    def __init__(self,parent=None):
        QtGui.QDialog.__init__(self,parent)
        self.setupUi(self)


    def guardar(self):
        #self.detalle.producto.id = (self.cbo_producto.itemData(self.cbo_producto.currentIndex())).toInt()[0]
        #self.detalle.producto.consultar()

        if len(str(self.txt_nombre.text()))<1 and len(str(self.txt_apellido.text()))<1 and len(str(self.txt_telefono.text()))<1:
            QMessageBox.about(self,"ERROR","Ingrese los campos")
        else:
            self.repre.nombre = str(self.txt_nombre.text())
            self.repre.apellido = str(self.txt_apellido.text())
            self.repre.telefono= str(self.txt_telefono.text())
            self.repre.expreso = str(self.cmb_expreso.currentText())
            #self.repre.expreso = str(self.cmb_expreso.currentText())
            #print self.nino.nombre
            #print self.nino.apellido
            self.limpiar()
            #self.close()
            QMessageBox.about(self,"CORRECTO","Se ha ingresado un representante")

    def limpiar(self):
        self.txt_nombre.setText('')
        self.txt_apellido.setText('')
        #self.txt_edad.setText('') 
        #self.txt_esAlergico.setText('')
        self.txt_telefono.setText('')



class PantallaJuego(QtGui.QDialog,juego):
    juego=Juego()
    
    def __init__(self,parent=None):
        QtGui.QDialog.__init__(self,parent)
        self.setupUi(self)
        self.personal=Personal()
        self.inicializar()

    def inicializar(self):
         
        self.setStyleSheet(estilo)
   
        self.ruta=''
        self.nombre_fichero=''
        self.juegos=[]
        self.LlenarCombo()
        self.setStyleSheet(estilo)
        self.btnLimpiar.clicked.connect(self.limpiar)
        self.btnGuardar.clicked.connect(self.guardar)
        self.btnImagen.clicked.connect(self.abrir)
        self.btnEliminar.clicked.connect(self.borrarTodo)
        self.tbaJuego.doubleClicked.connect(self.elegir_dobleclick)
        self.btnBuscar.clicked.connect(self.buscar)
        self.tbaJuegoEliminar.doubleClicked.connect(self.borrarSelec)        
	#self.txtNombre.textChanged.connect(self.onlyTextName)
    	self.cargar()

    def validacion(self):
       
        if(self.txtNombre.text()=="" or self.txtArea.text()=="" or self.txtUbicacion.text()==""):
            return True            
        else:
            return False
   
    def guardar(self):
        if self.validacion():
            QMessageBox.about(self,"ERROR","Ingresar todos los datos")
           
        else:
            self.juego.nombre = str(self.txtNombre.text())
            self.juego.area = str(self.txtArea.text())
            self.juego.ubicacion = str(self.txtUbicacion.text())
            self.juego.imagen = str(self.nombre_fichero)
            self.juego.personal.id = (self.cmbResponsable.itemData(self.cmbResponsable.currentIndex())).toInt()[0]
            self.juego.guardar()
            self.limpiar()
            QMessageBox.about(self,"Correcto","Juego guardado con exito")
            self.cargar()

    def limpiar(self):
        self.txtNombre.setText('')
        self.txtArea.setText('')
        self.txtUbicacion.setText('')
        #self.cmbResponsable.setText('')
        self.txtImagen.setPixmap(QPixmap(''))
	#def CargarPersonal(self):
    
    def abrir(self):
        self.nombre_fichero = QFileDialog.getOpenFileName(self, "Abrir fichero", self.ruta)
        if self.nombre_fichero:
            fichero_actual = self.nombre_fichero
            self.ruta = QFileInfo(self.nombre_fichero).path()	
            self.txtImagen.setPixmap(QPixmap(self.nombre_fichero))
            self.txtImagen.setScaledContents(True)	

    def cargar(self, atribute=None, name=None):
        model = QStandardItemModel()
        model.setColumnCount(5)
        model.setHorizontalHeaderLabels(self.juego.headernames)
        busq1 = []
        self.juegos=[]
        if (atribute is not None) and (name is not None):
            if name == 'nombre' or name == 'area' or name == 'cedula':
                busq1 = self.juego.consultar_By_Atribute(atribute,name)
            else:
                busq1=[]        
        else:
             busq1 = self.juego.consultar_todos()

        for p in busq1:
            tmp = [p.id, p.nombre,p.imagen, p.area,p.ubicacion,p.personal]
            li = [p.nombre,p.imagen, p.area,p.ubicacion,p.personal]
            self.juegos.append(tmp)
            row = []
            for name in li:
                item = QStandardItem(str(name))
                item.setEditable(False)
                row.append(item)

            model.appendRow(row)
        self.tbaJuego.setModel(model)
        self.tbaJuegoEliminar.setModel(model)

    def elegir_dobleclick(self):
        selected = self.tbaJuego.selectedIndexes()
        selected_index = selected.__getitem__(0)
        select = self.juegos[selected_index.row()]
        self.tabWidget.setCurrentWidget(self.tab_1)
        self.juego.id = select[0]
        self.txtNombre.setText(select[1])
        self.txtImagen.setPixmap(QPixmap(select[2]))
        self.txtArea.setText(str(select[3]))
        self.txtUbicacion.setText(str(select[4]))
        #self.cmb_tipo.setCurrentIndex(self.cmb_tipo.findText(select[5]))
    
    def LlenarCombo(self):
        for p in self.personal.consultar_todos():
            self.cmbResponsable.addItem(p.nombre,p.id)

    def borrarTodo(self):
        try:
            rst=QMessageBox.warning(self,"Alerta","Esta seguro que desea eliminar", QMessageBox.Cancel, QMessageBox.Ok)
            if rst == QMessageBox.Ok:
                self.juego.borrarJuegos()
                QMessageBox.about(self,"Correcto", "Se ha eliminado todo el personal")
        except:
            QMessageBox.about(self,"Error", "Problemas con la base de datos")
        self.cargar()

    def borrarSelec(self):
        try:
            selected = self.tbaJuegoEliminar.selectedIndexes()
            selected_index = selected.__getitem__(0)
            select = self.juegos[selected_index.row()]
            self.juego.id = select[0]

            rst=QMessageBox.warning(self,"Alerta","Esta seguro que desea eliminar", QMessageBox.Cancel, QMessageBox.Ok)
            if rst == QMessageBox.Ok:
                self.juego.borrarJuego()
                QMessageBox.about(self,"Correcto", "Se ha eliminado al Cliente")
        except:
            QMessageBox.about(self,"Error", "Problemas con la base de datos")
        self.cargar()

    def buscar(self):
        atribute= (str(self.txtBuscar.text())).strip()
        name=''
        print atribute
        if atribute != '':
            if self.rdoNombre.isChecked():
                name= 'nombre'
                
                self.cargar(atribute,name)
            elif self.rdoArea.isChecked():
                name= 'area'
                self.cargar(atribute,name)
            elif self.rdoUbicacion.isChecked():
                name= 'ubicacion'
                self.cargar(atribute,name)
            else:
                self.cargar()
        else:
            self.cargar()


class PantallaContabilidad(QtGui.QDialog,contabilidad):
    def __init__(self,parent=None):
        QtGui.QDialog.__init__(self,parent)
        self.setupUi(self)
        self.inicializar()

    def inicializar(self):
        self.btnCompras.clicked.connect(self.Compras)
        self.btnVentas.clicked.connect(self.Ventas)
        self.btnResultados.clicked.connect(self.Resultados)
        self.setStyleSheet(estilo)
 
    def Compras(self):
        compras = PantallaCompras()
        compras.exec_()    

    def Ventas(self):
        ventas = PantallaVentas()
        ventas.exec_()

    def Resultados(self):
        resultados = PantallaResultados()
        resultados.exec_()

class PantallaVentas(QtGui.QDialog,ventas):
    venta = Ventas()
    tmpCantidad = ""
    tmpCosto = ""
    def __init__(self,parent=None):
        QtGui.QDialog.__init__(self,parent)
        self.setupUi(self)
        self.personal=Personal()
        self.inicializar()
        
    def LlenarCombo(self):
        for p in self.personal.consultar_todos():
            self.cmbResponsable.addItem(p.nombre,p.id)

    def inicializar(self):
        ventas=[]
        self.txtTotal.setText('0')
        self.LlenarCombo()
        self.setStyleSheet(estilo)
        self.btnGuardar.clicked.connect(self.guardar)
        self.btnLimpiar.clicked.connect(self.limpiar)
        self.btnEliminar.clicked.connect(self.borrarTodo)
        self.tbaVenta.doubleClicked.connect(self.elegir_dobleclick)
        self.tbaVentaEliminar.doubleClicked.connect(self.borrarSelec)
        self.txtCosto.textChanged.connect(lambda: self.onlyDigit('costo,' + self.txtCosto.text()))
        self.txtCantidad.textChanged.connect(lambda: self.onlyDigit('cantidad,'+ self.txtCantidad.text())) 
        self.cargar()
 
    def onlyDigit(self,texto):
        try:
            number = str(texto.split(',')[1])
            name = str(texto.split(',')[0])

            if number != '':
                if not ((number.replace(' ','')).isdigit() and (number.replace('.','')).isdigit()) :
                    QMessageBox.about(self,"ERROR","Ingresar solo digitos")
                    if name == 'cantidad':
                        self.txtCantidad.setText(self.tmpCantidad)
                    elif name == 'costo':
                        self.txtCosto.setText(self.tmpCosto)

                else:
                    if len(number) == 1:
                        self.tmpCantidad = ''
                        self.tmpCosto = ''
                    else:
                        if name == 'cantidad':
                            self.tmpCantidad = number
                        elif name == 'costo':
                            self.tmpCosto = number
		
        except:
            name = str(texto.split(',')[0])
            QMessageBox.about(self,"ERROR","Ingresar solo digitos")
											
            if name == 'cantidad':
                self.tmpCantidad=''
                self.txtCantidad.setText('')
            elif name == 'costo':
                self.tmpCosto=''
                self.txtCosto.setText('')

        if self.txtCosto.text()=='' or self.txtCantidad.text()=='':
            self.txtTotal.setText('0')
        else:
            costo = float(self.txtCosto.text())
            cantidad = int(self.txtCantidad.text())
            total = costo*cantidad
            self.txtTotal.setText(str(total)) 

    def validacion(self):
       
        if(self.txtDetalle.text()=="" or self.txtCantidad.text()=="" or self.txtCosto.text()==""):
            return True            
        else:
            return False

    def guardar(self):
        if self.validacion():
            QMessageBox.about(self,"ERROR","Ingresar todos los datos")
           
        else:
            self.venta.Detalle = str(self.txtDetalle.text())
            self.venta.Costo = str(self.txtCosto.text())
            self.venta.Cantidad = str(self.txtCantidad.text())
            self.venta.Fecha = str(self.dteFecha.text())
            self.venta.Total = str(self.txtTotal.text())
            self.venta.personal.id = (self.cmbResponsable.itemData(self.cmbResponsable.currentIndex())).toInt()[0]
            self.venta.Observaciones = str(self.txtObservaciones.toPlainText())
            self.venta.guardar()
            self.limpiar()
            QMessageBox.about(self,"Correcto","Venta guardado con exito")
            self.cargar()
             
    
    def limpiar(self):
        self.txtDetalle.setText('')
        self.txtCosto.setText('')
        self.txtCantidad.setText('')
        self.txtTotal.setText('')
        self.txtObservaciones.setText('')
   
    def cargar(self, atribute=None, name=None):
        model = QStandardItemModel()
        model.setColumnCount(7)
        model.setHorizontalHeaderLabels(self.venta.headernames)
        busq1 = []
        self.ventas=[]
        if (atribute is not None) and (name is not None):
            if name == 'Detalle' or name == 'Fecha':
                busq1 = self.venta.consultar_By_Atribute(atribute,name)
            else:
                busq1=[]        
        else:
             busq1 = self.venta.consultar_todos()

        for v in busq1:
            tmp = [v.id, v.Detalle, v.Costo, v.Cantidad, v.Total, v.Observaciones, v.personal]
            li = [v.id, v.Detalle, v.Costo, v.Cantidad, v.Total, v.Observaciones, v.personal]
            self.ventas.append(tmp)
            row = []
            for name in li:
                item = QStandardItem(str(name))
                item.setEditable(False)
                row.append(item)

            model.appendRow(row)
        self.tbaVenta.setModel(model)
        self.tbaVentaEliminar.setModel(model)

    def elegir_dobleclick(self):
        selected = self.tbaVenta.selectedIndexes()
        selected_index = selected.__getitem__(0)
        select = self.ventas[selected_index.row()]
        self.tabWidget.setCurrentWidget(self.tab_1)
        self.venta.id = select[0]
        self.txtDetalle.setText(select[1])
        self.txtCosto.setText(select[2])
        self.txtCantidad.setText(select[3])
        self.txtTotal.setText(select[4])
        self.txtObservaciones.setText(select[5])

    def borrarTodo(self):
        try:
            rst=QMessageBox.warning(self,"Alerta","Esta seguro que desea eliminar", QMessageBox.Cancel, QMessageBox.Ok)
            if rst == QMessageBox.Ok:
                self.venta.borrarVentas()
                QMessageBox.about(self,"Correcto", "Se ha eliminado todo el personal")
        except:
            QMessageBox.about(self,"Error", "Problemas con la base de datos")
        self.cargar()

    def borrarSelec(self):
        try:
            selected = self.tbaOficioEliminar.selectedIndexes()
            selected_index = selected.__getitem__(0)
            select = self.ventas[selected_index.row()]
            self.oficio.id = select[0]

            rst=QMessageBox.warning(self,"Alerta","Esta seguro que desea eliminar", QMessageBox.Cancel, QMessageBox.Ok)
            if rst == QMessageBox.Ok:
                self.venta.borrarVentas()
                QMessageBox.about(self,"Correcto", "Se ha eliminado la venta")
        except:
            QMessageBox.about(self,"Error", "Problemas con la base de datos")
        self.cargar()

    
    def buscar(self):
        atribute= (str(self.txtBuscar.text())).strip()
        name=''
        print atribute
        if atribute != '':
            if self.rdoDetalle.isChecked():
                name= 'Detalle'
                self.cargar(atribute,name)
            elif self.rdoFecha.isChecked():
                name= 'Fecha'
                self.cargar(atribute,name)
            else:
                self.cargar()
        else:
            self.cargar()


class PantallaResultados(QtGui.QDialog,resultados):
    ventas=0
    compras=0
    total = 0
    def __init__(self,parent=None):
        QtGui.QDialog.__init__(self,parent)
        self.setupUi(self)
        self.inicializar()

    def inicializar(self):
        self.setStyleSheet(estilo)
        self.totalCompras()
        self.totalVentas()
        self.total=self.ventas-self.compras
        txtCompras.setText(str(self.compras))
        txtVentas.setText(str(self.ventas))
        txtTotal.setText(str(self.total))

    def totalCompras(self):
        conexion = self.conexion.getConnection()
        cursor = conexion.cursor()
        cursor.execute("call CompraTotal()")
        result=cursor.fetchall()
        if result is None:
            self.compras=0
        else:
            self.compras = float(result[0])
        cursor.close
            

    def totalVentas(self):
        conexion = self.conexion.getConnection()
        cursor = conexion.cursor()
        cursor.execute("call VentaTotal()")
        result=cursor.fetchall()
        if result is None:
            self.ventas=0
        else:
            self.ventas = float(result[0])
        cursor.close
        
class PantallaCompras(QtGui.QDialog,compras):
    compra = Compras()
    tmpGasto = ''
    def __init__(self,parent=None):
        QtGui.QDialog.__init__(self,parent)
        self.setupUi(self)
        self.personal=Personal()
        self.inicializar()
        
    def LlenarCombo(self):
        for p in self.personal.consultar_todos():
            self.cmbResponsable.addItem(p.nombre,p.id)

    def inicializar(self):
        ventas=[]
        self.LlenarCombo()
        self.setStyleSheet(estilo)
        self.btnGuardar.clicked.connect(self.guardar)
        self.btnLimpiar.clicked.connect(self.limpiar)
        self.btnEliminar.clicked.connect(self.borrarTodo)
        self.tbaCompras.doubleClicked.connect(self.elegir_dobleclick)
        self.txtGasto.textChanged.connect(lambda: self.onlyDigit('gasto,'+ self.txtGasto.text()))
        self.tbaComprasEliminar.doubleClicked.connect(self.borrarSelec)
        self.cargar()

    def onlyDigit(self,texto):
        try:
            number = str(texto.split(',')[1])
            name = str(texto.split(',')[0])

            if number != '':
                if not ((number.replace(' ','')).isdigit() and (number.replace('.','')).isdigit()) :
                    QMessageBox.about(self,"ERROR","Ingresar solo digitos")
                    if name == 'gasto':
                        self.txtGasto.setText(self.tmpGasto)
                else:
                    if len(number) == 1:
                        self.tmpGasto = ''

                    else:
                        if name == 'gasto':
                            self.tmpGasto = number
	
        except:
            name = str(texto.split(',')[0])
            QMessageBox.about(self,"ERROR","Ingresar solo digitos")
											
            if name == 'gasto':
                self.tmpGasto=''
                self.txtGasto.setText('')

    def validacion(self):
       
        if(self.txtDetalle.text()=="" or self.txtTipo.text()=="" or self.txtGasto.text()==""):
            return True            
        else:
            return False

    def guardar(self):
        if self.validacion():
            QMessageBox.about(self,"ERROR","Ingresar todos los datos")
           
        else:
            self.compra.Detalle = str(self.txtDetalle.text())
            self.compra.Gasto = str(self.txtGasto.text())
            self.compra.Fecha = str(self.dteFecha.text())
            self.compra.Tipo = str(self.txtTipo.text())
            self.compra.personal.id = (self.cmbEncargado.itemData(self.cmbEncargado.currentIndex())).toInt()[0]
            self.compra.Observaciones = str(self.txtObservaciones.PlainText())
            self.compra.guardar()
            self.limpiar()
            QMessageBox.about(self,"Correcto","Venta guardado con exito")
            self.cargar()
             
    
    def limpiar(self):
        self.txtDetalle.setText('')
        self.txtGasto.setText('')
        self.txtObsevaciones.setText('')
        self.txtTipo.setText('')
        self.txtObservaciones.setText('')
   
    def cargar(self, atribute=None, name=None):
        model = QStandardItemModel()
        model.setColumnCount(7)
        model.setHorizontalHeaderLabels(self.compra.headernames)
        busq1 = []
        self.compras=[]
        if (atribute is not None) and (name is not None):
            if name == 'Detalle' or name == 'Fecha':
                busq1 = self.compra.consultar_By_Atribute(atribute,name)
            else:
                busq1=[]        
        else:
             busq1 = self.compra.consultar_todos()

        for c in busq1:
            tmp = [c.id, c.Detalle, c.Gasto, v.Fecha, v.Tipo, v.Observaciones, v.personal]
            li = [c.id, c.Detalle, c.Gasto, c.Fecha, c.Tipo, c.Observaciones, c.personal]
            self.compras.append(tmp)
            row = []
            for name in li:
                item = QStandardItem(str(name))
                item.setEditable(False)
                row.append(item)

            model.appendRow(row)
        self.tbaCompras.setModel(model)
        self.tbaComprasEliminar.setModel(model)

    def elegir_dobleclick(self):
        selected = self.tbaCompras.selectedIndexes()
        selected_index = selected.__getitem__(0)
        select = self.compras[selected_index.row()]
        self.tabWidget.setCurrentWidget(self.tab_1)
        self.compra.id = select[0]
        self.txtDetalle.setText(select[1])
        self.txtGasto.setText(select[2])
        self.txtTipo.setText(select[3])
        self.dteFecha.setText(select[4])
        self.txtObservaciones.setText(select[5])

    def borrarTodo(self):
        try:
            rst=QMessageBox.warning(self,"Alerta","Esta seguro que desea eliminar", QMessageBox.Cancel, QMessageBox.Ok)
            if rst == QMessageBox.Ok:
                self.compra.borrarCompras()
                QMessageBox.about(self,"Correcto", "Se ha eliminado todo el personal")
        except:
            QMessageBox.about(self,"Error", "Problemas con la base de datos")
        self.cargar()

    def borrarSelec(self):
        try:
            selected = self.tbaOficioEliminar.selectedIndexes()
            selected_index = selected.__getitem__(0)
            select = self.compras[selected_index.row()]
            self.compra.id = select[0]

            rst=QMessageBox.warning(self,"Alerta","Esta seguro que desea eliminar", QMessageBox.Cancel, QMessageBox.Ok)
            if rst == QMessageBox.Ok:
                self.compra.borrarCompras()
                QMessageBox.about(self,"Correcto", "Se ha eliminado la venta")
        except:
            QMessageBox.about(self,"Error", "Problemas con la base de datos")
        self.cargar()

    
    def buscar(self):
        atribute= (str(self.txtBuscar.text())).strip()
        name=''
        print atribute
        if atribute != '':
            if self.rdoDetalle.isChecked():
                name= 'Detalle'
                self.cargar(atribute,name)
            elif self.rdoFecha.isChecked():
                name= 'Fecha'
                self.cargar(atribute,name)
            else:
                self.cargar()
        else:
            self.cargar()



class PantallaOficio(QtGui.QDialog,oficio):
    oficio=Oficio()
    
    def __init__(self,parent=None):
        QtGui.QDialog.__init__(self,parent)
        self.setupUi(self)
        self.personal=Personal()
        self.inicializar()

    def inicializar(self):
        self.oficios=[]
        self.setStyleSheet(estilo)
        self.btnLimpiar.clicked.connect(self.limpiar)
        self.btnGuardar.clicked.connect(self.guardar)
        self.btnEliminar.clicked.connect(self.borrarTodo)
        self.tbaOficio.doubleClicked.connect(self.elegir_dobleclick)
        #self.btnBuscar.clicked.connect(self.buscar)
        self.tbaOficioEliminar.doubleClicked.connect(self.borrarSelec)        
	#self.txtNombre.textChanged.connect(self.onlyTextName)
        self.cargar()

    def validacion(self):
       
        if(self.txtDetalle.text()=="" or self.txtDestinatario.text()=="" or self.txtTramite.text()=="" or self.txtRespuesta=="" or self.txtObservaciones.text()==""):
            return True            
        else:
            return False
   
    def guardar(self):
        if self.validacion():
            QMessageBox.about(self,"ERROR","Ingresar todos los datos")
           
        else:
            self.oficio.Detalle = str(self.txtDetalle.text())
            self.oficio.Destinatario = str(self.txtDestinatario.text())
            self.oficio.Estado = str(self.cmbEstado.currentText())
            self.oficio.Tramite = str(self.txtTramite.text())
            self.oficio.Respuesta = str(self.txtRespuesta.text())
            self.oficio.Observaciones = str(self.txtObservaciones.text())
            self.oficio.personal = str(1)
            self.oficio.guardar()
            self.limpiar()
            QMessageBox.about(self,"Correcto","Oficio guardado con exito")
            self.cargar()

    def limpiar(self):
        self.txtDetalle.setText('')
        self.txtDestinatario.setText('')
        self.txtObservaciones.setText('')
        self.txtRespuesta.setText('')
        self.txtTramite.setText('')
	#def CargarPersonal(self):
   
    def cargar(self, atribute=None, name=None):
        model = QStandardItemModel()
        model.setColumnCount(7)
        model.setHorizontalHeaderLabels(self.oficio.headernames)
        busq1 = []
        self.oficios=[]
        if (atribute is not None) and (name is not None):
            if name == 'nombre' or name == 'area' or name == 'cedula':
                busq1 = self.oficio.consultar_By_Atribute(atribute,name)
            else:
                busq1=[]        
        else:
             busq1 = self.oficio.consultar_todos()

        for o in busq1:
            tmp = [o.id, o.Detalle,o.Destinatario, o.Estado,o.Tramite,o.Respuesta, o.Observaciones, o.personal]
            li = [o.Detalle,o.Destinatario, o.Estado,o.Tramite,o.Respuesta, o.Observaciones, o.personal]
            self.oficios.append(tmp)
            row = []
            for name in li:
                item = QStandardItem(str(name))
                item.setEditable(False)
                row.append(item)

            model.appendRow(row)
        self.tbaOficio.setModel(model)
        self.tbaOficioEliminar.setModel(model)

    def elegir_dobleclick(self):
        selected = self.tbaOficio.selectedIndexes()
        selected_index = selected.__getitem__(0)
        select = self.oficios[selected_index.row()]
        self.tabWidget.setCurrentWidget(self.tab_1)
        self.oficio.id = select[0]
        self.txtDetalle.setText(select[1])
        self.txtDestinatario.setText(select[2])
        self.cmbEstado.findText(select[3])
        self.txtTramite.setText(select[4])
        self.txtRespuesta.setText(select[5])
        self.txtObservaciones.setText(select[6])
        #self.cmb_tipo.setCurrentIndex(self.cmb_tipo.findText(select[5]))
    
    def LlenarCombo(self):
        for p in self.personal.consultar_todos():
            self.cmbResponsable.addItem(p.nombre)

    def borrarTodo(self):
        try:
            rst=QMessageBox.warning(self,"Alerta","Esta seguro que desea eliminar", QMessageBox.Cancel, QMessageBox.Ok)
            if rst == QMessageBox.Ok:
                self.oficio.borrarOficios()
                QMessageBox.about(self,"Correcto", "Se ha eliminado todo el personal")
        except:
            QMessageBox.about(self,"Error", "Problemas con la base de datos")
        self.cargar()

    def borrarSelec(self):
        try:
            selected = self.tbaOficioEliminar.selectedIndexes()
            selected_index = selected.__getitem__(0)
            select = self.ofcios[selected_index.row()]
            self.oficio.id = select[0]

            rst=QMessageBox.warning(self,"Alerta","Esta seguro que desea eliminar", QMessageBox.Cancel, QMessageBox.Ok)
            if rst == QMessageBox.Ok:
                self.juego.borrarOficio()
                QMessageBox.about(self,"Correcto", "Se ha eliminado al Cliente")
        except:
            QMessageBox.about(self,"Error", "Problemas con la base de datos")
        self.cargar()
"""
    def buscar(self):
        atribute= (str(self.txtBuscar.text())).strip()
        name=''
        print atribute
        if atribute != '':
            if self.rdoNombre.isChecked():
                name= 'nombre'
                
                self.cargar(atribute,name)
            elif self.rdoArea.isChecked():
                name= 'area'
                self.cargar(atribute,name)
            elif self.rdoUbicacion.isChecked():
                name= 'ubicacion'
                self.cargar(atribute,name)
            else:
                self.cargar()
        else:
            self.cargar()
"""

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    log = Login()
    
    if log.exec_() == QtGui.QDialog.Accepted:
            
        #log.close()
        principal = Principal()
        principal.show()
    sys.exit(app.exec_()) 
    sys.exit(log.close())
