from Conexion import *
from objeto import * 
class Personal(Objeto):
  nombre = ''
  apellido = ''
  cedula = ''
  tipo = ''
  telefono = ''
  direccion = ''
  sexo= ''
  correo = ''
  carrera = ''
  facultad = ''
  headernames = ['Nombre','Apellido','Cedula','Telefono','Tipo','Direccion','Sexo','Correo','Carrera','Facultad']
  atributos = 'personal_id, personal_nombre, personal_apellido, \
               personal_cedula,personal_telefono,personal_tipo, \
			   personal_direccion,personal_sexo,personal_correo, \
			   personal_carrera,personal_facultad'
  tabla = ' personal'
  
  def __init__(self):
    self.inicializar()

  def cargar(self):
    pass
     #TODO

  
  def guardar(self):
    consulta = 'SELECT * FROM Personal WHERE personal_id = %s ;'
    conexion = self.conexion.getConnection()
    cursor= conexion.cursor()
    cursor.execute(consulta, (str(self.id),))
    if cursor.fetchone() is None:
      query = self.query_insert + ' %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s '+self.query_insert_end
      cursor.execute(query,(str(self.contar()),self.nombre,self.apellido,self.cedula,self.telefono,self.tipo,self.direccion,self.sexo,self.correo,self.carrera,self.facultad))
      
      conexion.commit()
      cursor.close()
      print query
    else:
      cursor.close()
      self.modificar()

  def borrarClientes(self):
    self.eliminar_todo()  
  
  def borrarCliente(self):
    self.eliminar()

  def modificar(self):
    query = (self.query_update+ 'personal_nombre= %s, personal_apellido= %s,personal_cedula= %s ,personal_telefono = %s,personal_tipo, personal_direccion = %s,personal_sexo = %s,personal_correo = %s,personal_carrera = %s,personal_facultad = %s' + self.query_update_end)
    conexion = self.conexion.getConnection()
    cursor= conexion.cursor()
    cursor.execute(query,(self.nombre,self.apellido,self.cedula,self.telefono,self.tipo,self.direccion,self.sexo,self.correo,self.carrera,self.facultad,self.id))
    conexion.commit()
    cursor.close()


  def enlistar(self, listas):
    lista=[]
    for r in listas: 
      personal = Personal()
      personal.mapeardatos(r)
      lista.append(personal)
    return lista

  def mapeardatos(self, datarow):
    self.id = datarow[0]
    self.nombre = datarow[1]
    self.apellido = datarow[2]
    self.cedula = datarow[3]
    self.telefono = datarow[4]
    self.tipo = datarow[5]
    self.direccion = datarow[6]
    self.sexo = datarow[7]
    self.correo = datarow[8]
    self.carrera = datarow[9]
    self.facultad = datarow[10]
    
