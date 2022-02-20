Proyect Python creating a marketing bootcamp enrollment system

*Objective* 
Create a platform where user can create a user and then suscribe to a marketing course, read it, and then be able to pay online. 

Software architecture: 

Class: Person
has
    Nombre: string
    Apellido Paterno: string
    Apellido Materno: string
    Fecha de Nacimiento: string
    Correo: string
    Teléfono: int
    Sexo: boolean
    País: string
    Ciudad: string

    child: Student
        Curso de interés: string
        Nivel de marketing: string - selection
    child: Professor ?¿

Class: Company

Class: Course

Class: enrollment