from django.contrib import admin
from .models import Aluno, Professor

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    model = Aluno
    list_display = ( "nome", "cpf", "dt_nascimento")


@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    model = Professor
    list_display = ( "nome", "cpf", "dt_nascimento")
