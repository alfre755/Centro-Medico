class Paciente:
    def __init__(self,rut,nombre,apellido,fechaNacimiento,sexo,telefono,direccion,correo,contraseña='default') -> None:
        self.Rut = rut
        self.Nombre = nombre
        self.Apellido = apellido
        self.FechaNacimiento = fechaNacimiento
        self.Sexo = sexo
        self.Telefono = telefono
        self.Direccion = direccion
        self.Correo = correo
        self.Contraseña = contraseña

    def getRut(self):
        return self.Rut
    
    def getNombre(self):
        return self.Nombre

    def getApellido(self):
        return self.Apellido

    def getFechaNacimiento(self):
        return self.FechaNacimiento

    def getSexo(self):
        return self.Sexo
    
    def getTelefono(self):
        return self.Telefono
    
    def getDireccion(self):
        return self.Direccion
    
    def getCorreo(self):
        return self.Correo
    
    def getContraseña(self):
        return self.Contraseña
    
            
    def setRut(self,nuevoRut):
        self.Rut = nuevoRut

    def setNombre(self,nuevoNombre):
        self.Nombre = nuevoNombre
    
    def setApellido(self,nuevoApellido):
        self.Apellido = nuevoApellido
    
    def setFechaNacimiento(self,nuevaFecha):
        self.FechaNacimiento = nuevaFecha
    
    def setSexo(self,nuevoSexo):
        self.Sexo = nuevoSexo
        
    def setTelefono(self,nuevoTelefono):
        self.Telefono = nuevoTelefono
    
    def setDireccion(self,nuevaDireccion):
        self.Direccion = nuevaDireccion
        
    def setCorreo(self,nuevoCorreo):
        self.Correo = nuevoCorreo
        
    def setContraseña(self,nuevaContraseña):
        self.Contraseña = nuevaContraseña

