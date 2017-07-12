from Queue import *
class hospital:
id = 0
    def __init__(self,fecha,turnoslibres,turnosocupados):
        
        self.TurnosLibres = turnoslibres
        self.turnosOcupados = turnosocupados
        self.FechaAtencion = fecha
        global id
        id +=1
        self.CodMedico = id

    def GetTurnoslibres(self):
        return self.TurnosLibres

    def GetNoturnosOcupados(self):
        return self.turnosOcupados

    def SetturnosOcupados(self,n):
        self.turnosOcupados = n

    def GetFechaAtencion(self):
        return self.FechaAtencion

    def GetCodeMedico(self):
        return self.CoddeMedico



class Medicos:

    def __init__(self):
        self.Docs= Queue()

    def AgregarMedico(self,especialidad,fecha,turnoslibres,turnosocupados):
        self.Docs.push(Medico(especialidad,fecha,turnoslibres,turnosocupados))
    def Verificar_Turno(self,codigo,fecha):
        a = True
        b = False
        for i in range(self.size):
            Doc=self.Docs.dequeue()
            if Doc.GetCoDdeMedico() = codigo:
                if Doc.GetFechaAtencion()= fecha:
                    if Doc.GetTurnoslibres() < Doc.GetturnosOcupados():
                        print a
                        self.Docs.enqueue(Doc)
                else:
                    print b
                    self.Docs.enqueue(Doc)
            else:
                self.Docs.enqueue(Doc)

class Agendas:

    def __init__(self):
        self.Gral = Queue()
        self.Especialidad = Queue()

    def Agendar(self,Medicos,fechaini,fechafin,turnosdisponibles):
        turOcupados = 0
        for i in range(Medicos.size())
            Medic = Medicos.dequeue()
            if Medic.GetFechaAtencion >= fechaini and Medic.GetFechaAtencion <= fechafin:
                if turnOcupados <= turnosdisponibles:
                    Disponibilidad = (Medic.GetTurnoslibres)-(Medic.GetturnosOcupados)
                    if Disponibilidad > 0:
                        turOcuapados += Disponibilidad
                        self.Gral.enqueue(Medic)
                        Medicos.enqueue(Medic)
    def AgendarEspecial(self,especialidad,Medicos,fechaini,fechafin,turnosdisponibles):
        turOcupados = 0
        for i in range(Medicos.size())
            Medic = Medicos.dequeue()
            if Medic.GetEspecialidad() == especialidad:
                if Medic.GetFechaAtencion >= fechaini and Medic.GetFechaAtencion <= fechafin:
                    if turnOcupados <= turnosdisponibles:
                        Disponibilidad = (Medic.GetNoTurnoslibres)-(Medic.GetNoturnosOcupados)
                        if Disponibilidad > 0:
                            turOcuapados += Disponibilidad
                            self.Especialidad.enqueue(Medic)
                            Medicos.enqueue(Medic)
