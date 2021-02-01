from django.contrib import admin
from .models import Aluno, Professor

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    model = Aluno
    list_display = ("matricula", "nome", "cpf", "email", "dt_nascimento", "senha")


@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    model = Professor
    list_display = ("matricula", "nome", "cpf", "email", "dt_nascimento", "senha")
