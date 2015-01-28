from Conexion import *
from objeto import * 
from Nino import *

class Representante(Objeto):

  nino = Nino()
  nombre = ''
  apellido = ''
  telefono = ''
  expreso = ''
  nInscritos = ''
  #nino = ''
  headernames = ['Nombre','Apellido','Telefono','Expreso','N. Inscritos']
  atributos = 'representante_id, representante_nombre, \
               representante_apellido,representante_telefono, \
               representante_expreso,representante_nInscritos, \
               representante_nino'
  tabla = ' representante'
  
  def __init__(self):
    self.inicializar()

  def cargar(self):
    pass
     #TODO

  def idNino(self):
    self.index = self.contar()
  
  def guardar(self):
    consulta = 'SELECT * FROM Representante WHERE representante_id = %s ;'
    conexion = self.conexion.getConnection()
    cursor= conexion.cursor()
    cursor.execute(consulta, (str(self.id),))
    if cursor.fetchone() is None:
      query = self.query_insert + ' %s,%s,%s,%s,%s,%s,%s '+self.query_insert_end
      cursor.execute(query,(str(self.contar()),self.nombre,self.apellido,self.telefono,self.expreso,self.nInscritos,self.nino.id))
      conexion.commit()
      cursor.close()
      print query
    else:
      cursor.close()
      self.modificar()

  def borrarNinos(self):
    self.eliminar_todo()  
  
  def borrarNino(self):
    self.eliminar()

  def modificar(self):
    query = (self.query_update+ 'representante_nombre= %s, representante_apellido= %s,representante_telefono= %s ,representante_expreso = %s,representante_nInscritos = %s,representante_nino=%s' + self.query_update_end)
    conexion = self.conexion.getConnection()
    cursor= conexion.cursor()
    cursor.execute(query,(self.nombre,self.apellido,self.telefono,self.expreso,self.nInscritos,self.nino.id,self.id))
    conexion.commit()
    cursor.close()

#Falta abajo
  def enlistar(self, listas):
    lista=[]
    for r in listas: 
      repre = Represenatante()
      repre.mapeardatos(r)
      lista.append(repre)
    return lista

  def mapeardatos(self, datarow):
    self.id = datarow[0]
    self.nombre = datarow[1]
    self.apellido = datarow[2]
    self.telefono = datarow[3]
    self.expreso = datarow[4]
    self.nInscritos = datarow[5]
    self.nino.id = datarow[6]
    
    
