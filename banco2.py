import Stack
class banco:
    

    def __init__(self, id, cuenta, fecha, saldo, tipo):
        self.id = id
        self.cuenta = cuenta
        self. fecha = fecha
        self.saldo = saldo
        

    def SetId(self, id):
        self.id = id

    def GetId(self):
        return self.id

    def setCuenta(self, cuenta):
        self.cuenta = cuenta

    def getCuenta(self):
        return self.id

    def setFecha(self, fecha):
        self.fecha = fecha

    def getFecha(self):
        return self.fecha

    def setSaldo(self, saldo):
        self.saldo = saldo

    def getSaldo(self):
        return self.saldo

    

    def __str__(self):
        cadena = "Id: " + self.id + ", Fecha: " + self.fecha + ", saldo: " + self.saldo 

        return cadena
    def __init__(self):
        self.s = Stack()

    def __str__(self):
        return self.s.items
        
    def lista(self):
        return self.s.lista()

    def saldo(self, cuenta):
        lista = self.lista()
        saldomaximo = 0.0
        for i in lista:
            if lista[i].cuenta == cuenta:
                if lista[i].tipo in "d":
                    saldomaximo += lista[i].saldo
                if lista[i].tipo == "r":
                    saldomaximo -= lista[i].saldo
        return saldomaximo

    def depositos(self, inf, sup):
        lista = self.lista()
        depositos = 0.0
        n = 0
        for i in lista:
            if lista[i].tipo in "d" and lista[i].fecha >= inf and lista[i].fecha <= sup:
                n += 1
                depositos += lista[i].saldo
        return "Numero de depositos: " + n + "\nCantidad depositada: " + depositos

    def retiros(self, inf, sup):
        lista = self.lista()
        retiros = 0.0
        n = 0
        for i in lista:
            if lista[i].tipo in "r" and lista[i].fecha >= inf and lista[i].fecha <= sup:
                n += 1
                retiros -= lista[i].saldo
        return "Numero de retiros: ",n,"\nCantidad retirada: ",retiros

    def banco2(self, banco):
        self.s.push(banco)

    def Stack(self, lista):
        if not self.s.isEmpty():
            self.s.items = []
        for i in lista:
            self.s.push(lista[i])
