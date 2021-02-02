from django.db import models
from django.contrib.auth.models import User

class Professor(models.Model):
	usuario = models.OneToOneField(User, related_name = 'professor', on_delete = models.CASCADE)
	nome = models.CharField(max_length=150)
	cpf = models.CharField(max_length=11)
	dt_nascimento = models.DateField()

	class Meta:
		ordering = ('nome',)

	def __str__(self):
		return self.nome


class Aluno(models.Model):
	usuario = models.OneToOneField(User, related_name = 'aluno', on_delete = models.CASCADE)
	nome = models.CharField(max_length=150)
	cpf = models.CharField(max_length=11)
	dt_nascimento = models.DateField() 

	class Meta:
		ordering = ('nome',)

	def __str__(self):
		return self.nome


class DisciplinaPeriodo(models.Model):
	disciplina = models.CharField(max_length=60)
	periodo = models.IntegerField()
	turma = models.CharField(max_length=30)
	professorId = models.ForeignKey(Professor,
		related_name='professores',
		on_delete=models.CASCADE)

	class Meta:
		ordering = ('disciplina',)

	def __str__(self):
		return self.disciplina


class Nota(models.Model):
	valor = models.FloatField()
	periodo = models.IntegerField()
	alunoId = models.ForeignKey(Aluno,
		related_name='notas',
		on_delete=models.CASCADE)
	disciplinaId = models.ForeignKey(DisciplinaPeriodo,
		related_name='notas',
		on_delete=models.CASCADE)
	
	class Meta:
		ordering = ('valor',)

	def _str_(self):
		return self.valor
