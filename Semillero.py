from Conexion import *
from objeto import *
from Personal import *
from Nino import *

class Semillero(Objeto):
  personal = Personal()
  tipo = ''
  imagen = ''
  ubicacion = ''
  ninos = []
  headernames = ['Tipo','Imagen','Ubicacion']
  atributos = 'semillero_id, semillero_tipo, \
              semillero_imagen, semillero_ubicacion, semillero_idPersonal'
  tabla = ' semillero'
   

  def __init__(self):
    self.inicializar()

  def guardar(self):
    self.id = self.contar()
    #query = self.query_insert + ' %s,%s,%s,%s,%s '+self.query_insert_end
    conexion = self.conexion.getConnection()
    cursor= conexion.cursor()
    cursor.callproc('ingresoSemillero',(self.id,self.tipo,self.imagen,self.ubicacion,self.personal.id))
    conexion.commit()
    cursor.close()
    for nino in self.ninos:
      nino.semillero.id = self.id
      nino.guardar()

  def modificar(self):
    query = (self.query_update+' semillero_tipo = %s , \
            semillero_imagen = %s , semillero_ubicacion = %s, semillero_idPersonal = %s ' + self.query_update_end)
    print query
    conexion = self.conexion.getConnection()
    cursor= conexion.cursor()
    cursor.execute(query,(self.tipo,self.imagen,self.ubicacion,self.personal.id,self.id))
    #cursor.execute(query,(id,self.tipo,self.nIntegrantes,self.imagen,self.ubicacion,self.personal.id))
    conexion.commit()
    cursor.close()

  def enlistarNino(self):
    query = ('select * from Nino where nino_semillero = %s')
    conexion = self.conexion.getConnection()
    cursor= conexion.cursor()
    cursor.execute(query,(self.id,))
    result = cursor.fetchall()
    cursor.close()
    print result
    for r in result: 
      nn = Nino()
      nn.mapeardatos(r)
      self.ninos.append(nn)

  def enlistar(self, listas):
    lista=[]
    for r in listas: 
      semillero = Semillero()
      semillero.mapeardatos(r)
      lista.append(semillero)
    return lista

  def mapeardatos(self, datarow):
    self.id = datarow[0]
    self.tipo = datarow[1]
    self.imagen = datarow[2]
    self.ubicacion = datarow[3]
    self.personal.id = datarow[4]
