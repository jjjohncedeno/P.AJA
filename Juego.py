from Conexion import *
from objeto import * 
class Juego(Objeto):
    nombre = ''
    imagen = ''
    area = ''
    ubicacion = ''
    responsable= ''
    headernames = ['Nombre','Imagen','Area','Ubicacion','Responsable']
    atributos = 'JuegoId, JuegoNombre, JuegoImagen, JuegoUbicacion,JuegoResponsable'
    tabla = ' juego'
  
    def __init__(self):
        self.inicializar()

    def cargar(self):
        pass
        #TODO

  
    def guardar(self):
        consulta = 'SELECT * FROM Juego WHERE personal_id = %s ;'
        conexion = self.conexion.getConnection()
        cursor= conexion.cursor()
        cursor.execute(consulta, (str(self.id),))
        if cursor.fetchone() is None:
            query = self.query_insert + '%s,%s,%s,%s,%s '+self.query_insert_end
            cursor.execute(query,(str(self.contar()),self.nombre,self.imagen,self.area,self.ubicacion,self.responsable))  
            conexion.commit()
            cursor.close()
            print query
        else:
            cursor.close()
            self.modificar()

    def borrarJuegos(self):
        self.eliminar_todo()  
  
    def borrarJuego(self):
        self.eliminar()

    def modificar(self):
        query = (self.query_update+ 'JuegoNombre= %s,JuegoArea= %s,JuegoUbicacion= %s ,JuegoResponsable = %s' + self.query_update_end)
        conexion = self.conexion.getConnection()
        cursor= conexion.cursor()
        cursor.execute(query,(self.nombre,self.imagen,self.area,self.ubicacion,self.responsable,self.id))
        conexion.commit()
        cursor.close()


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
        self.personal = datarow[5]      
