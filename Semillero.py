from Conexion import *
from objeto import *
from Personal import *

class Semillero(Objeto):
  personal = Personal()
  tipo = ''
  nIntegrantes = ''
  imagen = ''
  ubicacion = ''
  #idPersonal = ''
  ninos = []
  headernames = ['Tipo','N.Integrantes','Ubicacion']
  atributos = 'semillero_id, semillero_tipo, semillero_nIntegrantes,\
              semillero_imagen, semillero_ubicacion, semillero_idPersonal'
  tabla = ' semillero'

  def __init__(self):
    self.inicializar()

  def guardar(self):
    id = str(self.contar())
    query = self.query_insert + ' %s,%s,%s,%s,%s,%s '+self.query_insert_end
    conexion = self.conexion.getConnection()
    cursor= conexion.cursor()
    nIntegrantes = len(self.ninos)
    cursor.execute(query,(id,self.tipo,self.nIntegrantes,self.imagen,self.ubicacion,self.personal.id))
    conexion.commit()
    cursor.close()
    for nino in self.ninos:
      nino.semillero = id
      #detalle.id = i
      nino.guardar()
      #i = i+1
    print query

  def modificar(self):
    query = (self.query_update+' semillero_tipo = %s , \
            semillero_nIntegrantes = %s , semillero_imagen = %s ,\
            semillero_ubicacion = %s, semillero_idPersonal = %s '+self.query_update_end)
    print query
    conexion = self.conexion.getConnection()
    cursor= conexion.cursor()
    cursor.execute(query,(self.tipo,self.nIntegrantes,self.imagen,self.ubicacion,self.personal.id,self.id))
    conexion.commit()
    cursor.close()


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
    self.nIntegrantes = datarow[2]
    self.imagen = datarow[3]
    self.ubicacion = datarow[4]
    self.personal.i
    
    #self.cliente.consultar()
    #self.modo.consultar()

  """def obtenerDetalles(self):
    detalle = Detalle()
    lista = detalle.cargar_todos()
    for detalle in lista:
      if detalle.factura == self.id:
        self.detalles.append(detalle)"""


      
