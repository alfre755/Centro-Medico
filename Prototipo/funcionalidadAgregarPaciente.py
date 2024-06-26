if op == "1":
        rut = input("Ingrese rut: ")
        nombre = input("Ingrese nombre : ")
        apellido = input("Ingrese apellido : ")
        fechaNacimiento = input("Ingrese fecha de nacimiento: ")
        sexo = input("Ingrese su sexo: ")
        telefono = input("Ingrese su telefono: ")
        direccion = input("Ingrese su direccion: ")
        correo = input("Ingrese su correo: ")
        paciente = Paciente(rut,nombre,apellido,fechaNacimiento,sexo,telefono,direccion,correo)
        dao.InsertarPaciente(paciente)
        
        def InsertarPaciente(self, Paciente:Paciente)->None:
        cursor = self.cnx.cursor()
        query = ("INSERT INTO paciente (Rut_Paciente,Nombre_Paciente,Apellido_Paciente,Fecha_Nacimiento,Sexo,Telefono,Direccion,Correo_Electronico) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)")
        data = (Paciente.getRut(),Paciente.getNombre(),Paciente.getApellido(),Paciente.getFechaNacimiento(),Paciente.getSexo(),Paciente.getTelefono(),Paciente.getDireccion(),Paciente.getCorreo())
        cursor.execute(query, data)
        self.cnx.commit()