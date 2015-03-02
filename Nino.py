from Conexion import *
from objeto import * 
from Semillero import *

class Nino(Objeto):
  nombre = ''
  apellido = ''
  edad = ''
  esAlergico = ''
  observacion = ''
  semillero = Semillero()
  representantes = []
  headernames = ['Nombre','Apellido','Edad','Alergico','Observacion']
  atributos = 'nino_id, nino_nombre, nino_apellido, \
               nino_edad,nino_esAlergico,nino_observacion, \
               nino_semillero'
  
  tabla = ' nino'
  
  def __init__(self):
    self.inicializar()

  def guardar(self):
    self.id = self.contar()
    #consulta = 'SELECT * FROM Nino WHERE nino_id = %s ;'
    conexion = self.conexion.getConnection()
    cursor= conexion.cursor()
    cursor.callproc('ingresoNino',(self.id,self.nombre,self.apellido,self.edad,self.esAlergico,self.observacion,self.semillero.id))
    conexion.commit()
    cursor.close()
    for repre in self.representantes:
      #repre.nino.id = id
      #detalle.id = i
      repre.guardar()
      repre.nino.id = self.id
      repre.guardarRepresentacion()

  
  def modificar(self):
    query = (self.query_update+ 'nino_nombre= %s, nino_apellido= %s,nino_edad= %s ,nino_esAlergico = %s,nino_observacion = %s,nino_semillero=%s' + self.query_update_end)
    
    conexion = self.conexion.getConnection()
    cursor= conexion.cursor()
    cursor.execute(query,(self.nombre,self.apellido,self.edad,self.esAlergico,self.observacion,self.semillero.id,self.id))
    conexion.commit()
    cursor.close()

  def enlistarRepresentante(self):
    query = ('select rnte.* from Representacion rcion ,Representante rnte where rcion.representacion_nino = %s and rnte.representante_id  = rcion.representacion_representante')
    conexion = self.conexion.getConnection()
    cursor= conexion.cursor()
    cursor.execute(query,(self.id))
    result = cursor.fetchall()
    cursor.close()
    
    for r in result: 
      repre = Representante()
      repre.mapeardatos(r)
      self.representantes.append(repre)
    

	
  def enlistar(self, listas):
    lista=[]
    for r in listas: 
      nino = Nino()
      nino.mapeardatos(r)
      lista.append(nino)
    return lista
    

  def mapeardatos(self, datarow):
    self.id = datarow[0]
    self.nombre = datarow[1]
    self.apellido = datarow[2]
    self.edad = datarow[3]
    self.esAlergico = datarow[4]
    self.observacion = datarow[5]
    self.semillero.id = datarow[6]
