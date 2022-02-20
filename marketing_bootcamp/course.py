# se crean los cursos
## course esta asociado con profesor, estudiante y enroll
## course lleva nombre del curso, horas totales del curso, clave del curso, fecha del curso, costo del curso. duración¿?

from professor import Professor
from student import Student

class Course:
    def __init__(self, name, hours, code, start_date, cost, registered_students, professor):
        self.name = name
        self.hours = hours
        self.code = code
        self.start_date = start_date
        self.cost = cost
        self.registered_students = registered_students
        self.professors = []

        if isinstance(professor, Professor):
            self.professors.append(professor)
        elif 

    