from django.contrib import admin
<<<<<<< HEAD
from .models import Aluno, Professor

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    model = Aluno
    list_display = ("matricula", "nome", "cpf", "email", "dt_nascimento", "senha")


@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    model = Professor
    list_display = ("matricula", "nome", "cpf", "email", "dt_nascimento", "senha")
=======

# Register your models here.
>>>>>>> fb7491ee821e03c946d50f6ff8a1f32f63944efe
