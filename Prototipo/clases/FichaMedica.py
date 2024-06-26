class FichaMedica:
    def __init__(self,id_atencion,fecha,motivo,anamnesis,diagnostico,rut_paciente,rut_medico,id_receta,id_examen) -> None:
        self.IdAtencion = id_atencion
        self.Fecha = fecha
        self.Motivo = motivo
        self.Anamnesis = anamnesis
        self.Diagnostico = diagnostico
        self.RutPaciente = rut_paciente
        self.RutMedico = rut_medico
        self.Receta = id_receta
        self.Examen = id_examen

    def getIdAtencion(self):
        return self.IdAtencion
    
    def getFecha(self):
        return self.Fecha

    def getMotivo(self):
        return self.Motivo

    def getAnamnesis(self):
        return self.Anamnesis

    def getDiagnostico(self):
        return self.Diagnostico

    def getRutPaciente(self):
        return self.RutPaciente

    def getRutMedico(self):
        return self.RutMedico

    def getReceta(self):
        return self.Receta

    def getExamen(self):
        return self.Examen

   
    def setIdAtencion(self, nuevoIdAtencion):
        self.IdAtencion = nuevoIdAtencion

    def setFecha(self, nuevaFecha):
        self.Fecha = nuevaFecha

    def setMotivo(self, nuevoMotivo):
        self.Motivo = nuevoMotivo

    def setAnamnesis(self, nuevaAnamnesis):
        self.Anamnesis = nuevaAnamnesis

    def setDiagnostico(self, nuevoDiagnostico):
        self.Diagnostico = nuevoDiagnostico

    def setRutPaciente(self, nuevoRutPaciente):
        self.RutPaciente = nuevoRutPaciente

    def setRutMedico(self, nuevoRutMedico):
        self.RutMedico = nuevoRutMedico

    def setReceta(self, nuevaReceta):
        self.Receta = nuevaReceta

    def setExamen(self, nuevoExamen):
        self.Examen = nuevoExamen
        
    def updateAnamnesis(self, nuevaAnamnesis):
        self.setAnamnesis(nuevaAnamnesis)

    def updateDiagnostico(self, nuevoDiagnostico):
        self.setDiagnostico(nuevoDiagnostico)