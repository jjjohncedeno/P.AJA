from Conexion import *
from objeto import *
from Personal import *

class Ventas(Objeto):
    personal = Personal()
    Detalle = ''
    Fecha = ''
    Costo = ''
    Cantidad = ''
    Total = ""
    Observaciones = ''
    headernames = ['Detalle','Fecha', 'Costo', 'Cantidad', 'Total', 'Responsaable','Observaciones']
    atributos = 'venta_id, venta_detalle, venta_fecha, venta_costo,venta_cantidad, venta_IdPersonal, venta_observaciones'
    tabla = " venta"
  
    def __init__(self):
        self.inicializar()

    def cargar(self):
        pass
        #TODO

  
    def guardar(self):
        conexion = self.conexion.getConnection()
        cursor= conexion.cursor()
        cursor.callproc('selectId', ("Venta",int(self.id)))
        if cursor.fetchone() is None:
            cursor.callproc("ingresoVenta",(self.contar(), self.Detalle,self.Fecha,float(self.Costo),int(self.Cantidad), float(self.Total), int(self.personal.id), self.Observaciones))
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
        cursor.callproc('modificoCompra',(int(self.id),  self.Detalle,self.Fecha,float(self.Costo),int(self.Cantidad), float(self.Total), int(self.personal.id), self.Observaciones))
        conexion.commit()
        cursor.close()


    def enlistar(self, listas):
        lista=[]
        for r in listas: 
            venta = Ventas()
            venta.mapeardatos(r)
            lista.append(venta)
        return lista

    def mapeardatos(self, datarow):
        self.id = datarow[0]
        self.Detalle = datarow[1]
        self.Fecha = datarow[2]
        self.Costo = datarow[3]
        self.Cantidad = datarow[4]
        self.Total = datarow[5]
        self.personal.id = datarow[6]
        self.Observaciones = datarow[7] 
