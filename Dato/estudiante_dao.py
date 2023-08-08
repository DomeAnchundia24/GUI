from pyodbc import IntegrityError, ProgrammingError

from Dato.conexion import Conexion
from Dominio.Estudiante import Estudiante


class Estudiantedao:
    _INSERTAR = "INSERT INTO Estudiantes (Cedula,Nombre,Apellido,Email,Carrera,Activo) VALUES (?,?,?,?,?,?)"
    _SELECIONAR_X_CEDULA = "select id, cedula, nombre, apellido, email, carrera, activo from Estudiantes " \
                           "where cedula = ?"
    @classmethod
    def insertar_estudiante(cls,Estudiante):
        respuesta= {'exito':False,'mensaje':''}
        flag_exito = False
        mensaje = ''
        try:
            with Conexion.obtenerCursor() as cursor:
                dato= (Estudiante.cedula,Estudiante.nombre, Estudiante.apellido,Estudiante.email,Estudiante.carrera,
                        Estudiante.activo)
                cursor.execute(cls._INSERTAR, dato)
                flag_exito = True
                mensaje = 'Ingreso Exitoso'
        except IntegrityError as e:
            flag_exito = False
            # print('La cedula que intenta ingresar ya existe')

            if e.__str__().find('cedula') > 0:
                print('Cédula ya ingresada.')
                mensaje = 'cedula ya ingresada'
            elif e.__str__().find('email') > 0:
                print('Email ya ingresado.')
                mensaje = 'email ya ingresado'
            else:
                print('Error de integridad')
                mensaje = 'error de integridad'

        except ProgrammingError as e:
            flag_exito = False
            print('Los datos ingresados no son del tamaño permitido')
            mensaje ='Los datos ingresados no son del tamaño permitido'

        except Exception as e:
            flag_exito = False
            print(e)

        finally:
            respuesta['exito'] = flag_exito
            respuesta['mensaje'] = mensaje
            return respuesta

    @classmethod
    def selecionar_por_cedula(cls, estudiante):
        persona_encontrada = None
        try:
            with Conexion.obtenerCursor() as cursor:
                datos = (estudiante.cedula,)
                resultado = cursor.execute(cls._SELECIONAR_X_CEDULA, datos)
                persona_encontrada = resultado.fetchone()
                estudiante.email = persona_encontrada[4]
                estudiante.nombre = persona_encontrada[2]
                estudiante.apellido = persona_encontrada[3]
                estudiante.carrera = persona_encontrada[5]
                estudiante.activo = persona_encontrada[6]
                estudiante.cedula = persona_encontrada[1]
                estudiante.id = persona_encontrada[0]
        except Exception as e:
            print(e)
        finally:
            return estudiante
if __name__ == '__main__':
    e1 = Estudiante()
    e1.cedula = '0987654311'
    e1.nombre = 'Lola'
    e1.apellido = 'Cruz'
    e1.email = 'lolc@gmail.com'
    e1.carrera = 'ADM'
    e1.activo = True
    #Estudiantedao.insertar_estudiante(e1)
    persona_encontrada = Estudiantedao.selecionar_por_cedula(e1)
    print(persona_encontrada)
