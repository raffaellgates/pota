from django.db import models

class Professor(models.Model):
	matricula = models.CharField(max_length=25)
	nome = models.CharField(max_length=150)
<<<<<<< HEAD
	cpf = models.CharField(max_length=11)
	email = models.CharField(max_length=80)
	dt_nascimento = models.DateField()
	senha = models.CharField(max_length=30)
=======
	cpf = models.CharField(max_length=15)
	email = models.CharField(max_length=80)
	dt_nascimento = models.DateField()
>>>>>>> fb7491ee821e03c946d50f6ff8a1f32f63944efe

	class Meta:
		ordering = ('nome',)

	def __str__(self):
		return self.nome


class Aluno(models.Model):
	matricula = models.CharField(max_length=25)
	nome = models.CharField(max_length=150)
<<<<<<< HEAD
	cpf = models.CharField(max_length=11)
	email = models.CharField(max_length=80)
	dt_nascimento = models.DateField()
	senha = models.CharField(max_length=30) 
=======
	cpf = models.CharField(max_length=15)
	email = models.CharField(max_length=80)
	dt_nascimento = models.DateField()
>>>>>>> fb7491ee821e03c946d50f6ff8a1f32f63944efe

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
