from django.forms import ModelForm, EmailInput

from docentes.models import Docente, Institucion, Alumno, Materia


class DocenteFormulario(ModelForm):
    class Meta:
        model = Docente
        fields = ('nombre', 'apellido', 'sexo', 'email', 'activo', 'materia', 'institucion', 'cedula', 'celular', 'fecha_de_nacimiento')
        widgets = {
            'email': EmailInput(attrs={'type': 'email'})
        }

class MateriaFormulario(ModelForm):
    class Meta:
        model = Materia
        fields = ('nombre', 'horas', 'institucion', 'alumno')

class AlumnoFormulario(ModelForm):
    class Meta:
        model = Alumno
        fields = ('nombre', 'apellido', 'sexo', 'email', 'institucion', 'cedula', 'celular', 'fecha_de_nacimiento')

class InstitucionFormulario(ModelForm):
    class Meta:
        model = Institucion
        fields = ('nombre', 'direccion', 'numero')