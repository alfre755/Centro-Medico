import mysql.connector
from typing import List
import os
from clases.Paciente import Paciente
from clases.FichaMedica import FichaMedica
from clases.Examen import Examen
from clases.Receta import Receta
from clases.RecetaFicha import RecetaFicha
from clases.Medicamento import Medicamento
class DAO:
    def __init__(self) -> None:
        self.cnx = mysql.connector.connect(user='root', password='root',
                              host='127.0.0.1',
                              database='centro_medico')
        
    
    def InsertarPaciente(self, Paciente:Paciente)->None:
        cursor = self.cnx.cursor()
        query = ("INSERT INTO paciente (Rut_Paciente,Nombre_Paciente,Apellido_Paciente,Fecha_Nacimiento,Sexo,Telefono,Direccion,Correo_Electronico) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)")
        data = (Paciente.getRut(),Paciente.getNombre(),Paciente.getApellido(),Paciente.getFechaNacimiento(),Paciente.getSexo(),Paciente.getTelefono(),Paciente.getDireccion(),Paciente.getCorreo())
        cursor.execute(query, data)
        self.cnx.commit()  
          
    def VerPacientes(self)->List[Paciente]:
        cursor = self.cnx.cursor()
        query = ("SELECT * FROM paciente")
        cursor.execute(query)

        PacientesList:List[Paciente] = []
        for (rut,nombre,apellido,fechaNacimiento,sexo,telefono,direccion,correo,contraseña) in cursor:
            paciente = Paciente(rut,nombre,apellido,fechaNacimiento,sexo,telefono,direccion,correo,contraseña)
            PacientesList.append(paciente)
        return PacientesList

    def verificar_paciente_existe(self, rutPaciente):
        cursor = self.cnx.cursor()
        query = "SELECT 1 FROM Paciente WHERE Rut_Paciente = %s"
        cursor.execute(query, (rutPaciente,))
        existe = cursor.fetchone() is not None
        cursor.close()
        return existe
    
    def verFicha(self,rutSeleccionado):
        cursor = self.cnx.cursor(dictionary=True)
        query = ("SELECT * FROM ficha_medica WHERE Rut_Paciente = %s")
        cursor.execute(query, (rutSeleccionado,))
        fichas_medicas = []
        for row in cursor.fetchall():
            ficha_medica = FichaMedica(
                row['ID_Atencion'],
                row['Fecha'],
                row['Motivo_Consulta'],
                row['Anamnesis'],
                row['Diagnostico'],
                row['Rut_Paciente'],
                row['Rut_Medico'],
                row['ID_Receta'],
                row['ID_Examen']
            )
            fichas_medicas.append(ficha_medica)
        cursor.close()
        return fichas_medicas
    
    def VerFichaMedica(self, id_atencion):
        cursor = self.cnx.cursor()
        query = "SELECT * FROM Ficha_Medica WHERE ID_Atencion = %s"
        cursor.execute(query, (id_atencion,))
        result = cursor.fetchone()
        cursor.close()

        if result:
            ficha = FichaMedica(
                id_atencion=result[0],
                fecha=result[1],
                motivo=result[2],
                anamnesis=result[3],
                diagnostico=result[4],
                rut_paciente=result[5],
                rut_medico=result[6],
                id_receta=result[7],
                id_examen=result[8]
            )
            return ficha
        else:
            return None

    
    def InsertarFichaMedica(self, ficha:FichaMedica):
        cursor = self.cnx.cursor()
        query = ("INSERT INTO Ficha_Medica (Fecha, Motivo_Consulta, Anamnesis, Diagnostico, Rut_Paciente, Rut_Medico, ID_Receta, ID_Examen) "
             "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")
        data = (ficha.getFecha(), ficha.getMotivo(), ficha.getAnamnesis(), ficha.getDiagnostico(), ficha.getRutPaciente(), ficha.getRutMedico(), ficha.getReceta(), ficha.getExamen())
        cursor.execute(query, data)
        self.cnx.commit()
        cursor.close()   
        
               
    def actualizarAnamnesisDiagnostico(self, id_atencion, nueva_anamnesis, nuevo_diagnostico):
        cursor = self.cnx.cursor()
        query = "UPDATE ficha_medica SET Anamnesis = %s, Diagnostico = %s WHERE ID_Atencion = %s"
        data = (nueva_anamnesis, nuevo_diagnostico, id_atencion)
        cursor.execute(query, data)
        self.cnx.commit()
        cursor.close()

    def InsertarExamen(self, examen:Examen):
        cursor = self.cnx.cursor()
        query = ("INSERT INTO Examen (Tipo_Examen, Descripcion, Resultado) "
                 "VALUES (%s, %s, %s)")
        data = (examen.getTipoExamen(), examen.getDescripcion(), examen.getResultado())
        cursor.execute(query, data)
        self.cnx.commit()
        cursor.close()
        return cursor.lastrowid
    
    def InsertarReceta(self, receta:Receta):
        cursor = self.cnx.cursor()
        query = ("INSERT INTO Receta (Descripcion, ID_Medicamento) "
                 "VALUES (%s, %s)")
        data = (receta.getDescripcion(), receta.getIdMedicamento())
        cursor.execute(query, data)
        self.cnx.commit()
        cursor.close()
        return cursor.lastrowid
    
    def AsociarRecetaConFichaMedica(self, atencion:RecetaFicha):
        cursor = self.cnx.cursor()
        query = ("INSERT INTO Atencion_Receta (ID_Atencion, ID_Receta) "
                 "VALUES (%s, %s)")
        data = (atencion.getIdAtencion(), atencion.getIdReceta())
        cursor.execute(query, data)
        self.cnx.commit()
        cursor.close()
        
    def VerMedicamentos(self) -> List[Medicamento]:
        cursor = self.cnx.cursor()
        query = ("SELECT * FROM medicamento")
        cursor.execute(query)

        MedicamentosList: List[Medicamento] = []
        for (id, nombre, contradicciones) in cursor:
            medicamento = Medicamento(id, nombre, contradicciones)
            MedicamentosList.append(medicamento)
    
        cursor.close()
        return MedicamentosList
    
    def ActualizarFichaMedicaReceta(self, id_atencion, id_receta):
        cursor = self.cnx.cursor()
        query = "UPDATE Ficha_Medica SET ID_Receta = %s WHERE ID_Atencion = %s"
        data = (id_receta, id_atencion)
        cursor.execute(query, data)
        self.cnx.commit()
        cursor.close()
    
    def ActualizarFichaMedicaExamen(self, id_atencion, id_examen):
        cursor = self.cnx.cursor()
        query = "UPDATE Ficha_Medica SET ID_Examen = %s WHERE ID_Atencion = %s"
        data = (id_examen, id_atencion)
        cursor.execute(query, data)
        self.cnx.commit()
        cursor.close()
