## create a student class from the class person
## 16 febrero 2022
from distutils.log import error
from person import Person
from enroll import Enroll

class Student(Person):
    def __init__(self, nombre, apellido_paterno, apellido_materno, fdn, correo, telefono, address, international, course, payment_method):
        super().__init__(nombre, apellido_paterno, apellido_materno, fdn, correo, telefono, address)
        self.international = international
        self.enrolled = []
        self.course = course
        self.payment_method = payment_method

    def add_enrollment(self, enroll):
        if not isinstance(enroll, Enroll):
            raise error("Debes seleccionar un Curso")

    def is_course_finished(self):
        return False