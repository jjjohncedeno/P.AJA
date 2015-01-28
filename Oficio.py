from Conexion import *
from objeto import * 
class Oficio(Objeto):
    Detalle = ''
    Destinatario = ''
    Estado = ''
    Tramite = ''
    Respuesta = ''
    Observaciones = ''
    personal=''
    headernames = ['Detalle','Destinatario','Estado','Tramite','Respuesta', 'Observaciones']
    atributos = 'oficio_id, oficio_detalle, oficio_destinatario, oficio_estado, oficio_tramite, oficio_respuesta, oficio_observaciones, oficio_IdPersonal'
    tabla = 'oficio'
  
    def __init__(self):
        self.inicializar()

    def cargar(self):
        pass
        #TODO

  
    def guardar(self):
        consulta = 'SELECT * FROM Oficio WHERE oficio_id = %s;'
        conexion = self.conexion.getConnection()
        cursor = conexion.cursor()
        cursor.execute(consulta, (str(self.id)))
        if cursor.fetchone() is None:
            query = self.query_insert + '%s,%s,%s,%s,%s,%s,%s,%s ' + self.query_insert_end
            cursor.execute(query,(str(self.contar()),self.Detalle,self.Destinatario,self.Estado ,self.Tramite , self.Respuesta, self.Observaciones, 1))
            conexion.commit()
            cursor.close()
            print query
        else:
            cursor.close()
            self.modificar()

    def borrarOficios(self):
        self.eliminar_todo()  
  
    def borrarOficio(self):
        self.eliminar()

    def modificar(self):
        query = (self.query_update+ 'oficio_id = %s , oficio_detalle = %s, oficio_destinatario = %s, oficio_estado = %s, oficio_tramite = %s, oficio_respuesta = %s, oficio_observaciones = %s, oficio_IdPersonal = %s' + self.query_update_end)
        conexion = self.conexion.getConnection()
        cursor= conexion.cursor()
        cursor.execute(query,(self.Detalle,self.Destinatario,self.Estado ,self.Tramite , self.Respuesta, self.Observaciones,1))
        conexion.commit()
        cursor.close()


    def enlistar(self, listas):
        lista=[]
        for r in listas: 
            oficio = Oficio()
            oficio.mapeardatos(r)
            lista.append(oficio)
        return lista

    def mapeardatos(self, datarow):
        self.id = datarow[0]
        self.Detalle = datarow[1]
        self.Destinatario = datarow[2]
        self.Estado = datarow[3]
        self.Tramite = datarow[4]
        self.Respuesta = datarow[5]
        self.Observaciones = datarow[6]
        self.personal = datarow[7]  
