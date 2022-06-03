from django import forms


class Cursos(forms.Form):

    curso = forms.CharField()
    codigo = forms.IntegerField()

class Alumnos(forms.Form):

    nombre = forms.CharField(max_length=40)
    dni = forms.IntegerField()