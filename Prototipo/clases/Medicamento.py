class Medicamento:
    def __init__(self,id,nombre,contradicciones) -> None:
        self.Id=id
        self.Nombre = nombre
        self.Contradicciones= contradicciones
        
    def getId(self):
        return self.Id
    
    def getNombre(self):
        return self.Nombre
    
    def getContradicciones(self):
        return self.Contradicciones
    
    def setId(self,nuevaId):
        self.Id = nuevaId
        
    def setNombre(self,nuevoNombre):
        self.Nombre = nuevoNombre
        
    def setContradicciones(self,nuevaContradiccion):
        self.Contradicciones = nuevaContradiccion