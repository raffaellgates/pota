# Generated by Django 3.1 on 2021-02-01 19:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricula', models.CharField(max_length=25)),
                ('nome', models.CharField(max_length=150)),
                ('cpf', models.CharField(max_length=11)),
                ('email', models.CharField(max_length=80)),
                ('dt_nascimento', models.DateField()),
                ('senha', models.CharField(max_length=30)),
            ],
            options={
                'ordering': ('nome',),
            },
        ),
        migrations.CreateModel(
            name='DisciplinaPeriodo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disciplina', models.CharField(max_length=60)),
                ('periodo', models.IntegerField()),
                ('turma', models.CharField(max_length=30)),
            ],
            options={
                'ordering': ('disciplina',),
            },
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricula', models.CharField(max_length=25)),
                ('nome', models.CharField(max_length=150)),
                ('cpf', models.CharField(max_length=11)),
                ('email', models.CharField(max_length=80)),
                ('dt_nascimento', models.DateField()),
                ('senha', models.CharField(max_length=30)),
            ],
            options={
                'ordering': ('nome',),
            },
        ),
        migrations.CreateModel(
            name='Nota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.FloatField()),
                ('periodo', models.IntegerField()),
                ('alunoId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notas', to='boletim.aluno')),
                ('disciplinaId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notas', to='boletim.disciplinaperiodo')),
            ],
        ),
        migrations.AddField(
            model_name='disciplinaperiodo',
            name='professorId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='professores', to='boletim.professor'),
        ),
    ]
