class Receta:
    def __init__(self,id,descripcion,id_medicamento) -> None:
        self.Id = id
        self.Descripcion = descripcion
        self.IdMedicamento = id_medicamento
        
        # Getters
    def getId(self):
        return self.Id

    def getDescripcion(self):
        return self.Descripcion

    def getIdMedicamento(self):
        return self.IdMedicamento

    # Setters
    def setId(self, nuevaId):
        self.Id = nuevaId

    def setDescripcion(self, nuevaDescripcion):
        self.Descripcion = nuevaDescripcion

    def setIdMedicamento(self, nuevaIdMedicamento):
        self.IdMedicamento = nuevaIdMedicamento