from Conexion import *
from objeto import *
from Personal import *

class Compras(Objeto):
    personal = Personal()
    Detalle = ''
    Fecha = ''
    Gasto = ''
    Tipo = ""
    Observaciones = ''
    id = 0
    headernames = ['Detalle','Fecha', 'Gasto', 'Tipo', 'Responsaable','Observaciones']
    atributos = 'compra_id, compra_detalle, compra_fecha, compra_gasto, compra_IdPersonal, compra_observaciones'
    tabla = "Compra"
  
    def __init__(self):
        self.inicializar()

    def cargar(self):
        pass
        #TODO

  
    def guardar(self):
        conexion = self.conexion.getConnection()
        cursor= conexion.cursor()
        cursor.callproc('selectId', ("Compra",int(self.id)))
        if cursor.fetchone() is None:
            cursor.callproc("ingresoCompra",(self.contar(), self.Detalle,self.Fecha,self.Tipo,int(self.Gasto), int(self.personal.id), self.Observaciones))
            conexion.commit()
            cursor.close()
        else:
            cursor.close()
            self.modificar()

    def borrarJuegos(self):
        self.eliminar_todo()

    def borrarJuego(self):
        self.eliminar()

    def modificar(self):
        conexion = self.conexion.getConnection()
        cursor= conexion.cursor()
        cursor.callproc('modificoCompra',(int(self.id), self.Detalle,self.Fecha,self.Tipo,int(self.Gasto), int(self.personal.id), self.Observaciones))
        conexion.commit()
        cursor.close()


    def enlistar(self, listas):
        lista=[]
        for r in listas: 
            compra = Compra()
            compra.mapeardatos(r)
            lista.append(compra)
        return lista

    def mapeardatos(self, datarow):
        self.id = datarow[0]
        self.Detalle = datarow[1]
        self.Fecha = datarow[2]
        self.Gasto = datarow[3]
        self.Tipo = datarow[4]
        self.personal.id = datarow[5]
        self.Observaciones = datarow[6]      
