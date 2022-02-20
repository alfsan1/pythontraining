from msilib.schema import Error
from address import Address

class Person:
    def __init__(self, nombre, apellido_paterno, apellido_materno, fdn, correo, telefono, address):
        self.nombre = nombre
        self.appelido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.fecha_de_nacimiento = fdn
        self.correo = correo
        self.telefono = telefono
        self.addresses = []

        if isinstance(address, Address):
            self.addresses.append(address)
        else:
            raise Error("Necesitas introducir tu dirección")


