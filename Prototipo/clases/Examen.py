class Examen:
    def __init__(self,id,tipo,descripcion,resultado) -> None:
        self.IdExamen = id
        self.TipoExamen = tipo
        self.Descripcion = descripcion
        self.Resultado = resultado

    def getIdExamen(self):
        return self.IdExamen


    def getTipoExamen(self):
        return self.TipoExamen

    def getDescripcion(self):
        return self.Descripcion

    def getResultado(self):
        return self.Resultado

    # Setters
    def setIdExamen(self, nuevaId):
        self.IdExamen = nuevaId

    def setTipoExamen(self, nuevoTipo):
        self.TipoExamen = nuevoTipo

    def setDescripcion(self, nuevaDescripcion):
        self.Descripcion = nuevaDescripcion

    def setResultado(self, nuevoResultado):
        self.Resultado = nuevoResultado