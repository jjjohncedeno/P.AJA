from Conexion import *
from objeto import *
from Personal import *

class Semillero(Objeto):
  personal = Personal()
  tipo = ''
  
  modo = Modo()
  ninos = []
  transaccion = ''
  headernames = ['Cliente','Fecha','Modo','Transaccion']
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
    conexion.commit()
    cursor.close()


  def enlistar(self, listas):
    lista=[]
    for r in listas: 
      factura = Factura()
      factura.mapeardatos(r)
      lista.append(factura)
    return lista

  def mapeardatos(self, datarow):
    self.id = datarow[0]
    self.cliente.id = datarow[1]
    self.fecha = datarow[2]
    self.modo.id = datarow[3]
    self.transaccion = datarow[4]
    self.cliente.consultar()
    self.modo.consultar()

  def obtenerDetalles(self):
    detalle = Detalle()
    lista = detalle.cargar_todos()
    for detalle in lista:
      if detalle.factura == self.id:
        self.detalles.append(detalle)


      
