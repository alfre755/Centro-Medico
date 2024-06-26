class Medico:
    def __init__(self,rut,nombre,apellido,telefono,correo,especialidad) -> None:
        self.Rut = rut
        self.Nombre = nombre
        self.Apellido = apellido
        self.Telefono = telefono
        self.Correo = correo
        self.Especialidad = especialidad

    def getRut(self):
        return self.Rut
    
    def getNombre(self):
        return self.Nombre

    def getApellido(self):
        return self.Apellido

    def getTelefono(self):
        return self.Telefono
    
    def getCorreo(self):
        return self.Correo
    
    def getEspecialidad(self):
        return self.Especialidad
    
            
    def setRut(self,nuevoRut):
        self.Rut = nuevoRut

    def setNombre(self,nuevoNombre):
        self.Nombre = nuevoNombre
    
    def setApellido(self,nuevoApellido):
        self.Apellido = nuevoApellido
    
    def setEspecialidad(self,nuevaEspecialidad):
        self.Especialidad = nuevaEspecialidad
        
    def setTelefono(self,nuevoTelefono):
        self.Telefono = nuevoTelefono
        
    def setCorreo(self,nuevoCorreo):
        self.Correo = nuevoCorreo

