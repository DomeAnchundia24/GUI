from Dominio.Persona import Persona


class Estudiante(Persona):
    contador_estudiante = 0

    def __init__(self, cedula :str=None, nombre :str=None, apellido :str=None, email :str=None, telefono :str=None,
                 direccion :str=None, numero_libros :str=None, activo :str=None, carrera :str=None):
        super().__init__(cedula, nombre, apellido, email, telefono, direccion, carrera)
        self._numero_libros = numero_libros
        self._activo = activo
        Estudiante.contador_estudiante += 1

    @property
    def numero_libros(self):
        return self._numero_libros

    @numero_libros.setter
    def numero_libros(self, nuevo_numero_libros):
        self._numero_libros = nuevo_numero_libros

    @property
    def activo(self):
        return self._activo

    @activo.setter
    def activo(self, nuevo_activo):
        self._activo = nuevo_activo

    def pedir_libro(self):
        return True

    def devolver_libro(self):
        return True


if __name__ == "__main__":
    estudiante = Estudiante("123456789", "Domenica", "Anchundia", "dome@example.com", "1234567890", "Calle 123", 2,
                            True, "Literatuta")
    print(estudiante)


'''
Integrantes grupo #10: 
 Anchundia Valencia Domenica 
 Gallardo Alvarez Livington 
 Yepez Flores Jame
'''