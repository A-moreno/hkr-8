supermercado
from stack import *
id = 0
class Productos:
    def __init__(self,precios,fecha):
        self.Precios = precios
        self.Fecha = fecha
        self.cambiosdeprecio = [[],[]]
        global id
        id +=1
        self.CodigodeProducto = id

    def Getfecha(self):
        return self.Fecha

    def Setfecha(self,new):
        self.fecha = new
        self.cambios[0].appennd(self.fecha)

    def Getprecio(self):
        return self.Precio

    def actualizarProducto(self,new,NewPrecio):
        self.Setprecio(NewPrecio)
        self.Setfecha(new)

    def Setprecio(self,NewPrecio):
        self.Precio = NewPrecio
        self.cambios[1].append(self.NewPrecio)

    def GetNoCambioPrecio(self):
        self.NoCambioPrecio = len(self.cambios[1])
        return self.NoCambioPrecio

    def GetCodigodeProducto(self):
        return self.CodigodeProducto

class Productos1:
    def __init__(self):
        self.ListaProductos = Stack()
        self.MaxRe = Stack()
        self.Prom = []
    def agregarProductos1(self,precio,fecha):
        self.ListaProductos.push(Productos(precio,fecha))

    def actualizar(self,precionuevo,fechanueva,id):
        for i in range(self.ListaProductos.size):
            Producto2 = self.ListaProductos.pop()
            if Producto2.CodigodeProducto = id:
                Producto2.actualizarProducto(fechanueva,precionuevo)
                self.ListaProductos.push(Producto2)
            else:
                self.ListaProductos.puch(Producto2)
    def MaximoRemarcados(self,n):
        for i in range(self.ListaProducts.size):
            Producto2 = self.ListaProductos.pop()
            Cam = len(Producto2.cambios[1])
            if  Cam >= n:
                self.MaxRemarcados.push(Producto2)
                self.ListaProductos.push(Producto2)
            else:
                self.ListaProductos.push(Producto2)
