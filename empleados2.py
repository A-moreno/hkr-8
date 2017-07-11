
class Empleados:


	def movimiento(codigoEmpleado,cantidadtarea,tareas):
		self.CodigoEmpleado = codigo
		self.Cantidadtarea= cantidadtarea
        self.tareas = None

        global id
        id += 1
        self.id = id
        
        
    def Gettareas(self):
        return self.tareas

    def GetCanttarea(self):
        return self.Cantidadtarea

    def GetCodigodeEmpleado(self):
        return self.id
        
      
        
class Tareas:

    def __init__(self,tarearealizar,Area):
        self.tarearealizar=tarearealizar
        self.Area = Area
        self.listaD_areas = Stack()
        

    def Gettarearealizar(self)
        return self.tarearealizar
        

    def GetArea(self):
        return self.Area
        

    def AgregarTarea(self,tarearealizar,Area):
        self.listaD_areas.push(Tarea(tarearealizar,Area))
        

class Empleados:

    def __init__(self):
    
        self.nuevaTarea = Stack()
        self.Busca = []
        
    def AgregarEmpleados(self,cantidadtareas,tareas):
        self.nuevaTarea.push(Empleado(cantidadtareas,tareas))

    def BuscarEmpleado(self,inicio,fin):
    
        for i in range(self.nuevaTarea.size()):
            Empleado1 = self.Registro.pop()
            if Empleado1.id >= inicio and Empleado1.id <= fin:
                self.nuevaTarea.push(Empleado1)
                self.Busca.append(Empleado1)
            else:
                self.nuevaTarea.push(Empleado1)
    def Busqueda(self):
        print self.Busca

    def AsignarTarea(self):
        empleado2 = None
        for i in range(self.nuevaTarea.size()):
            empleado2 = self.nuevaTarea.pop()
            if empleado2.Cantidad == empleado2.tareas:
                self.nuevaTarea.push(Empleado2)
            else:
                empleado2.tareas = []
                while is not self.listareas.isEmpty() and empleado2.Cantidad =! len(empleado2.tareas):
                    tareas = self.listareas.pop()
                    empleado2.tareas.append(tareas)
self.nuevaTarea.push(empleado2) 
