class RecetaFicha:
    def __init__(self,id_atencion,id_receta) -> None:
        self.IdAtencion = id_atencion
        self.IdReceta = id_receta
        
    def getIdAtencion(self):
        return self.IdAtencion
    
    def getIdReceta(self):
        return self.IdReceta
    
    def setRut(self,nuevaIdAtencion):
        self.IdAtencion = nuevaIdAtencion
        
    def setRut(self,nuevaIdReceta):
        self.IdReceta = nuevaIdReceta