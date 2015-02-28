from Conexion import *
from objeto import * 
from Personal import *

class Juego(Objeto):
    personal = Personal()
    nombre = ''
    imagen = ''
    area = ''
    ubicacion = ''
    #responsable= ''
    headernames = ['Nombre','Imagen','Area','Ubicacion','Responsable']
    atributos = 'juego_id, juego_nombre, juego_imagen, juego_area, juego_ubicacion, juego_IdPersonal '
    tabla = ' juego'
  
    def __init__(self):
        self.inicializar()

    def cargar(self):
        pass
        #TODO

  
    def guardar(self):
        id = self.contar()
        #print id
        consulta = 'SELECT * FROM Juego WHERE juego_id = %s;'
        conexion = self.conexion.getConnection()
        cursor= conexion.cursor()
        cursor.execute(consulta, (str(self.id)))
        if cursor.fetchone() is None:
            #query = self.query_insert + '%s,%s,%s,%s,%s,%s ' + self.query_insert_end
            cursor.callproc('ingresoJuego',(id,self.nombre,self.imagen,self.area,self.ubicacion,self.personal.id))
            conexion.commit()
            cursor.close()
            #print query
        else:
            cursor.callproc('modificoJuego',(id,self.nombre,self.imagen,self.area,self.ubicacion,self.personal.id))
            cursor.close()
            #self.modificar()

    def borrarJuegos(self):
        self.eliminar_todo()  
  
    def borrarJuego(self):
        self.eliminar()

    """def modificar(self):
        query = (self.query_update+ 'juego_nombre=%s, juego_imagen= %s,juego_area= %s ,juego_ubicacion = %s, juego_IdPersonal = %s' + self.query_update_end)
        conexion = self.conexion.getConnection()
        cursor= conexion.cursor()
        cursor.execute(query,(self.nombre,self.imagen,self.area,self.ubicacion,self.personal.id,self.id))
        conexion.commit()
        cursor.close()"""


    def enlistar(self, listas):
        lista=[]
        for r in listas: 
            juego = Juego()
            juego.mapeardatos(r)
            lista.append(juego)
        return lista

    def mapeardatos(self, datarow):
        self.id = datarow[0]
        self.nombre = datarow[1]
        self.imagen = datarow[2]
        self.area = datarow[3]
        self.ubicacion = datarow[4]
        self.personal.id = datarow[5]      
