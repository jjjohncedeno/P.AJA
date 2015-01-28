from Conexion import *
from objeto import * 

class Nino(Objeto):
  nombre = ''
  apellido = ''
  edad = ''
  esAlergico = ''
  observacion = ''
  semillero = ''
  representantes = []
  index = ''
  headernames = ['Nombre','Apellido','Edad','Alergico','Observacion']
  atributos = 'nino_id, nino_nombre, nino_apellido, \
               nino_edad,nino_esAlergico,nino_observacion, \
               nino_semillero'
  tabla = ' nino'
  
  def __init__(self):
    self.inicializar()

  def cargar(self):
    pass
     #TODO

  def idNino(self):
    self.index = self.contar()
  
  def guardar(self):
    id = str(self.contar())
    consulta = 'SELECT * FROM Nino WHERE nino_id = %s ;'
    conexion = self.conexion.getConnection()
    cursor= conexion.cursor()
    cursor.execute(consulta, (str(self.id),))
    if cursor.fetchone() is None:
      query = self.query_insert + ' %s,%s,%s,%s,%s,%s,%s '+self.query_insert_end
      cursor.execute(query,(id,self.nombre,self.apellido,self.edad,self.esAlergico,self.observacion,self.semillero))
      conexion.commit()
      cursor.close()
      for repre in self.representantes:
        repre.nino.id = id
        #detalle.id = i
        nino.guardar()
      print query
    else:
      cursor.close()
      self.modificar()

  def borrarNinos(self):
    self.eliminar_todo()  
  
  def borrarNino(self):
    self.eliminar()

  def modificar(self):
    query = (self.query_update+ 'nino_nombre= %s, nino_apellido= %s,nino_edad= %s ,nino_esAlergico = %s,nino_observacion = %s,nino_semillero=%s' + self.query_update_end)
    conexion = self.conexion.getConnection()
    cursor= conexion.cursor()
    cursor.execute(query,(self.nombre,self.apellido,self.edad,self.esAlergico,self.observacion,self.semillero,self.id))
    conexion.commit()
    cursor.close()


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
    self.semillero = datarow[6]
    
    
