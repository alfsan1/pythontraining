## perfil del profesor
## que características tiene
## 16 febrero 2022
## courses será sobre las clases asignadas


from msilib.schema import Error
from person import Person
from address import Address
from course import Course

class Professor(Person):
    def __init__(self, nombre, apellido_paterno, apellido_materno, fdn, correo, telefono, address, salario):
        super().__init__(nombre, apellido_paterno, apellido_materno, fdn, correo, telefono, address)
        self.salario = salario
        self.courses = []

    def add_course(self, course):
        if not isinstance(course, Course):
            raise Error("Se necesita curso...")

        self.courses.append(course)

