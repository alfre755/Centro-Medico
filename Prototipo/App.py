from DbConnector import DAO
from clases.Paciente import Paciente
from clases.FichaMedica import FichaMedica
from clases.Examen import Examen
from clases.Receta import Receta
from clases.RecetaFicha import RecetaFicha

import os


dao = DAO()

while True:
    rutMedico = "22222222-2"
    rutPacienteingresado= "45"
    print("{1} . Menu usuario")
    print("{2} . Menu medico")
    
    op = input("Seleccione una opcion")
    
   
        
               
    if op == "1":
        os.system("cls")
        opci = input("{1} . Para cargar informacion de fichas medicas")
        if opci =="1":
            fichas_medicas = dao.verFicha(rutPacienteingresado)
            for ficha in fichas_medicas:
                print("ID Atención:", ficha.getIdAtencion())
                print("Fecha:", ficha.getFecha())
                print("Motivo de Consulta:", ficha.getMotivo())
                print("Anamnesis:", ficha.getAnamnesis())
                print("Diagnóstico:", ficha.getDiagnostico())
                print("Rut Paciente:", ficha.getRutPaciente())
                print("Rut Médico:", ficha.getRutMedico())
                print("ID Receta:", ficha.getReceta())
                print("ID Examen:", ficha.getExamen())
                print("-" * 50)
            idSeleccion = input("Seleccione el ID de la ficha que desea ver")
            fichaVer = dao.VerFichaMedica(idSeleccion)
            if fichaVer:
                print(f"ID Atencion: {ficha.getIdAtencion()}")
                print(f"Fecha: {ficha.getFecha()}")
                print(f"Motivo: {ficha.getMotivo()}")
                print(f"Anamnesis: {ficha.getAnamnesis()}")
                print(f"Diagnostico: {ficha.getDiagnostico()}")
                print(f"RUT Paciente: {ficha.getRutPaciente()}")
                print(f"RUT Medico: {ficha.getRutMedico()}")
                print(f"ID Receta: {ficha.getReceta()}")
                print(f"ID Examen: {ficha.getExamen()}")
            else:
                print("No se encontró una ficha médica con ese ID de atención.")
    
    if op=="2":
        os.system("cls")
        print("{1} . Generar nuevo paciente y ficha")
        print("{2} . Cambiar la anamensis y diagnostico de un paciente")
        print("{3} . Generar nueva ficha de paciente atendido anteriormente")
        print("{4} . Recetar medicamentos y/o examenes")
        print("{5} . Cargar informacion de paciente atendido anteriormente")
        opcion = input("¡Que desea hacer?")
        if opcion == "1":
            input("Ingresar datos del paciente")
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
            input("Paciente agregado con exito")
            input("Crear ficha medica")
            
            fecha = input("Ingrese fecha de atencion: ")
            motivo = input("Ingrese el motivo de la consulta: ")
            anamnesis = input("Ingrese anamnesis: ")
            diagnostico = input("Ingrese diagnostico: ")
            rut_medico = rutMedico
            id_receta = input("Ingrese receta (deje vacío si no aplica): ") or None
            id_examen = input("Ingrese examen (deje vacío si no aplica): ") or None
            fichaNueva = FichaMedica(
            id_atencion=None,  # ID de atención es AUTO_INCREMENT
            fecha=fecha,
            motivo=motivo,
            anamnesis=anamnesis,
            diagnostico=diagnostico,
            rut_paciente=rut,
            rut_medico=rut_medico,
            id_receta=id_receta,
            id_examen=id_examen
            )
            dao.InsertarFichaMedica(fichaNueva)  
            print("Ficha médica insertada correctamente.")   
            
        elif opcion =="2":
            for paciente in dao.VerPacientes():
                print(
                f"{paciente.getRut()} | {paciente.getNombre()} | {paciente.getApellido()} | {paciente.getFechaNacimiento()} | {paciente.getSexo()} | {paciente.getTelefono()} | {paciente.getDireccion()} | {paciente.getCorreo()} "
                )
                print("-" * 50)
            rutSeleccionado = input("Escriba el rut del paciente que desea generar una nueva anamnesis y diagnostico")
            fichas_medicas = dao.verFicha(rutSeleccionado)
            for ficha in fichas_medicas:
                print("ID Atención:", ficha.getIdAtencion())
                print("Fecha:", ficha.getFecha())
                print("Motivo de Consulta:", ficha.getMotivo())
                print("Anamnesis:", ficha.getAnamnesis())
                print("Diagnóstico:", ficha.getDiagnostico())
                print("Rut Paciente:", ficha.getRutPaciente())
                print("Rut Médico:", ficha.getRutMedico())
                print("ID Receta:", ficha.getReceta())
                print("ID Examen:", ficha.getExamen())
                print("-" * 50)
            idSeleccionado = input("Seleccione la id de atencion que desea modificar")
            nuevaAnamnesis = input("Escriba la anamnesis")
            nuevoDiagnostico = input("Escriba el nuevo diagnostico")
            dao.actualizarAnamnesisDiagnostico(idSeleccionado, nuevaAnamnesis, nuevoDiagnostico)
            print("Anamnesis y diagnóstico actualizados correctamente.")
        elif opcion=="3":
            rutPaciente = input("Ingrese rut del paciente")
            dao.verificar_paciente_existe(rutPaciente)
            if dao.verificar_paciente_existe(rutPaciente) == True:
                fecha = input("Ingrese fecha de atencion: ")
                motivo = input("Ingrese el motivo de la consulta: ")
                anamnesis = input("Ingrese anamnesis: ")
                diagnostico = input("Ingrese diagnostico: ")
                rut_medico = rutMedico
                id_receta = input("Ingrese receta (deje vacío si no aplica): ") or None
                id_examen = input("Ingrese examen (deje vacío si no aplica): ") or None
                fichaNueva = FichaMedica(
                id_atencion=None,  # ID de atención es AUTO_INCREMENT
                fecha=fecha,
                motivo=motivo,
                anamnesis=anamnesis,
                diagnostico=diagnostico,
                rut_paciente=rutPaciente,
                rut_medico=rut_medico,
                id_receta=id_receta,
                id_examen=id_examen
                )
                dao.InsertarFichaMedica(fichaNueva)  
                print("Ficha médica insertada correctamente.")  
            else: 
                print("No existe el paciente")   
        elif opcion=="4":
            for paciente in dao.VerPacientes():
                print(
                f"{paciente.getRut()} | {paciente.getNombre()} | {paciente.getApellido()} | {paciente.getFechaNacimiento()} | {paciente.getSexo()} | {paciente.getTelefono()} | {paciente.getDireccion()} | {paciente.getCorreo()} "
                )
                print("-" * 50)
            rutSeleccionado = input("Ingrese el rut del paciente que desea recetar medicamentos y/o examenes")
            fichas_medicas = dao.verFicha(rutSeleccionado)
            for ficha in fichas_medicas:
                print("ID Atención:", ficha.getIdAtencion())
                print("Fecha:", ficha.getFecha())
                print("Motivo de Consulta:", ficha.getMotivo())
                print("Anamnesis:", ficha.getAnamnesis())
                print("Diagnóstico:", ficha.getDiagnostico())
                print("Rut Paciente:", ficha.getRutPaciente())
                print("Rut Médico:", ficha.getRutMedico())
                print("ID Receta:", ficha.getReceta())
                print("ID Examen:", ficha.getExamen())
                print("-" * 50)
            fichaSeleccionada = input("Ingrese el ID de la ficha que desea agregar la receta y/o examenes")
            opcionRecetaoExamen= input("1 Para examen | 2 para receta")
            if opcionRecetaoExamen == "1":
                tipo_examen = input("Ingrese el tipo de examen: ")
                descripcion_examen = input("Ingrese la descripción del examen: ")
                resultado_examen = input("Ingrese el resultado del examen: ")
                examen = Examen(None, tipo_examen, descripcion_examen, resultado_examen)
                id_examen = dao.InsertarExamen(examen)
                dao.ActualizarFichaMedicaExamen(fichaSeleccionada,id_examen)
            else:
                descripcion_receta = input("Ingrese la descripción de la receta: ")
                input("A continuacion se le mostrara la lista de medicamentos")
                for medicamento in dao.VerMedicamentos():
                    print(f"ID: {medicamento.getId()}")
                    print(f"Nombre: {medicamento.getNombre()}")
                    print(f"Contradicciones: {medicamento.getContradicciones()}")
                    print("-" * 20)
                id_medicamento = input("Ingrese ID del medicamento: ")
                receta = Receta(None,descripcion_receta, id_medicamento)
                id_receta = dao.InsertarReceta(receta)
                input("Receta ingresada con exito")
                dao.ActualizarFichaMedicaReceta(fichaSeleccionada, id_receta)
        else:
            opcionver = input("1 Para ver la lista de pacientes | 2 Para buscar informacion con el rut")
            if opcionver == "1":
                for paciente in dao.VerPacientes():
                    print(
                    f"{paciente.getRut()} | {paciente.getNombre()} | {paciente.getApellido()} | {paciente.getFechaNacimiento()} | {paciente.getSexo()} | {paciente.getTelefono()} | {paciente.getDireccion()} | {paciente.getCorreo()} "
                    )
                    print("-" * 50)
                seleccion = input("Selecionne el rut del paciente que desea ver")
                fichas_medicas = dao.verFicha(seleccion)
                for ficha in fichas_medicas:
                    print("ID Atención:", ficha.getIdAtencion())
                    print("Fecha:", ficha.getFecha())
                    print("Motivo de Consulta:", ficha.getMotivo())
                    print("Anamnesis:", ficha.getAnamnesis())
                    print("Diagnóstico:", ficha.getDiagnostico())
                    print("Rut Paciente:", ficha.getRutPaciente())
                    print("Rut Médico:", ficha.getRutMedico())
                    print("ID Receta:", ficha.getReceta())
                    print("ID Examen:", ficha.getExamen())
                    print("-" * 50)
                idSeleccion = input("Seleccione el ID de la ficha que desea ver")
                fichaVer = dao.VerFichaMedica(idSeleccion)
                if fichaVer:
                    print(f"ID Atencion: {ficha.getIdAtencion()}")
                    print(f"Fecha: {ficha.getFecha()}")
                    print(f"Motivo: {ficha.getMotivo()}")
                    print(f"Anamnesis: {ficha.getAnamnesis()}")
                    print(f"Diagnostico: {ficha.getDiagnostico()}")
                    print(f"RUT Paciente: {ficha.getRutPaciente()}")
                    print(f"RUT Medico: {ficha.getRutMedico()}")
                    print(f"ID Receta: {ficha.getReceta()}")
                    print(f"ID Examen: {ficha.getExamen()}")
                else:
                    print("No se encontró una ficha médica con ese ID de atención.")
                
            else:
                seleccion = input("Selecionne el rut del paciente que desea ver")
                fichas_medicas = dao.verFicha(seleccion)
                for ficha in fichas_medicas:
                    print("ID Atención:", ficha.getIdAtencion())
                    print("Fecha:", ficha.getFecha())
                    print("Motivo de Consulta:", ficha.getMotivo())
                    print("Anamnesis:", ficha.getAnamnesis())
                    print("Diagnóstico:", ficha.getDiagnostico())
                    print("Rut Paciente:", ficha.getRutPaciente())
                    print("Rut Médico:", ficha.getRutMedico())
                    print("ID Receta:", ficha.getReceta())
                    print("ID Examen:", ficha.getExamen())
                    print("-" * 50)
                idSeleccion = input("Seleccione el ID de la ficha que desea ver")
                fichaVer = dao.VerFichaMedica(idSeleccion)
                if fichaVer:
                    print(f"ID Atencion: {ficha.getIdAtencion()}")
                    print(f"Fecha: {ficha.getFecha()}")
                    print(f"Motivo: {ficha.getMotivo()}")
                    print(f"Anamnesis: {ficha.getAnamnesis()}")
                    print(f"Diagnostico: {ficha.getDiagnostico()}")
                    print(f"RUT Paciente: {ficha.getRutPaciente()}")
                    print(f"RUT Medico: {ficha.getRutMedico()}")
                    print(f"ID Receta: {ficha.getReceta()}")
                    print(f"ID Examen: {ficha.getExamen()}")
                else:
                    print("No se encontró una ficha médica con ese ID de atención.")

                       


     
