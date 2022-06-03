from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name="Inicio"),
    path('cursos', views.cursos, name="Cursos"),
    path('alumnos', views.alumnos, name="Alumnos"),
    path('profesores', views.profesores, name="Profesores"),
]