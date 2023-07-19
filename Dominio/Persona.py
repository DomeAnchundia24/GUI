from abc import ABC, abstractmethod


class Persona(ABC):
    contador_persona = 0

    def __init__(self, cedula, nombre, apellido, email, telefono, direccion, carrera):
        self._cedula = cedula
        self._nombre = nombre
        self._apellido = apellido
        self._email = email
        self._telefono = telefono
        self._direccion = direccion
        self._carrera = carrera
        Persona.contador_persona += 1

    @property
    def cedula(self):
        return self._cedula

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, nuevo_apellido):
        self._apellido = nuevo_apellido

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, nuevo_email):
        self._email = nuevo_email

    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, nuevo_telefono):
        self._telefono = nuevo_telefono

    @property
    def direccion(self):
        return self._direccion

    @direccion.setter
    def direccion(self, nueva_direccion):
        self._direccion = nueva_direccion

    @property
    def carrera(self):
        return self._carrera

    @carrera.setter
    def carrera(self, nueva_carrera):
        self._carrera = nueva_carrera

    @abstractmethod
    def pedir_libro(self):
        pass

    @abstractmethod
    def devolver_libro(self):
        pass

    def __str__(self):
        return f"Nombre: {self.nombre} {self.apellido}\nCédula: {self.cedula}\nEmail: {self.email}\nTeléfono: " \
               f"{self.telefono}\nDirección: {self.direccion}\nCarrera: {self.carrera}"


'''
Integrantes grupo #10: 
 Anchundia Valencia Domenica 
 Gallardo Alvarez Livington 
 Yepez Flores Jame
'''