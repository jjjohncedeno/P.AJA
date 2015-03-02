from Conexion import *
from objeto import *
from Nino import *
class Representante(Objeto):

  nombre = ''
  apellido = ''
  cedula = ''
  telefono = ''
  expreso = ''
  nInscritos = 0
  parentesco = ''
  #nino = Nino()

  headernames = ['Nombre','Apellido','Cedula','Telefono','Expreso','N. Inscritos']
  atributos = 'representante_id, representante_nombre, \
               representante_apellido,representante_cedula, \
               representante_telefono, \
               representante_expreso,representante_nInscritos'
  tabla = ' representante'
  
  def __init__(self):
    self.inicializar()

 
  def guardar(self):
    self.id = self.contar()
    #consulta = 'SELECT * FROM Representante WHERE representante_id = %s ;'
    conexion = self.conexion.getConnection()
    cursor= conexion.cursor()
    #cursor.execute(consulta, (str(self.id),))
    cursor.callproc('ingresoRepresentante',(self.id,self.nombre,self.apellido,self.cedula,self.telefono,self.expreso,self.nInscritos))
    conexion.commit()
    cursor.close()

  def guardarRepresentacion(self):
    conexion = self.conexion.getConnection()
    cursor= conexion.cursor()
    cursor.callproc('ingresoRepresentacion',(self.parentesco,self.id,self.nino.id))
    conexion.commit()
    cursor.close()
    

    """if cursor.fetchone() is None:
      #query = self.query_insert + ' %s,%s,%s,%s,%s,%s,%s '+self.query_insert_end
      cursor.callproc('ingresoRepresentante',(self.contar(),self.nombre,self.apellido,self.telefono,self.expreso,self.nInscritos))
      conexion.commit()
      cursor.close()
      #print query
    else:
      cursor.close()
      self.modificar()"""

  
  def modificar(self):
    query = (self.query_update+ 'representante_nombre= %s, representante_apellido= %s,representante_cedula= %s,representante_telefono= %s ,representante_expreso = %s,representante_nInscritos = %s' + self.query_update_end)
    conexion = self.conexion.getConnection()
    cursor= conexion.cursor()
    cursor.execute(query,(self.nombre,self.apellido,self.cedula,self.telefono,self.expreso,self.nInscritos,self.id))
    conexion.commit()
    cursor.close()


  def enlistarParentesco(self):
    query = ('select representacion_parentesco from Representacion where representacion_representante = %s and representacion_nino = %s ')
    conexion = self.conexion.getConnection()
    cursor= conexion.cursor()
    cursor.execute(query,(self.id,self.nino.id))
    result = cursor.fetchall()
    cursor.close()
    return result[0][1]

  def enlistar(self, listas):
    lista=[]
    for r in listas: 
      repre = Representante()
      repre.mapeardatos(r)
      lista.append(repre)
    return lista

  def mapeardatos(self, datarow):
    self.id = datarow[0]
    self.nombre = datarow[1]
    self.apellido = datarow[2]
    self.cedula = datarow[3]
    self.telefono = datarow[4]
    self.expreso = datarow[5]
    self.nInscritos = datarow[6]   
