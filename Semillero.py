from Conexion import *
from objeto import *
from Personal import *

class Semillero(Objeto):
  personal = Personal()
  tipo = ''
<<<<<<< HEAD
  nIntegrantes = ''
  imagen = ''
  ubicacion = ''
  #idPersonal = ''
  ninos = []
  headernames = ['Tipo','N.Integrantes','Ubicacion']
=======
  
  modo = Modo()
  ninos = []
  transaccion = ''
  headernames = ['Cliente','Fecha','Modo','Transaccion']
>>>>>>> b961b0cd1336c18ff2d8be191f5af5ea98dd1193
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
<<<<<<< HEAD
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
=======
    nIntegrantes = len(ninos)
    cursor.execute(query,(id,self.tipo,self.nIntegrantes,self.imagen,self.ubicacion,self.personal.id))
    conexion.commit()
    cursor.close()
    i = 1
    for detalle in self.detalles:
      detalle.factura = id
      detalle.id = i
      detalle.guardar()
      i = i+1
    print query

  def modificar(self):
    query = (self.query_update+' factura_cliente = %s , \
       factura_fecha = %s , factura_modo = %s ,\
      factura_transaccion = %s  '+self.query_update_end)
    print query
    conexion = self.conexion.getConnection()
    cursor= conexion.cursor()
    cursor.execute(query,(self.cliente.id,self.fecha,self.modo.id,self.transaccion,self.id))
>>>>>>> b961b0cd1336c18ff2d8be191f5af5ea98dd1193
    conexion.commit()
    cursor.close()


  def enlistar(self, listas):
    lista=[]
    for r in listas: 
<<<<<<< HEAD
      semillero = Semillero()
      semillero.mapeardatos(r)
      lista.append(semillero)
=======
      factura = Factura()
      factura.mapeardatos(r)
      lista.append(factura)
>>>>>>> b961b0cd1336c18ff2d8be191f5af5ea98dd1193
    return lista

  def mapeardatos(self, datarow):
    self.id = datarow[0]
<<<<<<< HEAD
    self.tipo = datarow[1]
    self.nIntegrantes = datarow[2]
    self.imagen = datarow[3]
    self.ubicacion = datarow[4]
    self.personal.i
    
    #self.cliente.consultar()
    #self.modo.consultar()

  """def obtenerDetalles(self):
=======
    self.cliente.id = datarow[1]
    self.fecha = datarow[2]
    self.modo.id = datarow[3]
    self.transaccion = datarow[4]
    self.cliente.consultar()
    self.modo.consultar()

  def obtenerDetalles(self):
>>>>>>> b961b0cd1336c18ff2d8be191f5af5ea98dd1193
    detalle = Detalle()
    lista = detalle.cargar_todos()
    for detalle in lista:
      if detalle.factura == self.id:
<<<<<<< HEAD
        self.detalles.append(detalle)"""
=======
        self.detalles.append(detalle)
>>>>>>> b961b0cd1336c18ff2d8be191f5af5ea98dd1193


      
